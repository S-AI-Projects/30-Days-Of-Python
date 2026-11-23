# Day 24 Applied Lab (`R27-T024`): Missing-Value Summary State/Invariant Lab

## Overview
This lab calculates `count`, `missing_count`, `mean`, and `median` for numeric observation lists that may contain `None` values, and verifies state invariants across a sequence of observation insertions.

## Stated Invariants
Across any sequence of operations on observations $O$:
1. **Partition invariant**: `count + missing_count == len(O)`.
2. **All-missing nullity invariant**: `count == 0` if and only if `mean is None and median is None`.
3. **Missing-observation stability & bounds invariant**: Appending `None` increments `missing_count` by 1 while leaving `count`, `mean`, and `median` unchanged; when `count > 0`, `min(valid) <= mean <= max(valid)` and `min(valid) <= median <= max(valid)`.

## Contract Fixtures
- `[1, None, 3, 5]` $\rightarrow$ `{"count": 3, "missing_count": 1, "mean": 3, "median": 3}`
- `[None, None]` $\rightarrow$ `{"count": 0, "missing_count": 2, "mean": None, "median": None}`

## Running the Example and Tests
From the repository root:

```bash
python3 24_Day_Statistics/applied-labs/r27-t024/example.py
python3 -m unittest discover -s 24_Day_Statistics/applied-labs/r27-t024 -p "test_*.py"
```
