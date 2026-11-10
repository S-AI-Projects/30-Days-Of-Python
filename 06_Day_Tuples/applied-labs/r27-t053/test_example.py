import unittest
from example import (
    EXPECTED_TABLE,
    reference_translate_points,
    translate_points,
)


class TestTranslatePoints(unittest.TestCase):
    def test_fixture_translation(self):
        points = ((1, 2), (3, 4))
        shift = (2, -1)
        expected = ((3, 1), (5, 3))
        self.assertEqual(translate_points(points, shift), expected)

    def test_input_remains_unchanged(self):
        original = ((1, 2), (3, 4))
        snapshot = original
        result = translate_points(original, (2, -1))
        # Ensure original value has not changed
        self.assertEqual(original, ((1, 2), (3, 4)))
        self.assertIs(original, snapshot)
        self.assertIsNot(result, original)

    def test_compare_against_expected_table(self):
        for entry in EXPECTED_TABLE:
            pts = entry["points"]
            shift = entry["shift"]
            expected = entry["expected"]
            self.assertEqual(translate_points(pts, shift), expected)

    def test_compare_against_reference_implementation(self):
        for entry in EXPECTED_TABLE:
            pts = entry["points"]
            shift = entry["shift"]
            actual = translate_points(pts, shift)
            reference = reference_translate_points(pts, shift)
            self.assertEqual(actual, reference)

    def test_empty_points(self):
        self.assertEqual(translate_points((), (10, -5)), ())


if __name__ == "__main__":
    unittest.main()

