import unittest
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
REPO_NAME = REPO_ROOT.name
SKILLS_ROOT = REPO_ROOT / 'skills'
REQUIRED = ['SKILL.md', 'agents/claude.yaml', 'agents/openai.yaml']
def discover(): return sorted(p.parent for p in SKILLS_ROOT.glob('*/SKILL.md'))
class TestSourceLayout(unittest.TestCase):
    def test_skills_exist(self): self.assertGreater(len(discover()), 0)
    def test_required_files(self):
        for skill in discover():
            for rel in REQUIRED:
                with self.subTest(skill=skill.name, rel=rel):
                    self.assertTrue((skill / rel).exists())
class TestBuiltZips(unittest.TestCase):
    def setUp(self):
        build_dir = REPO_ROOT / 'built'
        self.zips = sorted(build_dir.glob('*-skill.zip')) if build_dir.exists() else []
    def test_required_files_in_zips(self):
        if not self.zips:
            self.skipTest('built/ directory is empty — run make build first')
        for z in self.zips:
            skill_name = z.stem.replace('-skill', '')
            with zipfile.ZipFile(z, 'r') as zf:
                names = {name.replace("\\", "/") for name in zf.namelist()}
            for rel in REQUIRED:
                self.assertIn(f'{REPO_NAME}/skills/{skill_name}/{rel}', names)
if __name__ == '__main__':
    unittest.main()
