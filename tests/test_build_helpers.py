from __future__ import annotations

import importlib.util
import shutil
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
        skill = next((p.parent.name for p in (REPO_ROOT / 'skills').glob('*/SKILL.md')))
        scratch = REPO_ROOT / '.tmp-test-artifacts'
        scratch.mkdir(exist_ok=True)
        z = scratch / f'{skill}-skill.zip'
        try:
            with zipfile.ZipFile(z, 'w') as zf:
                zf.writestr(f'{REPO_ROOT.name}/skills/{skill}/SKILL.md', 'placeholder')
                zf.writestr(f'{REPO_ROOT.name}/skills/{skill}/agents/claude.yaml', 'name: test')
                zf.writestr(f'{REPO_ROOT.name}/skills/{skill}/agents/openai.yaml', 'name: test')
            ok, detail = mod.verify_zip(z)
        finally:
            z.unlink(missing_ok=True)
            shutil.rmtree(scratch, ignore_errors=True)
        self.assertTrue(ok)
        self.assertEqual(detail, 'valid')


if __name__ == '__main__':
    unittest.main()
