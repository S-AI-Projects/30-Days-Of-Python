# Day 28 Applied Lab (`R27-T026`): Local `/items` HTTP Contract Executable Lesson Example

## Overview
This applied lab models a local `/items` HTTP endpoint supporting `GET` and `POST` against an injected in-memory list store, without requiring external sockets or third-party servers.

## Worked Walkthrough: Input $\rightarrow$ Intermediate Store State $\rightarrow$ Output

1. **`POST /items` with valid JSON `{"id": 1, "name": "notebook"}`**:
   - *Input*: `method="POST"`, `path="/items"`, `body='{"id": 1, "name": "notebook"}'`, `store=[]`
   - *Intermediate state*: JSON parses into a dict and is appended to `store` (`store == [{"id": 1, "name": "notebook"}]`).
   - *Output*: HTTP status `201`, response payload `{"id": 1, "name": "notebook"}`.
2. **`GET /items`**:
   - *Input*: `method="GET"`, `path="/items"`, `store=[{"id": 1, "name": "notebook"}]`
   - *Intermediate state*: Reads current snapshot of `store` without mutating it.
   - *Output*: HTTP status `200`, response payload `[{"id": 1, "name": "notebook"}]`.
3. **`POST /items` with malformed JSON `'{"id": 2, "name": '`**:
   - *Input*: `method="POST"`, `path="/items"`, `body='{"id": 2, "name": '`
   - *Intermediate state*: `json.loads` raises `JSONDecodeError`; `store` remains `[{"id": 1, "name": "notebook"}]`.
   - *Output*: HTTP status `400`.
4. **`DELETE /items` (unsupported method)**:
   - *Input*: `method="DELETE"`, `path="/items"`
   - *Intermediate state*: Method is not in `["GET", "POST"]`; `store` remains unchanged.
   - *Output*: HTTP status `405` with `Allow: GET, POST`.

## Running the Example and Tests
From the repository root:

```bash
python3 28_Day_API/applied-labs/r27-t026/example.py
python3 -m unittest discover -s 28_Day_API/applied-labs/r27-t026 -p "test_*.py"
```
