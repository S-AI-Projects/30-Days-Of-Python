import subprocess
import sys
import unittest
from pathlib import Path

from example import EXAMPLES, normalize


class NormalizationPipelineTests(unittest.TestCase):
    def test_every_fixture_result(self):
        for value, expected in EXAMPLES:
            with self.subTest(value=value):
                self.assertEqual(normalize(value), expected)

    def test_normalization_is_idempotent_for_every_fixture(self):
        for value, expected in EXAMPLES:
            with self.subTest(value=value):
                self.assertEqual(normalize(normalize(value)), expected)

    def test_published_example_runs_in_a_fresh_process(self):
        example_path = Path(__file__).with_name("example.py")
        result = subprocess.run(
            [sys.executable, str(example_path)],
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("After strip: 'HELLO   World'", result.stdout)
        self.assertIn("After lowercase: 'hello   world'", result.stdout)
        self.assertIn("After whitespace collapse: 'hello world'", result.stdout)
        self.assertIn("Normalized again: 'hello world'", result.stdout)


if __name__ == "__main__":
    unittest.main()
