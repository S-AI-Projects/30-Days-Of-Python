# Verification Evidence: R27-T028 (Issue #31)

## Task Summary
- **Issue**: #31 (`R27-T028`: Day 10: run-length encoding — input-scale experiment `[10_Day_Loops/10_loops.md]`)
- **Command**: `python3 -m unittest discover -s 10_Day_Loops/applied-labs/r27-t028 -p "test_*.py" -v`

## Tool Versions
- Python: `Python 3.15.2`
- Git: `git version 2.54.0 (Apple Git-157)`

## Inputs & Expected vs. Actual Results

| Case | Input | Expected Encoded Output | Expected Operation Stats | Actual Encoded Output & Stats | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Scale $N=0$ | `""` | `[]` | `inspections=0, comparisons=0, emissions=0` | `[]`, matches stats | PASS |
| Single run | `"aaa"` | `[("a", 3)]` | `inspections=3, comparisons=2, emissions=1` | `[("a", 3)]`, matches stats | PASS |
| Scale $N=6$ | `"aaabbc"` | `[("a", 3), ("b", 2), ("c", 1)]` | `inspections=6, comparisons=5, emissions=3` | `[("a", 3), ("b", 2), ("c", 1)]`, matches stats | PASS |
| Scale $N=60$ | `"aaabbc" * 10` | `[("a", 3), ("b", 2), ("c", 1)] * 10` | `inspections=60, comparisons=59, emissions=30` | `[("a", 3), ("b", 2), ("c", 1)] * 10`, matches stats | PASS |

## Unittest Output
```text
test_contract_fixtures (test_example.TestRunLengthEncoding.test_contract_fixtures) ... ok
test_three_bounded_input_sizes_operation_counts (test_example.TestRunLengthEncoding.test_three_bounded_input_sizes_operation_counts) ... ok
test_total_decoded_count_equals_input_length (test_example.TestRunLengthEncoding.test_total_decoded_count_equals_input_length) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```
