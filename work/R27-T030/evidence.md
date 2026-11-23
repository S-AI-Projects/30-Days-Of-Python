# Verification Evidence: R27-T030 (Issue #33)

## Task Summary
- **Issue**: #33 (`R27-T030`: Day 1: arithmetic report — refactor an applied example `[readme.md]`)
- **Command**: `python3 -m unittest discover -s ./applied-labs/r27-t030 -p "test_*.py" -v`

## Tool Versions
- Python: `Python 3.15.2`
- Git: `git version 2.54.0 (Apple Git-157)`

## Inputs & Expected vs. Actual Results

| Case | Input | Expected Result | Actual Result | Matches Pre-Refactor Version | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Contract fixture 1 | `(7, 3)` | `{"sum": 10, "difference": 4, "product": 21}` | `{"sum": 10, "difference": 4, "product": 21}` | Yes | PASS |
| Contract fixture 2 | `(0, 0)` | `{"sum": 0, "difference": 0, "product": 0}` | `{"sum": 0, "difference": 0, "product": 0}` | Yes | PASS |
| Extracted validation `validate_integer_pair` | `(True, 3)`, `(7, "3")`, `(2.5, 1)` | Raises `TypeError` | Raises `TypeError` | Yes | PASS |

## Unittest Output
```text
test_contract_seven_and_three (test_example.TestArithmeticReportRefactor.test_contract_seven_and_three) ... ok
test_contract_zero_and_zero (test_example.TestArithmeticReportRefactor.test_contract_zero_and_zero) ... ok
test_extracted_responsibility_validate_integer_pair (test_example.TestArithmeticReportRefactor.test_extracted_responsibility_validate_integer_pair) ... ok
test_refactored_version_matches_initial_working_version (test_example.TestArithmeticReportRefactor.test_refactored_version_matches_initial_working_version) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```
