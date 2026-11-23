# Verification Evidence: R27-T026 (Issue #29)

## Task Summary
- **Issue**: #29 (`R27-T026`: Day 28: HTTP contract — executable lesson example `[28_Day_API/28_API.md]`)
- **Command**: `python3 -m unittest discover -s 28_Day_API/applied-labs/r27-t026 -p "test_*.py" -v`

## Tool Versions
- Python: `Python 3.15.2`
- Git: `git version 2.54.0 (Apple Git-157)`

## Inputs & Expected vs. Actual Results

| Step | Method & Path | Request Body | Expected Status & Output | Actual Status & Output | Store After Step | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | `POST /items` | `'{"id": 1, "name": "notebook"}'` | `201`, `{"id": 1, "name": "notebook"}` | `201`, `{"id": 1, "name": "notebook"}` | `[{"id": 1, "name": "notebook"}]` | PASS |
| 2 | `GET /items` | `None` | `200`, `[{"id": 1, "name": "notebook"}]` | `200`, `[{"id": 1, "name": "notebook"}]` | `[{"id": 1, "name": "notebook"}]` | PASS |
| 3 | `POST /items` | `'{"id": 2, "name": '` | `400`, error JSON | `400`, error JSON | `[{"id": 1, "name": "notebook"}]` | PASS |
| 4 | `DELETE /items` | `None` | `405`, error JSON | `405`, error JSON | `[{"id": 1, "name": "notebook"}]` | PASS |

## Unittest Output
```text
test_malformed_json_yields_400_and_does_not_mutate_store (test_example.TestHttpContractItemsEndpoint.test_malformed_json_yields_400_and_does_not_mutate_store) ... ok
test_post_valid_item_returns_201_and_get_lists_it (test_example.TestHttpContractItemsEndpoint.test_post_valid_item_returns_201_and_get_lists_it) ... ok
test_published_lesson_example_is_executable (test_example.TestHttpContractItemsEndpoint.test_published_lesson_example_is_executable) ... ok
test_unsupported_method_yields_405 (test_example.TestHttpContractItemsEndpoint.test_unsupported_method_yields_405) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```
