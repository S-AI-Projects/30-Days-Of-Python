"""Unit tests for Day 14 Applied Lab (R27-T022): Function Composition."""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(__file__))
import example  # noqa: E402


class TestFunctionCompositionNormalization(unittest.TestCase):
    def test_contract_normalization(self) -> None:
        self.assertEqual(example.normalize_text("  HELLO   World "), "hello world")

    def test_idempotence_boundary(self) -> None:
        samples = [
            "  HELLO   World ",
            "",
            "   \t\n  ",
            "already normalized",
            "  SINGLE  ",
        ]
        for sample in samples:
            once = example.normalize_text(sample)
            twice = example.normalize_text(once)
            self.assertEqual(twice, once)

    def test_empty_and_whitespace_only_boundaries(self) -> None:
        self.assertEqual(example.normalize_text(""), "")
        self.assertEqual(example.normalize_text("     "), "")
        self.assertEqual(example.normalize_text("\t\n  \r\n"), "")

    def test_invalid_non_string_inputs_raise_type_error(self) -> None:
        for invalid in (None, 123, ["  HELLO "]):
            with self.subTest(invalid=invalid):
                with self.assertRaises(TypeError):
                    example.normalize_text(invalid)  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()
