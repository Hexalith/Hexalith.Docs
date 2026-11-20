#!/usr/bin/env python3
"""Compare the pilots' approved README files with their latest listed stable NuGet packages."""

import argparse
import gzip
import io
from http.client import HTTPException
import json
from pathlib import Path
import re
import sys
from urllib import error, parse, request
from xml.etree import ElementTree
from zipfile import BadZipFile, ZipFile

ROOT = Path(__file__).resolve().parents[1]
PILOTS = ("Hexalith.Commons", "Hexalith.PolymorphicSerializations")
NUGET = "https://api.nuget.org/v3/registration5-gz-semver2"
STABLE = re.compile(r"[0-9]+(?:\.[0-9]+){1,3}(?:\+[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*)?")
MIB = 1024 * 1024


class VerificationError(Exception):
    """A diagnostic that can be printed without exposing package contents or credentials."""


def read_limited(stream, limit):
    data = stream.read(limit + 1)
    if len(data) > limit:
        raise VerificationError("resource exceeds size limit")
    return data


def download(url, limit):
    parts = parse.urlsplit(url)
    if parts.scheme != "https" or parts.netloc != "api.nuget.org":
        raise VerificationError("unexpected NuGet resource location")
    try:
        with request.urlopen(url, timeout=20) as response:
            if response.headers.get("Content-Encoding", "").lower() == "gzip":
                with gzip.GzipFile(fileobj=response) as stream:
                    return read_limited(stream, limit)
            return read_limited(response, limit)
    except error.HTTPError as exc:
        raise VerificationError(f"NuGet returned HTTP {exc.code}") from exc
    except (OSError, EOFError, HTTPException) as exc:
        raise VerificationError("NuGet download failed or timed out") from exc


def version_key(version):
    if not isinstance(version, str) or not STABLE.fullmatch(version):
        return None
    # NuGet ignores build metadata and zero-pads numeric components for comparison.
    parts = [int(part) for part in version.split("+", 1)[0].split(".")]
    return parts + [0] * (4 - len(parts))


def latest_stable(package_id):
    index = json.loads(download(f"{NUGET}/{package_id.lower()}/index.json", 8 * MIB))
    # NuGet registration pages are version-ordered. A newer page can be entirely
    # prerelease or unlisted, so keep walking until a listed stable version exists.
    for page in reversed(index["items"]):
        leaves = page.get("items")
        if leaves is None:
            leaves = json.loads(download(page["@id"], 8 * MIB))["items"]
        for leaf in reversed(leaves):
            entry = leaf["catalogEntry"]
            version = entry["version"]
            if entry["id"].casefold() != package_id.casefold():
                raise VerificationError("registration package ID mismatch")
            if entry["listed"] is True and STABLE.fullmatch(version):
                return version, leaf["packageContent"]
    raise VerificationError("no listed stable version (prereleases excluded)")


def package_readme(payload, package_id, version):
    with ZipFile(io.BytesIO(payload)) as archive:
        specs = [name for name in archive.namelist() if "/" not in name and name.lower().endswith(".nuspec")]
        if len(specs) != 1:
            raise VerificationError("expected a single root .nuspec")
        with archive.open(specs[0]) as stream:
            spec = ElementTree.fromstring(read_limited(stream, MIB))
        metadata = spec.find("{*}metadata")
        if metadata is None or metadata.findtext("{*}id", "").casefold() != package_id.casefold():
            raise VerificationError("package ID differs from registration")
        if version_key(metadata.findtext("{*}version")) != version_key(version):
            raise VerificationError("package version differs from registration")
        member = metadata.findtext("{*}readme", "").strip().replace("\\", "/").lstrip("/")
        if not member:
            raise VerificationError("package .nuspec has no README declaration")
        if archive.namelist().count(member) != 1:
            raise VerificationError("missing or ambiguous .nuspec README target")
        with archive.open(member) as stream:
            return read_limited(stream, 4 * MIB)


def normalize(content):
    return content.decode("utf-8-sig").replace("\r\n", "\n")


def approved_files(module, root):
    packages = module["packages"]
    ids = packages["ids"]
    if not isinstance(ids, list) or any(not isinstance(pid, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*", pid) for pid in ids):
        raise VerificationError("invalid registry package IDs")
    if not ids or len(ids) != packages["count"] or len({pid.casefold() for pid in ids}) != len(ids):
        raise VerificationError("registry package count or uniqueness mismatch")
    overrides = {}
    for name in packages["projectReadmes"]:
        path = Path(name)
        if path.is_absolute() or ".." in path.parts or path.name != "README.md":
            raise VerificationError("invalid README path in registry")
        pkg = path.parent.name
        if pkg not in ids or pkg in overrides:
            raise VerificationError("invalid per-package README mapping in registry")
        overrides[pkg] = path
    return {pid: root / overrides.get(pid, Path("README.md")) for pid in ids}


def verify_module(module, root, expected_version):
    files = approved_files(module, root)
    matched = 0
    for package_id, source in files.items():
        label = package_id
        try:
            if not source.is_file():
                raise VerificationError("expected README missing from checkout")
            version, url = latest_stable(package_id)
            label += f" {version}"
            if expected_version and version_key(expected_version) != version_key(version):
                raise VerificationError(f"latest stable version differs from expected {expected_version}")
            published = package_readme(download(url, 64 * MIB), package_id, version)
            if normalize(published) != normalize(source.read_bytes()):
                raise VerificationError(f"README differs from {source.relative_to(root).as_posix()}")
        except VerificationError as exc:
            print(f"FAIL {label}  {exc}")
        except (OSError, EOFError, BadZipFile, ElementTree.ParseError, ValueError, KeyError, TypeError) as exc:
            print(f"FAIL {label}  unreadable package, source or metadata ({type(exc).__name__})")
        else:
            print(f"PASS {label}")
            matched += 1
    print(f"{module['name']} matched {matched}/{len(files)} registered packages")
    return matched == len(files)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--module", choices=PILOTS, help="check one pilot (default: both)")
    parser.add_argument("--version", help="require this stable release version for the selected module")
    args = parser.parse_args(argv)
    if args.version is not None and (not args.module or not STABLE.fullmatch(args.version)):
        parser.error("--version requires --module and a stable numeric NuGet version")

    selected = (args.module,) if args.module else PILOTS
    try:
        registry = json.loads((ROOT / "docs/module-registry.json").read_text(encoding="utf-8"))
        passed = True
        for name in selected:
            matches = [row for row in registry["modules"] if row["name"] == name]
            if len(matches) != 1:
                raise VerificationError(f"expected one registry row for {name}")
            if not verify_module(matches[0], ROOT / "references" / name, args.version):
                passed = False
    except VerificationError as exc:
        print(f"FAIL {exc}", file=sys.stderr)
        return 1
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"FAIL unreadable module registry ({type(exc).__name__})", file=sys.stderr)
        return 1
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
