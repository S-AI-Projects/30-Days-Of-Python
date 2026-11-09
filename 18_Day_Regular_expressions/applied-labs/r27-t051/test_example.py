import unittest
from example import extract_date, validate_date


class TestExtractDate(unittest.TestCase):
    def test_accepted_valid_date(self):
        self.assertEqual(extract_date("2024-02-29"), "2024-02-29")

    def test_rejected_invalid_calendar_date(self):
        with self.assertRaises(ValueError):
            extract_date("2023-02-29")

    def test_no_token_returns_none(self):
        self.assertIsNone(extract_date("text without a token"))

    def test_token_embedded_in_text(self):
        self.assertEqual(
            extract_date("The release date is 2024-02-29."), "2024-02-29"
        )

    def test_validate_date_helper(self):
        validate_date(2024, 2, 29)  # must not raise
        with self.assertRaises(ValueError):
            validate_date(2023, 2, 29)


if __name__ == "__main__":
    unittest.main()
