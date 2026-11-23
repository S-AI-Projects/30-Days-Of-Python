"""Unit tests for Day 7 Applied Lab (R27-T023): Enrolment Sets Reference Comparison."""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(__file__))
import example  # noqa: E402


class TestEnrolmentSetsComparison(unittest.TestCase):
    def test_contract_fixture(self) -> None:
        group_a = {"Ana", "Bo"}
        group_b = {"Bo", "Cy"}
        result = example.compare_enrolments(group_a, group_b)
        self.assertEqual(result["intersection"], {"Bo"})
        self.assertEqual(result["first_only"], {"Ana"})
        self.assertEqual(result["first-only"], {"Ana"})
        self.assertEqual(result["union"], {"Ana", "Bo", "Cy"})

    def test_matches_independent_reference_implementation(self) -> None:
        group_a = {"Ana", "Bo"}
        group_b = {"Bo", "Cy"}
        actual = example.compare_enrolments(group_a, group_b)
        reference = example.reference_compare_enrolments(group_a, group_b)
        self.assertEqual(actual, reference)

    def test_all_expected_result_table_cases_match(self) -> None:
        comparisons = example.verify_against_reference_table()
        self.assertGreaterEqual(len(comparisons), 4)
        for entry in comparisons:
            with self.subTest(case=entry["case"]):
                self.assertTrue(entry["matches_reference"])
                self.assertTrue(entry["matches_table"])
                self.assertEqual(entry["actual"], entry["expected"])


if __name__ == "__main__":
    unittest.main()
