import unittest
from example import translate


class TestTranslate(unittest.TestCase):
    def test_main_example(self):
        result = translate(((1, 2), (3, 4)), 2, -1)
        self.assertEqual(result, ((3, 1), (5, 3)))

    def test_input_unchanged(self):
        original = ((1, 2), (3, 4))
        translate(original, 2, -1)
        self.assertEqual(original, ((1, 2), (3, 4)))

    def test_empty_input_returns_empty_tuple(self):
        self.assertEqual(translate((), 5, 5), ())

    def test_zero_shift_returns_equal_points(self):
        self.assertEqual(translate(((1, 2),), 0, 0), ((1, 2),))

    def test_point_with_one_coordinate_raises(self):
        # Boundary: one below the required 2
        with self.assertRaises(ValueError):
            translate(((1,),), 1, 1)

    def test_point_with_three_coordinates_raises(self):
        # Boundary: one above the required 2
        with self.assertRaises(ValueError):
            translate(((1, 2, 3),), 1, 1)

    def test_empty_point_raises(self):
        with self.assertRaises(ValueError):
            translate(((),), 1, 1)

    def test_one_bad_point_among_good_ones_raises(self):
        with self.assertRaises(ValueError):
            translate(((1, 2), (3,)), 1, 1)

    def test_non_tuple_input_raises(self):
        with self.assertRaises(TypeError):
            translate([(1, 2)], 1, 1)


if __name__ == "__main__":
    unittest.main()