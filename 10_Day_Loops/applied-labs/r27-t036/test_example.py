import unittest

try:
    from .example import extract_run, run_length_encode
except (ImportError, ValueError):
    from example import extract_run, run_length_encode

class TestRunLengthEncoding(unittest.TestCase):
    def test_fixture_multiple_runs(self):
        self.assertEqual(run_length_encode("aaabbc"), [("a", 3), ("b", 2), ("c", 1)])

    def test_fixture_empty_string(self):
        self.assertEqual(run_length_encode(""), [])

    def test_fixture_single_run(self):
        self.assertEqual(run_length_encode("aaa"), [("a", 3)])

    def test_extracted_run_responsibility(self):
        symbol, count, next_idx = extract_run("aaabbc", 0)
        self.assertEqual(symbol, "a")
        self.assertEqual(count, 3)
        self.assertEqual(next_idx, 3)

if __name__ == "__main__":
    unittest.main()
