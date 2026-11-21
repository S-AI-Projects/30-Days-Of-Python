import ast
import itertools
import pathlib
import subprocess
import sys
import unittest

from example import reference_text_stats, text_stats

HERE = pathlib.Path(__file__).parent

# Independent expected-result table: (text, words, distinct).
# Worked out by hand, not produced by running either function.
TABLE = [
    ("one two two", 3, 2),
    ("", 0, 0),
    ("   ", 0, 0),
    ("one", 1, 1),
    ("a a a", 3, 1),
    ("One one", 2, 2),
    ("  one   two\ttwo\n", 3, 2),
    ("a\nb\nc", 3, 3),
]

EXPECTED_OUTPUT = [
    "text_stats: {'words': 3, 'distinct': 2}",
    "reference: {'words': 3, 'distinct': 2}",
]

ALPHABET = ["a", "b", " ", "\t"]
MAX_LENGTH = 6
EXPECTED_STRING_COUNT = sum(len(ALPHABET) ** n for n in range(MAX_LENGTH + 1))  # 5461


def all_short_strings():
    """Every string over ALPHABET with length 0 to MAX_LENGTH (no randomness)."""
    for length in range(MAX_LENGTH + 1):
        for chars in itertools.product(ALPHABET, repeat=length):
            yield "".join(chars)


class TestAgainstTable(unittest.TestCase):
    def test_main_example(self):
        self.assertEqual(text_stats("one two two"), {"words": 3, "distinct": 2})

    def test_implementation_matches_table(self):
        for text, words, distinct in TABLE:
            with self.subTest(text=text):
                self.assertEqual(text_stats(text), {"words": words, "distinct": distinct})

    def test_reference_matches_table(self):
        # The reference must be correct too, not just "different".
        for text, words, distinct in TABLE:
            with self.subTest(text=text):
                self.assertEqual(
                    reference_text_stats(text), {"words": words, "distinct": distinct}
                )


class TestAgainstReference(unittest.TestCase):
    def test_implementation_matches_reference_on_all_short_strings(self):
        checked = 0
        for text in all_short_strings():
            self.assertEqual(text_stats(text), reference_text_stats(text), repr(text))
            checked += 1
        self.assertEqual(checked, EXPECTED_STRING_COUNT)
        print(f"compared {checked} strings, all agree")

    def test_reference_is_independent(self):
        tree = ast.parse((HERE / "example.py").read_text(encoding="utf-8"))
        func = next(
            n for n in tree.body
            if isinstance(n, ast.FunctionDef) and n.name == "reference_text_stats"
        )
        attributes = {n.attr for n in ast.walk(func) if isinstance(n, ast.Attribute)}
        names = {n.id for n in ast.walk(func) if isinstance(n, ast.Name)}
        self.assertNotIn("split", attributes)
        self.assertNotIn("set", names)
        self.assertNotIn("Counter", names)


class TestPackaging(unittest.TestCase):
    def test_import_without_user_site_packages(self):
        code = (
            "import sys, example; "
            "assert sys.flags.no_user_site == 1; "
            "print(example.text_stats('one two two'))"
        )
        result = subprocess.run(
            [sys.executable, "-s", "-c", code],
            cwd=HERE,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("'words': 3", result.stdout)

    def test_declared_dependencies_are_empty(self):
        lines = (HERE / "requirements.txt").read_text(encoding="utf-8").splitlines()
        declared = [l.strip() for l in lines if l.strip() and not l.strip().startswith("#")]
        self.assertEqual(declared, [])

    def test_example_runs_in_fresh_process(self):
        result = subprocess.run(
            [sys.executable, "-s", str(HERE / "example.py")],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.splitlines(), EXPECTED_OUTPUT)

    def test_example_has_no_imports(self):
        tree = ast.parse((HERE / "example.py").read_text(encoding="utf-8"))
        imports = [n for n in ast.walk(tree) if isinstance(n, (ast.Import, ast.ImportFrom))]
        self.assertEqual(imports, [])


if __name__ == "__main__":
    unittest.main()