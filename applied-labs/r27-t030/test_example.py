"""Unit tests for Day 1 Applied Lab (R27-T030): Arithmetic Report Refactoring."""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(__file__))
import example  # noqa: E402


class TestArithmeticReportRefactor(unittest.TestCase):
    def test_contract_seven_and_three(self) -> None:
        self.assertEqual(
            example.arithmetic_report(7, 3),
            {"sum": 10, "difference": 4, "product": 21},
        )

    def test_contract_zero_and_zero(self) -> None:
        self.assertEqual(
            example.arithmetic_report(0, 0),
            {"sum": 0, "difference": 0, "product": 0},
        )

    def test_refactored_version_matches_initial_working_version(self) -> None:
        pairs = [(7, 3), (0, 0), (-5, 4), (12, -12)]
        for a, b in pairs:
            with self.subTest(a=a, b=b):
                self.assertEqual(
                    example.arithmetic_report(a, b),
                    example.arithmetic_report_initial(a, b),
                )

    def test_extracted_responsibility_validate_integer_pair(self) -> None:
        self.assertEqual(example.validate_integer_pair(7, 3), (7, 3))
        for bad_a, bad_b in ((True, 3), (7, "3"), (2.5, 1)):
            with self.subTest(bad_a=bad_a, bad_b=bad_b):
                with self.assertRaises(TypeError):
                    example.validate_integer_pair(bad_a, bad_b)  # type: ignore[arg-type]
                with self.assertRaises(TypeError):
                    example.arithmetic_report(bad_a, bad_b)  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()
