import ast
import pathlib
import subprocess
import sys
import unittest

from example import text_stats, tokenize

HERE = pathlib.Path(__file__).parent

# The published worked example. example.py must print exactly this,
# and the README must contain exactly these lines.
EXPECTED_OUTPUT = [
    "input: 'one two two'",
    "split into words: ['one', 'two', 'two']",
    "distinct words: ['one', 'two']",
    "output: {'words': 3, 'distinct': 2}",
]


class TestTextStats(unittest.TestCase):
    def test_main_example(self):
        self.assertEqual(text_stats("one two two"), {"words": 3, "distinct": 2})

    def test_empty_text(self):
        self.assertEqual(text_stats(""), {"words": 0, "distinct": 0})

    def test_extra_whitespace_is_ignored(self):
        self.assertEqual(text_stats("  one   two\ttwo\n"), {"words": 3, "distinct": 2})

    def test_words_are_case_sensitive(self):
        self.assertEqual(text_stats("One one"), {"words": 2, "distinct": 2})

    def test_intermediate_state(self):
        self.assertEqual(tokenize("one two two"), ["one", "two", "two"])


class TestPackaging(unittest.TestCase):
    def test_published_example_runs_and_matches_readme(self):
        # Run example.py in a fresh process with user-site packages disabled (-s).
        result = subprocess.run(
            [sys.executable, "-s", str(HERE / "example.py")],
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.splitlines(), EXPECTED_OUTPUT)
        # The README's worked explanation must show the same lines.
        readme = (HERE / "README.md").read_text(encoding="utf-8")
        for line in EXPECTED_OUTPUT:
            self.assertIn(line, readme)

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

    def test_example_has_no_imports(self):
        tree = ast.parse((HERE / "example.py").read_text(encoding="utf-8"))
        imports = [n for n in ast.walk(tree) if isinstance(n, (ast.Import, ast.ImportFrom))]
        self.assertEqual(imports, [])


if __name__ == "__main__":
    unittest.main()