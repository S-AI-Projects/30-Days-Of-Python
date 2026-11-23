# Verification Evidence: R27-T024 (Issue #27)

## Task Summary
- **Issue**: #27 (`R27-T024`: Day 24: missing-value summary — state/invariant lab `[24_Day_Statistics/24_statistics.md]`)
- **Command**: `python3 -m unittest discover -s 24_Day_Statistics/applied-labs/r27-t024 -p "test_*.py" -v`

## Tool Versions
- Python: `Python 3.15.2`
- Git: `git version 2.54.0 (Apple Git-157)`

## Inputs & Expected vs. Actual Results

| Case | Input | Expected Result | Actual Result | Invariant Check | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Contract fixture | `[1, None, 3, 5]` | `{"count": 3, "missing_count": 1, "mean": 3, "median": 3}` | `{"count": 3, "missing_count": 1, "mean": 3, "median": 3}` | `True` | PASS |
| All-missing | `[None, None]` | `{"count": 0, "missing_count": 2, "mean": None, "median": None}` | `{"count": 0, "missing_count": 2, "mean": None, "median": None}` | `True` | PASS |
| Empty observations | `[]` | `{"count": 0, "missing_count": 0, "mean": None, "median": None}` | `{"count": 0, "missing_count": 0, "mean": None, "median": None}` | `True` | PASS |
| Sequential `ObservationTracker` | `add(1) -> add(None) -> add(3) -> add(5)` | Final state matches `[1, None, 3, 5]` & invariants hold at every step | Final state matches `[1, None, 3, 5]` & invariants hold at every step | `True` | PASS |

## Unittest Output
```text
test_all_missing_and_empty_yield_null_mean_and_median (test_example.TestMissingValueSummary.test_all_missing_and_empty_yield_null_mean_and_median) ... ok
test_contract_fixture (test_example.TestMissingValueSummary.test_contract_fixture) ... ok
test_state_invariants_across_sequence_of_operations (test_example.TestMissingValueSummary.test_state_invariants_across_sequence_of_operations) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```
