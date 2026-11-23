import unittest
from example import CSVAnalyzer, MalformedRowError, analyze_csv


class TestCSVAnalyzer(unittest.TestCase):
    def test_fixture_grouping(self):
        result = analyze_csv("A:2,A:3,B:4")
        expected = {
            "A": {"count": 2, "sum": 5},
            "B": {"count": 1, "sum": 4},
        }
        self.assertEqual(result, expected)

    def test_multiline_and_comma_separated(self):
        csv_data = "category,amount\nA,2\nA,3\nB,4"
        result = analyze_csv(csv_data)
        expected = {
            "A": {"count": 2, "sum": 5},
            "B": {"count": 1, "sum": 4},
        }
        self.assertEqual(result, expected)

    def test_malformed_amount_identifies_line_number(self):
        bad_csv = "A,2\nA,not_a_number\nB,4"
        with self.assertRaises(MalformedRowError) as cm:
            analyze_csv(bad_csv)
        self.assertEqual(cm.exception.line_number, 2)
        self.assertIn("line 2", str(cm.exception))

    def test_failure_and_recovery_without_restart(self):
        analyzer = CSVAnalyzer()

        # Step 1: Encounter malformed input
        with self.assertRaises(MalformedRowError) as cm:
            analyzer.analyze("A,2\nA,malformed_val\nB,4")
        self.assertEqual(cm.exception.line_number, 2)
        self.assertEqual(analyzer.last_status, "error")

        # Step 2: Immediate recovery on next valid input on the same instance
        recovered = analyzer.analyze("A:2,A:3,B:4")
        self.assertEqual(analyzer.last_status, "success")
        self.assertEqual(
            recovered,
            {"A": {"count": 2, "sum": 5}, "B": {"count": 1, "sum": 4}},
        )

    def test_empty_state_and_recovery(self):
        analyzer = CSVAnalyzer()
        self.assertEqual(analyzer.analyze(""), {})
        self.assertEqual(analyzer.last_status, "empty")

        recovered = analyzer.analyze("X:10\nY:25")
        self.assertEqual(
            recovered,
            {"X": {"count": 1, "sum": 10}, "Y": {"count": 1, "sum": 25}},
        )

    def test_invalid_type_rejected(self):
        with self.assertRaises(TypeError):
            analyze_csv(None)


if __name__ == "__main__":
    unittest.main()
