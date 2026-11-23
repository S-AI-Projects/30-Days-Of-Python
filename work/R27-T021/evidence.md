# Verification Evidence: R27-T021 (Issue #3)

## Task Summary
- **Issue**: #3 (`R27-T021`: Day 30: capstone integration — implement the applied example `[30_Day_Conclusions/30_conclusions.md]`)
- **Command**: `python3 -m unittest discover -s 30_Day_Conclusions/applied-labs/r27-t021 -p "test_*.py" -v`

## Tool Versions
- Python: `Python 3.15.2`
- Git: `git version 2.54.0 (Apple Git-157)`

## Inputs & Expected vs. Actual Results

| Case | Input | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- |
| Valid expenses | `food,12.50\nfood,7.50\ntravel,5.00` | `food=20.00, travel=5.00`, `errors=[]` | `food=20.00, travel=5.00`, `errors=[]` | PASS |
| Negative expenses | `food,12.50\nfood,-4.00\nfood,7.50\ntravel,5.00\ntravel,-1.25` | `food=20.00, travel=5.00`, `error_lines=[2, 5]` | `food=20.00, travel=5.00`, `error_lines=[2, 5]` | PASS |
| Malformed & zero rows | `food,0.00\ninvalid_line\nbooks,abc` | `food=0.00`, `error_lines=[2, 3]` | `food=0.00`, `error_lines=[2, 3]` | PASS |

## Unittest Output
```text
test_contract_fixture_totals (test_example.TestExpenseSummarizer.test_contract_fixture_totals) ... ok
test_malformed_and_zero_expense_handling (test_example.TestExpenseSummarizer.test_malformed_and_zero_expense_handling) ... ok
test_negative_expenses_reported_by_line (test_example.TestExpenseSummarizer.test_negative_expenses_reported_by_line) ... ok
test_run_demo_executes_contract (test_example.TestExpenseSummarizer.test_run_demo_executes_contract) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```
