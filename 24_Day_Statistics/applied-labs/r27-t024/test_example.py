"""Unit tests for Day 24 Applied Lab (R27-T024): Missing-Value Summary State/Invariant Lab."""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(__file__))
import example  # noqa: E402


class TestMissingValueSummary(unittest.TestCase):
    def test_contract_fixture(self) -> None:
        result = example.summarize_observations([1, None, 3, 5])
        self.assertEqual(
            result,
            {
                "count": 3,
                "missing_count": 1,
                "mean": 3,
                "median": 3,
            },
        )
        self.assertTrue(example.check_summary_invariants([1, None, 3, 5], result))

    def test_all_missing_and_empty_yield_null_mean_and_median(self) -> None:
        all_missing = example.summarize_observations([None, None])
        self.assertEqual(
            all_missing,
            {
                "count": 0,
                "missing_count": 2,
                "mean": None,
                "median": None,
            },
        )
        self.assertTrue(example.check_summary_invariants([None, None], all_missing))

        empty = example.summarize_observations([])
        self.assertEqual(
            empty,
            {
                "count": 0,
                "missing_count": 0,
                "mean": None,
                "median": None,
            },
        )
        self.assertTrue(example.check_summary_invariants([], empty))

    def test_state_invariants_across_sequence_of_operations(self) -> None:
        tracker = example.ObservationTracker()
        s0 = tracker.summary()
        self.assertEqual(s0, {"count": 0, "missing_count": 0, "mean": None, "median": None})

        s1 = tracker.add(1)
        self.assertEqual(s1, {"count": 1, "missing_count": 0, "mean": 1, "median": 1})

        # Appending None increments missing_count while preserving count, mean, and median
        s2 = tracker.add(None)
        self.assertEqual(s2["count"], s1["count"])
        self.assertEqual(s2["missing_count"], s1["missing_count"] + 1)
        self.assertEqual(s2["mean"], s1["mean"])
        self.assertEqual(s2["median"], s1["median"])

        s3 = tracker.add(3)
        self.assertEqual(s3, {"count": 2, "missing_count": 1, "mean": 2, "median": 2})

        s4 = tracker.add(5)
        self.assertEqual(s4, {"count": 3, "missing_count": 1, "mean": 3, "median": 3})
        self.assertTrue(example.check_summary_invariants(tracker.observations, s4))


if __name__ == "__main__":
    unittest.main()
