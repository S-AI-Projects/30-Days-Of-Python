import ast
import pathlib
import unittest

from example import parse_integers


class TestParseIntegers(unittest.TestCase):
    def test_main_example(self):
        values, errors = parse_integers(["3", "bad", "-2"])
        self.assertEqual(values, [3, -2])
        self.assertEqual(len(errors), 1)
        self.assertEqual(errors[0][:2], (1, "bad"))  # index 1, the bad record

    def test_empty_input_gives_empty_state(self):
        self.assertEqual(parse_integers([]), ([], []))

    def test_all_invalid_gives_no_values_and_all_errors(self):
        values, errors = parse_integers(["bad", "", "1.5"])
        self.assertEqual(values, [])
        self.assertEqual([e[0] for e in errors], [0, 1, 2])

    def test_recovery_after_error_in_same_session(self):
        # Error state first...
        values, errors = parse_integers(["bad"])
        self.assertEqual(values, [])
        self.assertEqual(len(errors), 1)
        # ...then the next valid input works without restarting anything.
        values, errors = parse_integers(["7"])
        self.assertEqual(values, [7])
        self.assertEqual(errors, [])

    def test_unrelated_exception_is_not_swallowed(self):
        # None raises TypeError, which is a different problem from bad text.
        with self.assertRaises(TypeError):
            parse_integers(["3", None, "5"])

    def test_no_bare_except_in_source(self):
        source = pathlib.Path(__file__).with_name("example.py").read_text()
        handlers = [
            node for node in ast.walk(ast.parse(source))
            if isinstance(node, ast.ExceptHandler)
        ]
        self.assertTrue(handlers)  # the example does handle errors
        for handler in handlers:
            self.assertIsInstance(handler.type, ast.Name)  # not a bare except
            self.assertEqual(handler.type.id, "ValueError")  # only ValueError


if __name__ == "__main__":
    unittest.main()
    