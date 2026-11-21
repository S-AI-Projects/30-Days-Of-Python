import ast
import io
import pathlib
import subprocess
import sys
import unittest

from example import BAD_FIXTURE, FIXTURE, group_csv

HERE = pathlib.Path(__file__).parent

# What `python3 example.py` must print, every time.
EXPECTED_OUTPUT = [
    "A: count=2 sum=5",
    "B: count=1 sum=4",
    "---",
    "A: count=1 sum=2",
    "B: count=1 sum=4",
    "line 3: amount is not an integer: 'oops'",
    "line 4: expected 2 fields, got 1",
    "line 6: empty category",
]


class TestGrouping(unittest.TestCase):
    def test_main_example(self):
        groups, errors = group_csv(io.StringIO(FIXTURE))
        self.assertEqual(
            groups,
            {"A": {"count": 2, "sum": 5}, "B": {"count": 1, "sum": 4}},
        )
        self.assertEqual(errors, [])

    def test_negative_amounts_are_summed(self):
        groups, errors = group_csv(["category,amount", "A,5", "A,-2"])
        self.assertEqual(groups, {"A": {"count": 2, "sum": 3}})
        self.assertEqual(errors, [])

    def test_empty_input(self):
        self.assertEqual(group_csv(io.StringIO("")), ({}, []))

    def test_header_only(self):
        self.assertEqual(group_csv(io.StringIO("category,amount\n")), ({}, []))

    def test_malformed_rows_identify_their_line_number(self):
        groups, errors = group_csv(io.StringIO(BAD_FIXTURE))
        self.assertEqual(
            errors,
            [
                (3, "amount is not an integer: 'oops'"),
                (4, "expected 2 fields, got 1"),
                (6, "empty category"),
            ],
        )
        # The good rows are still counted.
        self.assertEqual(
            groups,
            {"A": {"count": 1, "sum": 2}, "B": {"count": 1, "sum": 4}},
        )

    def test_malformed_rows_are_not_silently_dropped(self):
        groups, errors = group_csv(io.StringIO(BAD_FIXTURE))
        data_rows = 5  # BAD_FIXTURE has 5 data rows after the header
        counted = sum(entry["count"] for entry in groups.values())
        self.assertEqual(counted + len(errors), data_rows)

    def test_blank_line_is_reported_not_skipped(self):
        groups, errors = group_csv(io.StringIO("category,amount\nA,2\n\nB,4\n"))
        self.assertEqual(errors, [(3, "expected 2 fields, got 0")])
        self.assertEqual(
            groups,
            {"A": {"count": 1, "sum": 2}, "B": {"count": 1, "sum": 4}},
        )


class TestIsolation(unittest.TestCase):
    def test_source_is_injected(self):
        # The same data through two different kinds of source gives the same answer.
        from_stream = group_csv(io.StringIO(FIXTURE))
        from_list = group_csv(FIXTURE.splitlines())
        self.assertEqual(from_stream, from_list)

    def test_two_calls_agree(self):
        # No state is carried over between calls.
        first = group_csv(io.StringIO(BAD_FIXTURE))
        second = group_csv(io.StringIO(BAD_FIXTURE))
        self.assertEqual(first, second)

    def test_two_isolated_processes_agree(self):
        outputs = []
        for _ in range(2):
            result = subprocess.run(
                [sys.executable, str(HERE / "example.py")],
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            outputs.append(result.stdout.splitlines())
        self.assertEqual(outputs[0], outputs[1])
        self.assertEqual(outputs[0], EXPECTED_OUTPUT)

    def test_example_imports_only_csv_and_io(self):
        # No time, random, network or file modules: nothing to inject but the lines.
        tree = ast.parse((HERE / "example.py").read_text(encoding="utf-8"))
        names = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                names.update(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom):
                names.add(node.module)
        self.assertEqual(names, {"csv", "io"})


if __name__ == "__main__":
    unittest.main()