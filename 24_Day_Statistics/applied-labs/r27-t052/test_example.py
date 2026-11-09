import unittest
from example import missing_value_summary


class TestMissingValueSummary(unittest.TestCase):
    def test_standard_observations_with_none(self):
        result = missing_value_summary([1, None, 3, 5])
        self.assertEqual(
            result,
            {"count": 3, "missing_count": 1, "mean": 3, "median": 3},
        )

    def test_all_missing_boundary(self):
        result = missing_value_summary([None, None, None])
        self.assertEqual(
            result,
            {"count": 0, "missing_count": 3, "mean": None, "median": None},
        )

    def test_empty_input_boundary(self):
        result = missing_value_summary([])
        self.assertEqual(
            result,
            {"count": 0, "missing_count": 0, "mean": None, "median": None},
        )

    def test_even_count_median(self):
        result = missing_value_summary([1, None, 2, 3, 4])
        self.assertEqual(result["count"], 4)
        self.assertEqual(result["missing_count"], 1)
        self.assertEqual(result["mean"], 2.5)
        self.assertEqual(result["median"], 2.5)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            missing_value_summary(None)
        with self.assertRaises(TypeError):
            missing_value_summary(123)

    def test_invalid_element_type(self):
        with self.assertRaises(TypeError):
            missing_value_summary([1, "invalid", 3])


if __name__ == "__main__":
    unittest.main()

