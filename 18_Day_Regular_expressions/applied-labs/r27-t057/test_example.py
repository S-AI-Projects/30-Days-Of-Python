import unittest
from example import (
    explain_date_extraction,
    extract_date,
    validate_date,
)


class TestDateExtraction(unittest.TestCase):
    def test_accepted_valid_date(self):
        self.assertEqual(extract_date("2024-02-29"), "2024-02-29")

    def test_rejected_invalid_calendar_date(self):
        with self.assertRaises(ValueError):
            extract_date("2023-02-29")

    def test_no_token_returns_none(self):
        self.assertIsNone(extract_date("text without a token"))

    def test_token_embedded_in_text(self):
        self.assertEqual(
            extract_date("Report generated on 2024-02-29."), "2024-02-29"
        )

    def test_worked_explanation_pipeline(self):
        explanation = explain_date_extraction("Scheduled for 2024-02-29.")
        self.assertEqual(explanation["input"], "Scheduled for 2024-02-29.")
        self.assertTrue(explanation["intermediate"]["matched"])
        self.assertEqual(explanation["intermediate"]["token"], "2024-02-29")
        self.assertEqual(
            explanation["intermediate"]["groups"],
            {"year": "2024", "month": "02", "day": "29"},
        )
        self.assertEqual(
            explanation["intermediate"]["parsed_ints"],
            {"year": 2024, "month": 2, "day": 29},
        )
        self.assertTrue(explanation["intermediate"]["calendar_valid"])
        self.assertEqual(explanation["output"], "2024-02-29")

    def test_worked_explanation_invalid_calendar(self):
        explanation = explain_date_extraction("Scheduled for 2023-02-29.")
        self.assertTrue(explanation["intermediate"]["matched"])
        self.assertFalse(explanation["intermediate"]["calendar_valid"])
        self.assertEqual(explanation["output"], "ValueError")

    def test_worked_explanation_no_token(self):
        explanation = explain_date_extraction("No date present")
        self.assertFalse(explanation["intermediate"]["matched"])
        self.assertIsNone(explanation["output"])

    def test_validate_date_helper(self):
        validate_date(2024, 2, 29)
        with self.assertRaises(ValueError):
            validate_date(2023, 2, 29)


if __name__ == "__main__":
    unittest.main()
