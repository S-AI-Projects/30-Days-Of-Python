import unittest

from example import calculate_shipping_costs, shipping_cost


class ShippingCostTests(unittest.TestCase):
    def test_shipping_cost_boundaries(self):
        cases = (
            (49.99, 10),
            (50, 5),
            (99.99, 5),
            (100, 0),
        )
        for total, expected in cases:
            with self.subTest(total=total):
                self.assertEqual(shipping_cost(total), expected)

    def test_negative_total_is_rejected(self):
        with self.assertRaises(ValueError):
            shipping_cost(-1)

    def test_bounded_input_scales_and_operation_counts(self):
        base_inputs = [49.99, 50, 99.99, 100]
        base_expected = [10, 5, 5, 0]
        for size in (4, 40, 400):
            with self.subTest(input_count=size):
                inputs = base_inputs * (size // len(base_inputs))
                expected = base_expected * (size // len(base_expected))
                actual, operation_count = calculate_shipping_costs(inputs)
                self.assertEqual(actual, expected)
                self.assertEqual(operation_count, size)
                print(
                    f"input_count={size} expected_count={len(expected)} "
                    f"actual_count={len(actual)} operation_count={operation_count}"
                )


if __name__ == "__main__":
    unittest.main()
