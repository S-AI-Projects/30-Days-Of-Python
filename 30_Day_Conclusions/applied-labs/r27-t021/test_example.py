"""Unit tests for Day 30 Capstone Applied Lab (R27-T021)."""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(__file__))
import example  # noqa: E402


class TestExpenseSummarizer(unittest.TestCase):
    def test_contract_fixture_totals(self) -> None:
        fixture = "food,12.50\nfood,7.50\ntravel,5.00"
        result = example.summarize_expenses(fixture)
        self.assertEqual(
            result["formatted_totals"],
            {"food": "20.00", "travel": "5.00"},
        )
        self.assertEqual(result["totals"], {"food": 20.0, "travel": 5.0})
        self.assertEqual(result["summary"], "food=20.00, travel=5.00")
        self.assertEqual(result["errors"], [])

    def test_negative_expenses_reported_by_line(self) -> None:
        fixture = [
            "food,12.50",
            "food,-4.00",
            "food,7.50",
            "travel,5.00",
            "travel,-1.25",
        ]
        result = example.summarize_expenses(fixture)
        self.assertEqual(
            result["formatted_totals"],
            {"food": "20.00", "travel": "5.00"},
        )
        self.assertEqual(result["error_lines"], [2, 5])
        self.assertIn("Line 2", result["errors"][0]["reason"])
        self.assertIn("negative", result["errors"][0]["reason"])
        self.assertIn("Line 5", result["errors"][1]["reason"])

    def test_malformed_and_zero_expense_handling(self) -> None:
        fixture = "food,0.00\ninvalid_line\nbooks,abc"
        result = example.summarize_expenses(fixture)
        self.assertEqual(result["formatted_totals"], {"food": "0.00"})
        self.assertEqual(result["error_lines"], [2, 3])

    def test_run_demo_executes_contract(self) -> None:
        clean_result, mixed_result = example.run_demo()
        self.assertEqual(clean_result["summary"], "food=20.00, travel=5.00")
        self.assertEqual(mixed_result["error_lines"], [2, 5])


if __name__ == "__main__":
    unittest.main()
