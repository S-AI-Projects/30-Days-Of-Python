import unittest
from example import elapsed_seconds, elapsed_many


def make_pairs(n):
    """n pairs; pair i differs by 1800 + 60 * (i % 60) seconds."""
    pairs = []
    expected = []
    for i in range(n):
        start = "2024-01-01T10:00:00+05:30"  # = 04:30:00 UTC
        end = f"2024-01-01T05:{i % 60:02d}:00+00:00"
        pairs.append((start, end))
        expected.append(1800 + 60 * (i % 60))
    return pairs, expected


class TestElapsedSeconds(unittest.TestCase):
    def test_main_example(self):
        result = elapsed_seconds("2024-01-01T10:00:00+05:30", "2024-01-01T05:00:00+00:00")
        self.assertEqual(result, 1800)

    def test_reverse_order_is_negative(self):
        result = elapsed_seconds("2024-01-01T05:00:00+00:00", "2024-01-01T10:00:00+05:30")
        self.assertEqual(result, -1800)

    def test_missing_offset_in_start_is_rejected(self):
        with self.assertRaises(ValueError):
            elapsed_seconds("2024-01-01T10:00:00", "2024-01-01T05:00:00+00:00")

    def test_missing_offset_in_end_is_rejected(self):
        with self.assertRaises(ValueError):
            elapsed_seconds("2024-01-01T10:00:00+05:30", "2024-01-01T05:00:00")

    def test_date_only_is_rejected(self):
        with self.assertRaises(ValueError):
            elapsed_seconds("2024-01-01", "2024-01-01T05:00:00+00:00")

    def test_garbage_text_is_rejected(self):
        with self.assertRaises(ValueError):
            elapsed_seconds("not a timestamp", "2024-01-01T05:00:00+00:00")


class TestInputSizes(unittest.TestCase):
    """Three bounded input sizes. We assert correctness and report the
    number of parse operations. There is no speed threshold."""

    def check_size(self, n):
        pairs, expected = make_pairs(n)
        results, parse_calls = elapsed_many(pairs)
        self.assertEqual(results, expected)  # correctness
        self.assertEqual(parse_calls, 2 * n)  # two parses per pair
        print(f"size={n} pairs, parse_calls={parse_calls}")

    def test_size_1(self):
        self.check_size(1)

    def test_size_10(self):
        self.check_size(10)

    def test_size_100(self):
        self.check_size(100)


if __name__ == "__main__":
    unittest.main()