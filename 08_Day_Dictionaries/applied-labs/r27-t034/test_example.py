import unittest

try:
    from .example import apply_stock_changes
except (ImportError, ValueError):
    from example import apply_stock_changes

class TestInventoryMapping(unittest.TestCase):
    def test_fixture_successful_change(self):
        initial = {"tea": 3}
        changes = {"tea": -2, "coffee": 4}
        result = apply_stock_changes(initial, changes)
        self.assertEqual(result, {"tea": 1, "coffee": 4})

    def test_fixture_rejects_negative_and_leaves_original_unchanged(self):
        initial = {"tea": 3}
        invalid_change = {"tea": -4}
        with self.assertRaises(ValueError):
            apply_stock_changes(initial, invalid_change)
        self.assertEqual(initial, {"tea": 3})

    def test_sequence_of_operations_invariant(self):
        state = {"tea": 3}
        state = apply_stock_changes(state, {"tea": -2, "coffee": 4})
        self.assertTrue(all(v >= 0 for v in state.values()))
        self.assertEqual(state, {"tea": 1, "coffee": 4})

        state = apply_stock_changes(state, {"coffee": -1, "milk": 2})
        self.assertTrue(all(v >= 0 for v in state.values()))
        self.assertEqual(state, {"tea": 1, "coffee": 3, "milk": 2})

        with self.assertRaises(ValueError):
            apply_stock_changes(state, {"milk": -3})
        self.assertEqual(state, {"tea": 1, "coffee": 3, "milk": 2})

if __name__ == "__main__":
    unittest.main()
