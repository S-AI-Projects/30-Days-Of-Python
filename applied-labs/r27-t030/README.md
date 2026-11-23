# Day 1 Applied Lab (`R27-T030`): Arithmetic Report — Refactor an Applied Example

## Overview
This applied lab returns `{"sum": a + b, "difference": a - b, "product": a * b}` for two integers `(a, b)`. It starts from a single-function working version (`arithmetic_report_initial`), captures its exact behavior in tests, and extracts integer-operand validation into a single clearly named helper (`validate_integer_pair`) used by `arithmetic_report` without changing the external contract.

## Contract Fixtures
- `(7, 3)` $\rightarrow$ `{"sum": 10, "difference": 4, "product": 21}`
- `(0, 0)` $\rightarrow$ `{"sum": 0, "difference": 0, "product": 0}`
- Non-integer inputs (including `bool` or `float`) raise `TypeError` in both the initial and refactored versions.

## Running the Example and Tests
From the repository root:

```bash
python3 ./applied-labs/r27-t030/example.py
python3 -m unittest discover -s ./applied-labs/r27-t030 -p "test_*.py"
```
