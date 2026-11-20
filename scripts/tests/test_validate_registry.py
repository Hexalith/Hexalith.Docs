import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from validate_registry import ROOT, validate


class RegistryTests(unittest.TestCase):
    def setUp(self):
        self.registry = json.loads((ROOT / "docs/module-registry.json").read_text())
        self.commons = next(r for r in self.registry["modules"] if r["name"] == "Hexalith.Commons")

    def test_workspace_inventory_validates_offline(self):
        self.assertEqual(validate(self.registry, ROOT), [])

    def test_replacing_a_required_module_with_a_duplicate_fails(self):
        rows = self.registry["modules"]
        rows[0] = rows[1]
        problems = validate(self.registry, ROOT)
        self.assertTrue(any("duplicate module" in p for p in problems))
        self.assertTrue(any("missing registry entry" in p for p in problems))

    def test_readme_from_another_package_cannot_be_selected(self):
        self.commons["packages"]["projectReadmes"] = ["src/Other.Package/README.md"]
        self.assertTrue(any("README paths" in p for p in validate(self.registry, ROOT)))

    def test_inconsistent_package_count_fails(self):
        self.commons["packages"]["count"] += 1
        self.assertTrue(any("package count" in p for p in validate(self.registry, ROOT)))

    def test_registry_rejects_a_source_outside_the_checkout(self):
        self.commons["packages"]["inventorySource"] = "../another-module"
        self.assertTrue(any("inventory needs" in p for p in validate(self.registry, ROOT)))

    def test_invalid_block_type_is_reported(self):
        self.commons["quickstarts"] = 1
        self.assertTrue(any("quickstart block" in p for p in validate(self.registry, ROOT)))


if __name__ == "__main__":
    unittest.main()
