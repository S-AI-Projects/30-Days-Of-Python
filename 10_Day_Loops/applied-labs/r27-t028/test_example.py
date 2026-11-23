"""Unit tests for Day 10 Applied Lab (R27-T028): Run-Length Encoding Input-Scale Experiment."""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(__file__))
import example  # noqa: E402


class TestRunLengthEncoding(unittest.TestCase):
    def test_contract_fixtures(self) -> None:
        self.assertEqual(
            example.run_length_encode("aaabbc"),
            [("a", 3), ("b", 2), ("c", 1)],
        )
        self.assertEqual(example.run_length_encode(""), [])
        self.assertEqual(example.run_length_encode("aaa"), [("a", 3)])

    def test_three_bounded_input_sizes_operation_counts(self) -> None:
        experiment = example.run_input_scale_experiment()
        self.assertEqual(len(experiment), 3)

        scale_0, scale_6, scale_60 = experiment

        self.assertEqual(scale_0["encoded"], [])
        self.assertEqual(
            scale_0["stats"],
            {
                "input_length": 0,
                "symbol_inspections": 0,
                "comparisons": 0,
                "run_emissions": 0,
            },
        )

        self.assertEqual(scale_6["encoded"], [("a", 3), ("b", 2), ("c", 1)])
        self.assertEqual(
            scale_6["stats"],
            {
                "input_length": 6,
                "symbol_inspections": 6,
                "comparisons": 5,
                "run_emissions": 3,
            },
        )

        self.assertEqual(scale_60["encoded"], [("a", 3), ("b", 2), ("c", 1)] * 10)
        self.assertEqual(
            scale_60["stats"],
            {
                "input_length": 60,
                "symbol_inspections": 60,
                "comparisons": 59,
                "run_emissions": 30,
            },
        )

    def test_total_decoded_count_equals_input_length(self) -> None:
        for sample in ("", "aaa", "aaabbc", "xyz", "aabbaa"):
            with self.subTest(sample=sample):
                encoded, stats = example.run_length_encode_with_stats(sample)
                self.assertEqual(sum(count for _, count in encoded), len(sample))
                self.assertEqual(stats["symbol_inspections"], len(sample))


if __name__ == "__main__":
    unittest.main()
