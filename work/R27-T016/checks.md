# R27-T016 check evidence

## Inputs and observed contract

The corresponding request inputs and expected responses are in
[`inputs.json`](inputs.json). The endpoint tests run over HTTP on an ephemeral
`127.0.0.1` port using an injected `InMemoryItemStore`; they do not call an
external service.

| Request | Expected result | Actual result |
|---|---|---|
| `POST /items`, `{"name": "notebook"}` | `201`, `{"id": 1, "name": "notebook"}` | `201`, `{"id": 1, "name": "notebook"}` |
| `GET /items` after POST | `200`, `[{"id": 1, "name": "notebook"}]` | `200`, `[{"id": 1, "name": "notebook"}]` |
| `POST /items`, `{"name":` | `400`, `{"error": "Malformed JSON"}` | `400`, `{"error": "Malformed JSON"}` |
| `PUT /items` | `405`, `{"error": "Method not allowed"}` | `405`, `{"error": "Method not allowed"}` |

## Behavior capture and refactor

Before refactoring, the working request branch handled JSON decoding and name
validation inline. The initial endpoint test run passed all three endpoint
tests, confirming the four HTTP results above. The implementation then
extracted this unchanged behavior to `parse_item_payload`; the final tests also
exercise that responsibility directly.

## Tool versions and final check

- Python: `Python 3.14.6`
- Git: `git version 2.55.0`
- GitHub CLI: `gh version 2.101.0 (2026-09-15)`

Command:

```sh
python3 -m unittest discover -s 28_Day_API/applied-labs/r27-t016 -p "test_*.py"
```

Post-refactor actual result:

```text
Ran 4 tests in 0.513s
OK
```

The test command exited with status `0`. It checks each contract response and
the extracted parser responsibility; unittest exits non-zero if an assertion
fails.

The executable was also started separately with
`python3 28_Day_API/applied-labs/r27-t016/example.py`. A loopback POST returned
`201 Created` with `{"id": 1, "name": "smoke"}`, and a subsequent GET returned
`200 OK` with `[{"id": 1, "name": "smoke"}]`.
