import unittest
from example import ShoppingCart, calculate_shipping


class TestShippingBands(unittest.TestCase):
    def test_fixture_shipping_bands(self):
        self.assertEqual(calculate_shipping(49.99), 10)
        self.assertEqual(calculate_shipping(50), 5)
        self.assertEqual(calculate_shipping(99.99), 5)
        self.assertEqual(calculate_shipping(100), 0)

    def test_negative_totals_rejected(self):
        with self.assertRaises(ValueError):
            calculate_shipping(-1)
        with self.assertRaises(ValueError):
            calculate_shipping(-0.01)

    def test_state_invariant_across_operation_sequence(self):
        cart = ShoppingCart()

        # Initial state (empty cart: total=0, shipping=10)
        valid, msg = cart.verify_invariant()
        self.assertTrue(valid, msg)
        self.assertEqual(cart.total, 0)
        self.assertEqual(cart.shipping, 10)
        self.assertEqual(cart.grand_total, 10)

        # Sequence of operations crossing boundary bands
        operations = [49.99, 0.01, 49.99, 0.01]
        expected_states = [
            # (total, shipping, grand_total)
            (49.99, 10, 59.99),
            (50.00, 5, 55.00),
            (99.99, 5, 104.99),
            (100.00, 0, 100.00),
        ]

        for price, (exp_total, exp_shipping, exp_grand) in zip(
            operations, expected_states
        ):
            cart.add_item(price)
            valid, msg = cart.verify_invariant()
            self.assertTrue(valid, msg)
            self.assertEqual(cart.total, exp_total)
            self.assertEqual(cart.shipping, exp_shipping)
            self.assertEqual(cart.grand_total, exp_grand)

    def test_negative_item_rejected_preserves_invariant(self):
        cart = ShoppingCart()
        cart.add_item(25.0)
        with self.assertRaises(ValueError):
            cart.add_item(-10.0)
        valid, msg = cart.verify_invariant()
        self.assertTrue(valid, msg)
        self.assertEqual(cart.total, 25.0)

    def test_invalid_type_rejected(self):
        with self.assertRaises(TypeError):
            calculate_shipping("fifty")


if __name__ == "__main__":
    unittest.main()
