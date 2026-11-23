"""Unit tests for Day 5 Applied Lab (R27-T025): Ordered Deduplication."""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(__file__))
import example  # noqa: E402


class TestOrderedDeduplication(unittest.TestCase):
    def test_contract_deduplication_preserves_order_and_input(self) -> None:
        original = [3, 1, 3, 2, 1]
        result = example.deduplicate_ordered(original)
        self.assertEqual(result, [3, 1, 2])
        self.assertEqual(original, [3, 1, 3, 2, 1])
        self.assertIsNot(result, original)

    def test_empty_list_boundary(self) -> None:
        empty: list[int] = []
        result = example.deduplicate_ordered(empty)
        self.assertEqual(result, [])
        self.assertEqual(empty, [])

    def test_two_isolated_runs_with_injected_clock_and_sink_agree(self) -> None:
        for fixture_name in example.REPEATABLE_FIXTURES:
            with self.subTest(fixture=fixture_name):
                run_a = example.run_isolated_fixture(fixture_name)
                run_b = example.run_isolated_fixture(fixture_name)
                self.assertEqual(run_a, run_b)
                self.assertEqual(run_a["input_before"], run_a["input_after"])


if __name__ == "__main__":
    unittest.main()
