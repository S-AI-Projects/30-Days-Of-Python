# Applied Lab R27-T045: Group a CSV by Category

Added activity (not an original numbered exercise).

Groups a supplied CSV by category and calculates the count and sum for
each. Malformed rows are never silently dropped: each one is reported
with its line number. This lab uses only the standard library (`csv`).

- Input (header `category,amount`, then rows `A,2` / `A,3` / `B,4`)
- Expected: `A(count=2, sum=5)` and `B(count=1, sum=4)`, no errors
- Input with malformed rows:

```
category,amount
A,2
A,oops
B
B,4
,7
```

- Expected: `A(count=1, sum=2)`, `B(count=1, sum=4)`, and errors at
  line 3 (amount is not an integer), line 4 (expected 2 fields, got 1)
  and line 6 (empty category)

Line numbers count the header as line 1, so the first data row is line 2.
Amounts must be integers.

## Repeatable runs (injection)

`group_csv(lines)` receives its data as lines passed in. It never opens a
file, reads the clock, uses randomness, or touches the network, so the
tests use in-memory text and get the same answer every time. Categories
are sorted in the report so the output order never changes. The test
`test_two_isolated_processes_agree` runs `example.py` in two separate
processes and checks that both print exactly the same output.

## Run the tests

From the repository root:

    python3 -m unittest discover -s 25_Day_Pandas/applied-labs/r27-t045 -p "test_*.py"

## Run the example

    python3 25_Day_Pandas/applied-labs/r27-t045/example.py
    