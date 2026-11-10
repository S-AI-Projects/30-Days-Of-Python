import os
import subprocess
import sys
import unittest

from example import explain_text_statistics, text_statistics


class TestTextStatistics(unittest.TestCase):
    def test_fixture_one_two_two(self):
        result = text_statistics("one two two")
        self.assertEqual(result["total_words"], 3)
        self.assertEqual(result["distinct_words"], 2)

    def test_worked_explanation_pipeline(self):
        explanation = explain_text_statistics("one two two")
        self.assertEqual(explanation["input"], "one two two")
        self.assertEqual(
            explanation["intermediate"]["tokens"], ["one", "two", "two"]
        )
        self.assertEqual(
            explanation["intermediate"]["unique_tokens"], ["one", "two"]
        )
        self.assertEqual(
            explanation["output"]["total_words"], 3
        )
        self.assertEqual(
            explanation["output"]["distinct_words"], 2
        )

    def test_empty_string(self):
        result = text_statistics("")
        self.assertEqual(result["total_words"], 0)
        self.assertEqual(result["distinct_words"], 0)

    def test_invalid_type_rejected(self):
        with self.assertRaises(TypeError):
            text_statistics(None)

    def test_import_succeeds_without_user_site(self):
        lab_dir = os.path.dirname(os.path.abspath(__file__))
        cmd = [
            sys.executable,
            "-s",  # disables user-site packages
            "-c",
            "import example; res = example.text_statistics('one two two'); assert res['total_words'] == 3 and res['distinct_words'] == 2",
        ]
        proc = subprocess.run(cmd, cwd=lab_dir, capture_output=True, text=True)
        self.assertEqual(
            proc.returncode, 0, f"Subprocess failed: {proc.stderr}"
        )


if __name__ == "__main__":
    unittest.main()
