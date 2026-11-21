import io
import sys
import unittest
from unittest.mock import patch

try:
    from .example import cli, count_words
except (ImportError, ValueError):
    from example import cli, count_words

class TestWordCountPackage(unittest.TestCase):
    def test_fixture_word_count(self):
        self.assertEqual(count_words("a b a"), 3)

    def test_cli_execution_fixture(self):
        captured = io.StringIO()
        with patch("sys.stdout", captured):
            exit_code = cli(["a", "b", "a"])
        self.assertEqual(exit_code, 0)
        self.assertEqual(captured.getvalue().strip(), "3")

    def test_deterministic_isolated_runs(self):
        fixture = "The quick brown fox jumps over the lazy dog"
        run1 = count_words(fixture)
        run2 = count_words(fixture)
        self.assertEqual(run1, run2)
        self.assertEqual(run1, 9)

    def test_injected_storage_fixture(self):
        mock_storage = {"storage://file.txt": "a b a"}
        result = count_words("storage://file.txt", storage_reader=lambda uri: mock_storage[uri])
        self.assertEqual(result, 3)

if __name__ == "__main__":
    unittest.main()
