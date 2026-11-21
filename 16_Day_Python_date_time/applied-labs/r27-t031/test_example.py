import unittest
from datetime import timezone
from example import parse_iso_aware, elapsed_seconds_utc


class TestTimezoneAwareTimestamps(unittest.TestCase):

    def test_fixture_difference_1800_seconds(self):
        """Verify the exact fixture from the task contract differs by 1800s."""
        t1 = "2024-01-01T10:00:00+05:30"
        t2 = "2024-01-01T05:00:00+00:00"
        self.assertEqual(elapsed_seconds_utc(t1, t2), 1800.0)

    def test_fixture_order_independence(self):
        """Verify calculation is symmetric."""
        t1 = "2024-01-01T10:00:00+05:30"
        t2 = "2024-01-01T05:00:00+00:00"
        self.assertEqual(elapsed_seconds_utc(t2, t1), 1800.0)

    def test_reject_naive_timestamp(self):
        """Reject timestamps that lack an explicit offset."""
        with self.assertRaises(ValueError):
            parse_iso_aware("2024-01-01T10:00:00")

    def test_valid_utc_timezone_conversion(self):
        """Ensure converted datetime is timezone-aware and matches UTC."""
        dt = parse_iso_aware("2024-01-01T10:00:00+05:30").astimezone(timezone.utc)
        self.assertEqual(dt.hour, 4)
        self.assertEqual(dt.minute, 30)
        self.assertEqual(dt.tzinfo, timezone.utc)


if __name__ == "__main__":
    unittest.main()