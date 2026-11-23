# Verification Evidence: R27-T025 (Issue #28)

## Task Summary
- **Issue**: #28 (`R27-T025`: Day 5: ordered deduplication — deterministic fixture lab `[05_Day_Lists/05_lists.md]`)
- **Command**: `python3 -m unittest discover -s 05_Day_Lists/applied-labs/r27-t025 -p "test_*.py" -v`

## Tool Versions
- Python: `Python 3.15.2`
- Git: `git version 2.54.0 (Apple Git-157)`

## Inputs & Expected vs. Actual Results

| Case | Input | Expected Output | Original List After Run | Isolated Runs Agree | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Contract sample | `[3, 1, 3, 2, 1]` | `[3, 1, 2]` | `[3, 1, 3, 2, 1]` | `True` | PASS |
| Empty sample | `[]` | `[]` | `[]` | `True` | PASS |
| All duplicates | `[7, 7, 7]` | `[7]` | `[7, 7, 7]` | `True` | PASS |
| Already unique | `[4, 5, 6]` | `[4, 5, 6]` | `[4, 5, 6]` | `True` | PASS |

## Unittest Output
```text
test_contract_deduplication_preserves_order_and_input (test_example.TestOrderedDeduplication.test_contract_deduplication_preserves_order_and_input) ... ok
test_empty_list_boundary (test_example.TestOrderedDeduplication.test_empty_list_boundary) ... ok
test_two_isolated_runs_with_injected_clock_and_sink_agree (test_example.TestOrderedDeduplication.test_two_isolated_runs_with_injected_clock_and_sink_agree) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```
