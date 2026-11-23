"""Unit tests for Day 29 Applied Lab (R27-T029): Installable Mini-Package Regression Lab."""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(__file__))
import example  # noqa: E402


class TestInstallableWordcountPackage(unittest.TestCase):
    def test_word_count_function_counts_repeated_words(self) -> None:
        self.assertEqual(example.word_count("a b a"), 3)
        self.assertEqual(example.word_count(""), 0)
        self.assertEqual(example.word_count("  hello   world  "), 2)

    def test_regression_focused_mutant_detection(self) -> None:
        # Passes on the correct implementation ("a b a" -> 3)
        self.assertTrue(example.verify_repeated_word_contract(example.word_count))
        # Fails on the temporary one-line mutant ("a b a" -> len(set(tokens)) == 2 != 3)
        self.assertFalse(
            example.verify_repeated_word_contract(example.word_count_unique_mutant)
        )
        self.assertEqual(example.word_count_unique_mutant("a b a"), 2)

    def test_installed_cli_counts_words_and_help_works_outside_source_dir(self) -> None:
        result = example.install_and_exercise_cli()
        self.assertEqual(result["count_exit_code"], 0)
        self.assertEqual(result["count_stdout"], "3")
        self.assertEqual(result["help_exit_code"], 0)
        self.assertIn("usage: r27-wordcount", str(result["help_stdout"]))


if __name__ == "__main__":
    unittest.main()
