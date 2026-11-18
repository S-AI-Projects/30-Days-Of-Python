import unittest
from example import apply_changes


class TestApplyChanges(unittest.TestCase):
    def test_main_example(self):
        result = apply_changes({"tea": 3}, {"tea": -2, "coffee": 4})
        self.assertEqual(result, {"tea": 1, "coffee": 4})

    def test_negative_raises(self):
        with self.assertRaises(ValueError):
            apply_changes({"tea": 3}, {"tea": -4})

    def test_original_unchanged(self):
        original = {"tea": 3}
        with self.assertRaises(ValueError):
            apply_changes(original, {"tea": -4})
        self.assertEqual(original, {"tea": 3})

    def test_exactly_zero_is_allowed(self):
        # Boundary test: catches the mutant "< 0" -> "<= 0"
        self.assertEqual(apply_changes({"tea": 2}, {"tea": -2}), {"tea": 0})


if __name__ == "__main__":
    unittest.main()
    