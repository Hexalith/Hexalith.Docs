import contextlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from urllib.error import HTTPError
from unittest.mock import patch
from zipfile import ZipFile

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import verify_published_readmes as verify


def leaf(version, listed=True):
    return {"catalogEntry": {"id": "Example", "version": version, "listed": listed},
            "packageContent": f"https://api.nuget.org/example/{version}.nupkg"}


def archive(readme="text\r\n", member="docs/Package.md"):
    stream = io.BytesIO()
    with ZipFile(stream, "w") as package:
        package.writestr("Example.nuspec", f'<package xmlns="urn:test"><metadata>'
                         f'<id>Example</id><version>2.0.0</version><readme>{member}</readme>'
                         '</metadata></package>')
        if readme is not None:
            package.writestr("docs/Package.md", readme)
    return stream.getvalue()


class PublishedReadmeTests(unittest.TestCase):
    def test_paginated_registration_ignores_unlisted_and_prerelease(self):
        page = {"@id": "https://api.nuget.org/example/page.json"}
        index = {"items": [{"items": [leaf("2.0.0")]}, page]}
        latest_page = {"items": [leaf("2.1.0", False), leaf("3.0.0-rc.1")]}
        with patch.object(verify, "download", side_effect=[json.dumps(index), json.dumps(latest_page)]):
            self.assertEqual(verify.latest_stable("Example"), ("2.0.0", leaf("2.0.0")["packageContent"]))

    def test_prerelease_only_package_fails(self):
        index = {"items": [{"items": [leaf("3.0.0-beta.1")]}]}
        with patch.object(verify, "download", return_value=json.dumps(index)):
            with self.assertRaisesRegex(verify.VerificationError, "no listed stable version"):
                verify.latest_stable("Example")

    def test_follows_nuspec_path_and_checks_package_identity(self):
        self.assertEqual(verify.package_readme(archive(member="docs\\Package.md"), "Example", "2.0.0"), b"text\r\n")
        with self.assertRaisesRegex(verify.VerificationError, "README target"):
            verify.package_readme(archive(readme=None), "Example", "2.0.0")
        with self.assertRaisesRegex(verify.VerificationError, "package ID"):
            verify.package_readme(archive(), "Different", "2.0.0")
        self.assertEqual(verify.package_readme(archive(), "Example", "2.0.0.0+metadata"), b"text\r\n")

    def test_registry_count_and_overrides(self):
        root = Path("references/Sample")
        module = {"packages": {"ids": ["Example", "Tools"], "count": 2,
                               "projectReadmes": ["src/libraries/Example/README.md"]}}
        self.assertEqual(verify.approved_files(module, root),
                         {"Example": root / "src/libraries/Example/README.md", "Tools": root / "README.md"})
        module["packages"]["count"] = 3
        with self.assertRaisesRegex(verify.VerificationError, "count"):
            verify.approved_files(module, root)

    def test_latest_approved_text_and_expected_release(self):
        module = {"name": "Sample", "packages": {"ids": ["Example"], "count": 1, "projectReadmes": []}}
        with tempfile.TemporaryDirectory() as temp, contextlib.redirect_stdout(io.StringIO()) as output:
            root = Path(temp)
            source = root / "README.md"
            source.write_bytes(b"\xef\xbb\xbftext\n")
            with patch.object(verify, "latest_stable", return_value=("2.0.0", leaf("2.0.0")["packageContent"])):
                with patch.object(verify, "download", return_value=archive()):
                    self.assertTrue(verify.verify_module(module, root, "2.0.0"))
                    self.assertFalse(verify.verify_module(module, root, "2.0.1"))
                    source.write_text("different", encoding="utf-8")
                    self.assertFalse(verify.verify_module(module, root, None))
            self.assertIn("matched 1/1", output.getvalue())
            self.assertIn("matched 0/1", output.getvalue())
            self.assertIn("latest stable version differs from expected 2.0.1", output.getvalue())

    def test_reports_http_error_without_url_or_response_body(self):
        url = "https://api.nuget.org/packages/example"
        with patch.object(verify.request, "urlopen", side_effect=HTTPError(url, 404, "body detail", {}, None)):
            with self.assertRaises(verify.VerificationError) as caught:
                verify.download(url, verify.MIB)
            self.assertEqual(str(caught.exception), "NuGet returned HTTP 404")


if __name__ == "__main__":
    unittest.main()
