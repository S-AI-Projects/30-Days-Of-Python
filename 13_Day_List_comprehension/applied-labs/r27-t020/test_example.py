import unittest

from example import even_squares


class EvenSquaresTests(unittest.TestCase):
    def test_even_values_are_squared_and_odd_values_are_excluded(self):
        numbers = [-2, -1, 0, 1, 2]

        self.assertEqual(even_squares(numbers), {-2: 4, 0: 0, 2: 4})

    def test_odd_only_input_returns_empty_mapping(self):
        self.assertEqual(even_squares([-3, -1, 1, 3]), {})

    def test_input_is_not_modified(self):
        numbers = [-2, -1, 0, 1, 2]
        original = numbers.copy()

        even_squares(numbers)

        self.assertEqual(numbers, original)


if __name__ == "__main__":
    unittest.main()
