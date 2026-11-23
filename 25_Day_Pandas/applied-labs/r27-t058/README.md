# R27-T058: Small CSV analysis with failure and recovery handling

`analyze_csv(csv_input)` groups supplied CSV data by category and calculates `count` and `sum`.

## Contract and Guarantees

- **Grouped Totals**: `A:2,A:3,B:4` produces `A(count=2, sum=5)` and `B(count=1, sum=4)`.
- **No Silent Drops**: Malformed amounts are never silently skipped; a `MalformedRowError` is raised identifying the exact line number.
- **Failure and Recovery**: `CSVAnalyzer` handles error or empty states and cleanly recovers on subsequent valid inputs without restarting.

## Run the tests

From the repository root:

    python3 -m unittest discover -s 25_Day_Pandas/applied-labs/r27-t058 -p "test_*.py"
