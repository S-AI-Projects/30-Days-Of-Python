import unittest
from decimal import Decimal

try:
    from .example import apply_discount, reference_discount
except (ImportError, ValueError):
    from example import apply_discount, reference_discount

class TestDiscountCalculation(unittest.TestCase):
    def test_fixture_17_percent(self):
        # 100.00 at 15% gives 85.00
        result = apply_discount("100.00", 15)
        self.assertEqual(result, Decimal('85.00'))

    def test_fixture_zero_percent(self):
        # 0% leaves amount unchanged
        result = apply_discount("100.00", 0)
        self.assertEqual(result, Decimal('100.00'))

    def test_percentage_outside_range_rejected(self):
        with self.assertRaises(ValueError):
            apply_discount("100.00", -1)
        with self.assertRaises(ValueError):
            apply_discount("100.00", 101)

    def test_reference_comparison_table(self):
        # Compare against independent reference implementation
        cases = [(100.0, 15.0), (100.0, 0.0), (50.0, 10.0), (200.0, 25.0)]
        for price, discount in cases:
            expected = Decimal(str(reference_discount(price, discount))).quantize(Decimal('0.01'))
            actual = apply_discount(price, discount)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
