# Day 5 Applied Lab (`R27-T025`): Ordered Deduplication Deterministic Fixture Lab

## Overview
This lab removes duplicate elements from a list while preserving first-occurrence order and leaving the original input list untouched. To guarantee deterministic repeatability across isolated runs, an optional event sink and clock callable are injected rather than reading global state or wall-clock time.

## Contract Fixtures
- `[3, 1, 3, 2, 1]` $\rightarrow$ `[3, 1, 2]`, while the original list remains `[3, 1, 3, 2, 1]`.
- `[]` $\rightarrow$ `[]`.
- Two isolated executions of `run_isolated_fixture("contract_sample")` produce identical outputs and identical event logs (`run_one == run_two`).

## Running the Example and Tests
From the repository root:

```bash
python3 05_Day_Lists/applied-labs/r27-t025/example.py
python3 -m unittest discover -s 05_Day_Lists/applied-labs/r27-t025 -p "test_*.py"
```
