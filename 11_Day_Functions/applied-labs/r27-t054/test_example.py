import unittest
from example import price, validate_quantity


class TestPrice(unittest.TestCase):
    def test_discount_applied(self):
        self.assertEqual(price(3, unit_price=10, discount=0.1), 27)

    def test_zero_quantity(self):
        self.assertEqual(price(0, unit_price=10, discount=0.1), 0)

    def test_negative_quantity_rejected(self):
        with self.assertRaises(ValueError):
            price(-1, unit_price=10)

    def test_keyword_only(self):
        with self.assertRaises(TypeError):
            price(3, 10, 0.1)

    def test_validate_quantity_helper(self):
        validate_quantity(0)  # must not raise
        with self.assertRaises(ValueError):
            validate_quantity(-5)


if __name__ == "__main__":
    unittest.main()