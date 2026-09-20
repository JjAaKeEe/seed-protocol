from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools" / "seed.py"
SPEC = importlib.util.spec_from_file_location("seed_tool", MODULE_PATH)
assert SPEC and SPEC.loader
seed_tool = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = seed_tool
SPEC.loader.exec_module(seed_tool)


class SeedProtocolTests(unittest.TestCase):
    def test_golden_seed_validates(self) -> None:
        report = seed_tool.validate_seed(ROOT)
        self.assertTrue(report.valid, report.errors)
        self.assertEqual(report.manifest["id"], "seed:S-0000")

    def test_boot_packet_routes_core_context(self) -> None:
        manifest = seed_tool.load_manifest(ROOT)
        packet = seed_tool.render_boot_packet(ROOT, manifest)
        self.assertIn("# Bootstrap", packet)
        self.assertIn("# Principles", packet)
        self.assertIn("# Current status", packet)
        self.assertIn("# Model boundary", packet)
        self.assertIn("# Authority", packet)
        self.assertNotIn("# Canonical entry", packet)

    def test_full_boot_packet_includes_canon(self) -> None:
        manifest = seed_tool.load_manifest(ROOT)
        packet = seed_tool.render_boot_packet(ROOT, manifest, full=True)
        self.assertIn("# Canonical entry", packet)
        self.assertIn("The Golden Seed", packet)

    def test_minimal_template_initializes_and_validates(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "example-seed"
            seed_tool.init_seed(target, "seed:example", "Example Seed")
            report = seed_tool.validate_seed(target)
            self.assertTrue(report.valid, report.errors)
            self.assertEqual(report.manifest["title"], "Example Seed")
            self.assertNotIn("{{TITLE}}", (target / "README.md").read_text())

    def test_missing_required_file_is_an_error(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "example-seed"
            seed_tool.init_seed(target, "seed:example", "Example Seed")
            (target / "BOOTSTRAP.md").unlink()
            report = seed_tool.validate_seed(target)
            self.assertFalse(report.valid)
            self.assertTrue(
                any("BOOTSTRAP.md" in error for error in report.errors),
                report.errors,
            )

    def test_escaping_entry_path_is_an_error(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "example-seed"
            seed_tool.init_seed(target, "seed:example", "Example Seed")
            manifest_path = target / "SEED.yaml"
            manifest = json.loads(manifest_path.read_text())
            manifest["canonical_entry"] = "../outside.md"
            manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
            report = seed_tool.validate_seed(target)
            self.assertFalse(report.valid)
            self.assertTrue(any("escapes" in error for error in report.errors))

    def test_snapshot_contains_seed_root(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "seed.zip"
            manifest = seed_tool.load_manifest(ROOT)
            result = seed_tool.snapshot_seed(ROOT, manifest, output)
            self.assertEqual(result, output.resolve())
            with zipfile.ZipFile(output) as archive:
                names = set(archive.namelist())
            self.assertIn(f"{ROOT.name}/SEED.yaml", names)
            self.assertIn(f"{ROOT.name}/BOOTSTRAP.md", names)
            self.assertFalse(any("__pycache__" in name for name in names))


if __name__ == "__main__":
    unittest.main()
