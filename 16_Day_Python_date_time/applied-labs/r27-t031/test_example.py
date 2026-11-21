import unittest
from datetime import timezone

try:
    from .example import parse_iso_offset, elapsed_seconds_utc
except (ImportError, ValueError):
    from example import parse_iso_offset, elapsed_seconds_utc

class TestTimezoneAwareTimestamps(unittest.TestCase):
    def test_fixture_difference_1800_seconds(self):
        t1 = "2024-01-01T10:00:00+05:30"
        t2 = "2024-01-01T05:00:00+00:00"
        diff = elapsed_seconds_utc(t1, t2)
        self.assertEqual(diff, 1800.0)

    def test_reject_naive_timestamp(self):
        naive_ts = "2024-01-01T10:00:00"
        with self.assertRaises(ValueError):
            parse_iso_offset(naive_ts)

    def test_utc_normalization_equality(self):
        t1 = "2024-01-01T12:00:00+02:00"
        t2 = "2024-01-01T10:00:00+00:00"
        self.assertEqual(elapsed_seconds_utc(t1, t2), 0.0)

    def test_timezone_preservation(self):
        dt = parse_iso_offset("2024-01-01T10:00:00+05:30")
        self.assertIsNotNone(dt.tzinfo)

if __name__ == "__main__":
    unittest.main()
