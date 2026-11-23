# Verification Evidence: R27-T027 (Issue #30)

## Task Summary
- **Issue**: #30 (`R27-T027`: Day 19: CSV round trip — failure-and-recovery lab `[19_Day_File_handling/19_file_handling.md]`)
- **Command**: `python3 -m unittest discover -s 19_Day_File_handling/applied-labs/r27-t027 -p "test_*.py" -v`

## Tool Versions
- Python: `Python 3.15.2`
- Git: `git version 2.54.0 (Apple Git-157)`

## Inputs & Expected vs. Actual Results

| Step | Input Records | Expected CSV & Parsed Result | Actual CSV & Parsed Result | Session State | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 (Empty state) | `[]` | `"name,score\n"`, `[]` | `"name,score\n"`, `[]` | `empty_header_only` | PASS |
| 2 (Error state) | `[{"name": "Ada, Jr.", "score": "bad"}]` | Raises / captures `ValueError` without crashing session | Captures `ValueError`, retains prior valid state | `error` | PASS |
| 3 (Recovery state) | `[{"name": "Ada, Jr.", "score": 7}]` | `'name,score\n"Ada, Jr.",7\n'`, `[{"name": "Ada, Jr.", "score": 7}]` | `'name,score\n"Ada, Jr.",7\n'`, `[{"name": "Ada, Jr.", "score": 7}]` | `ok` | PASS |

## Unittest Output
```text
test_empty_data_produces_only_header (test_example.TestCsvRoundTripRecovery.test_empty_data_produces_only_header) ... ok
test_failure_and_empty_state_then_recovery_without_restart (test_example.TestCsvRoundTripRecovery.test_failure_and_empty_state_then_recovery_without_restart) ... ok
test_quoted_comma_record_survives_utf8_file_round_trip (test_example.TestCsvRoundTripRecovery.test_quoted_comma_record_survives_utf8_file_round_trip) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```
