# Applied Lab R27-T048: Parse Integers with Indexed Errors

Added activity (not an original numbered exercise).

Parses integers from a list of text records. It returns the valid values
plus a list of errors, each with the index of the bad record. Only
`ValueError` is caught; unrelated exceptions are not swallowed, and no
bare `except` is used.

- Input: `["3", "bad", "-2"]`
- Expected: values `[3, -2]` and one error at index 1
- Input: `[]`
- Expected: `([], [])` (the empty state)
- Input: `["bad"]`, then `["7"]` in the same session
- Expected: first call has no values and one error; the next call recovers
  with `[7]` and no errors
- Input: `["3", None, "5"]`
- Expected: `TypeError` (not swallowed)

Run the tests from the repository root:

    python3 -m unittest discover -s 15_Day_Python_type_errors/applied-labs/r27-t048 -p "test_*.py"

Failure and recovery: running `example.py` shows the empty state, an
error, and a successful recovery on the next valid input, all in one
session without restarting. The test `test_no_bare_except_in_source`
checks the source code itself, so a bare `except` would fail the tests.