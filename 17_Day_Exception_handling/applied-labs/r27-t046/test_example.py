import ast
import copy
import pathlib
import subprocess
import sys
import unittest

from example import (
    ALLOWED,
    DEFAULTS,
    merge_options,
    merge_options_original,
    reject_unknown_keys,
)

HERE = pathlib.Path(__file__).parent

# The behavior of the working version, captured BEFORE refactoring.
# Both versions must match every row, which proves the contract is unchanged.
CAPTURED = [
    ({}, ("ok", {"limit": 10, "reverse": False})),
    ({"limit": 3}, ("ok", {"limit": 3, "reverse": False})),
    ({"reverse": True}, ("ok", {"limit": 10, "reverse": True})),
    ({"limit": 3, "reverse": True}, ("ok", {"limit": 3, "reverse": True})),
    ({"limt": 3}, ("error", "Unknown option(s): limt")),
    ({"revers": True, "limt": 3}, ("error", "Unknown option(s): limt, revers")),
    ({"defaults": 1}, ("error", "Unknown option(s): defaults")),
    ({"allowed": 1}, ("error", "Unknown option(s): allowed")),
]

EXPECTED_OUTPUT = [
    "{'limit': 3, 'reverse': False}",
    "rejected: Unknown option(s): limt",
]


def outcome(func, overrides):
    try:
        return ("ok", func(DEFAULTS, ALLOWED, **overrides))
    except ValueError as exc:
        return ("error", str(exc))


def calls_inside(function_name):
    """Names of the plain functions called inside a function in example.py."""
    tree = ast.parse((HERE / "example.py").read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == function_name:
            return {
                n.func.id
                for n in ast.walk(node)
                if isinstance(n, ast.Call) and isinstance(n.func, ast.Name)
            }
    raise AssertionError(f"{function_name} not found in example.py")


class TestContract(unittest.TestCase):
    def test_main_example(self):
        result = merge_options(DEFAULTS, ALLOWED, limit=3)
        self.assertEqual(result, {"limit": 3, "reverse": False})

    def test_typo_limt_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "limt"):
            merge_options(DEFAULTS, ALLOWED, limt=3)

    def test_inputs_are_not_modified(self):
        defaults = copy.deepcopy(DEFAULTS)
        allowed = copy.deepcopy(ALLOWED)
        merge_options(defaults, allowed, limit=3)
        self.assertEqual(defaults, DEFAULTS)
        self.assertEqual(allowed, ALLOWED)


class TestRefactoring(unittest.TestCase):
    def test_original_version_matches_captured_behavior(self):
        for overrides, expected in CAPTURED:
            with self.subTest(overrides=overrides):
                self.assertEqual(outcome(merge_options_original, overrides), expected)

    def test_refactored_version_matches_captured_behavior(self):
        for overrides, expected in CAPTURED:
            with self.subTest(overrides=overrides):
                self.assertEqual(outcome(merge_options, overrides), expected)

    def test_extracted_responsibility_on_its_own(self):
        self.assertIsNone(reject_unknown_keys({"limit": 3}, ALLOWED))
        with self.assertRaisesRegex(ValueError, "limt"):
            reject_unknown_keys({"limt": 3}, ALLOWED)

    def test_refactored_version_calls_the_extracted_function(self):
        self.assertIn("reject_unknown_keys", calls_inside("merge_options"))
        self.assertNotIn("reject_unknown_keys", calls_inside("merge_options_original"))


class TestPublishedExample(unittest.TestCase):
    def test_example_runs_in_fresh_process(self):
        result = subprocess.run(
            [sys.executable, str(HERE / "example.py")],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.splitlines(), EXPECTED_OUTPUT)


if __name__ == "__main__":
    unittest.main()