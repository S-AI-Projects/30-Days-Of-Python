import unittest

try:
    from .example import arithmetic_report
except (ImportError, ValueError):
    from example import arithmetic_report

class TestArithmeticReport(unittest.TestCase):
    def test_fixture_positive_integers(self):
        result = arithmetic_report(7, 3)
        self.assertEqual(result, {"sum": 10, "difference": 4, "product": 21})

    def test_fixture_boundary_zero_zero(self):
        result = arithmetic_report(0, 0)
        self.assertEqual(result, {"sum": 0, "difference": 0, "product": 0})

    def test_invalid_input_none(self):
       with self.assertRaises(ValueError):
            arithmetic_report(None, 5)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            arithmetic_report(7.5, 3)
        with self.assertRaises(TypeError):
            arithmetic_report(True, 3)

if __name__ == "__main__":
    unittest.main()
