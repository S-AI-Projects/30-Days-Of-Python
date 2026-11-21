import unittest

try:
    from .example import even_squares_mapping, instrumented_even_squares
except (ImportError, ValueError):
    from example import even_squares_mapping, instrumented_even_squares

class TestFilteredComprehension(unittest.TestCase):
    def test_fixture_mixed_integers(self):
        input_data = [-2, -1, 0, 1, 2]
        original_copy = list(input_data)
        result = even_squares_mapping(input_data)
        self.assertEqual(result, {-2: 4, 0: 0, 2: 4})
        self.assertEqual(input_data, original_copy)

    def test_fixture_odd_only(self):
        input_data = [1, 3, 5, 7, -9]
        self.assertEqual(even_squares_mapping(input_data), {})

    def test_bounded_input_scale_experiments(self):
        s1 = list(range(10))
        res1, checks1, emits1 = instrumented_even_squares(s1)
        self.assertEqual(checks1, 10)
        self.assertEqual(emits1, 5)
        self.assertEqual(len(res1), 5)

        s2 = list(range(50))
        res2, checks2, emits2 = instrumented_even_squares(s2)
        self.assertEqual(checks2, 50)
        self.assertEqual(emits2, 25)
        self.assertEqual(len(res2), 25)

        s3 = list(range(100))
        res3, checks3, emits3 = instrumented_even_squares(s3)
        self.assertEqual(checks3, 100)
        self.assertEqual(emits3, 50)
        self.assertEqual(len(res3), 50)

if __name__ == "__main__":
    unittest.main()
