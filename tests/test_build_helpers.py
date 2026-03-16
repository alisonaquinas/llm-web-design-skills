from __future__ import annotations

import importlib.util
import unittest
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def load(rel_path: str):
    path = REPO_ROOT / rel_path
    spec = importlib.util.spec_from_file_location(path.stem.replace('-', '_'), path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


class TestBuildHelpers(unittest.TestCase):
    def test_parse_version(self):
        mod = load('scripts/check_node_version.py')
        self.assertEqual(mod.parse_version('v20.11.1\n'), (20, 11, 1))
        self.assertIsNone(mod.parse_version('unknown'))

    def test_verify_zip(self):
        mod = load('scripts/verify_built_zips.py')
        scratch = REPO_ROOT / '.tmp-test-artifacts'
        scratch.mkdir(exist_ok=True)
        z = scratch / 'sample.zip'
        try:
            with zipfile.ZipFile(z, 'w') as zf:
                zf.writestr('hello.txt', 'hello')
            ok, detail = mod.verify_zip(z)
        finally:
            z.unlink(missing_ok=True)
            scratch.rmdir()
        self.assertTrue(ok)
        self.assertEqual(detail, 'valid')


if __name__ == '__main__':
    unittest.main()
