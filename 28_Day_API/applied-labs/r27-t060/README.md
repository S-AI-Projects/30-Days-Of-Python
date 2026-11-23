# R27-T060: HTTP contract testing with injected in-memory store and mutant detection

`handle_request(method, path, body=None, *, store=None)` simulates HTTP request handling for a local `/items` endpoint.

## Contract and Expected Responses

- **POST /items (valid JSON)**: Returns `201 Created` and stores the item.
- **GET /items**: Returns `200 OK` with the list of stored items.
- **POST /items (malformed JSON)**: Returns `400 Bad Request`.
- **Unsupported HTTP methods (e.g. DELETE, PUT)**: Returns `405 Method Not Allowed`.

## Mutation and Regression Verification

- **Decisive Condition**: The return of `201 Created` specifically indicates resource creation according to REST/HTTP standards.
- **Mutant (`handle_request_mutant`)**: Mutates the decisive status condition to return `200 OK` instead of `201 Created`.
- **Focused Test**: `test_focused_regression_passes_on_correct_and_fails_on_mutant` passes on `handle_request` and catches the mutant by raising `AssertionError`.

## Run the tests

From the repository root:

    python3 -m unittest discover -s 28_Day_API/applied-labs/r27-t060 -p "test_*.py"
