from __future__ import annotations

import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = REPO_ROOT / 'skills'
TARGETS = {
    'material-design': ['dark theme', 'Storybook snapshots', 'Concrete scenario patterns'],
    'tailwind': ['React or Vue app', 'multiple packages', 'Concrete scenario patterns'],
    'vite': ['webpack or CRA', 'preview parity', 'Concrete scenario patterns'],
}


class TestSkillContentQuality(unittest.TestCase):
    def test_all_skills_have_two_common_request_examples(self):
        for skill_md in sorted(SKILLS_ROOT.glob('*/SKILL.md')):
            text = skill_md.read_text(encoding='utf-8')
            m = re.search(r'## Common Requests\n(.*?)(?:\n## |\Z)', text, re.S)
            with self.subTest(skill=skill_md.parent.name):
                self.assertIsNotNone(m)
                examples = re.findall(r'```text\n(.*?)```', m.group(1), re.S)
                self.assertGreaterEqual(len(examples), 2)

    def test_round3_targets_have_concrete_improvements(self):
        for skill_name, needles in TARGETS.items():
            skill_text = (SKILLS_ROOT / skill_name / 'SKILL.md').read_text(encoding='utf-8')
            workflow_text = (SKILLS_ROOT / skill_name / 'references' / 'workflows.md').read_text(encoding='utf-8')
            merged = skill_text + '\n' + workflow_text
            for needle in needles:
                with self.subTest(skill=skill_name, needle=needle):
                    self.assertIn(needle, merged)


if __name__ == '__main__':
    unittest.main()
