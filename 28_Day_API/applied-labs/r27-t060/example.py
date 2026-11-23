"""R27-T060: HTTP contract testing with injected store and mutant detection."""

import json


def handle_request(method, path, body=None, *, store=None):
    """Simulate HTTP request handling on local /items endpoint with injected in-memory store.

    - POST a valid item returns (201, item)
    - GET lists stored items (200, items)
    - Malformed JSON yields (400, error)
    - Unsupported HTTP method yields (405, error)
    """
    if store is None:
        store = []

    if path != "/items":
        return 404, {"error": "Not Found"}

    if method not in ("GET", "POST"):
        return 405, {"error": "Method Not Allowed"}

    if method == "GET":
        return 200, list(store)

    if method == "POST":
        if body is None:
            return 400, {"error": "Malformed JSON"}
        try:
            data = json.loads(body)
            if not isinstance(data, dict):
                return 400, {"error": "Malformed JSON: expected JSON object"}
        except (ValueError, TypeError):
            return 400, {"error": "Malformed JSON"}

        store.append(data)
        # Decisive condition: Successful creation returns HTTP 201 Created
        return 201, data


def handle_request_mutant(method, path, body=None, *, store=None):
    """One-line mutant of the decisive status condition for mutation/regression testing.

    Mutant: returns 200 OK instead of 201 Created for resource creation.
    """
    status, payload = handle_request(method, path, body, store=store)
    # One-line mutant of the decisive condition
    if status == 201:
        status = 200  # MUTANT: incorrect status code for POST creation contract
    return status, payload


if __name__ == "__main__":
    memory_store = []
    print("1. POST valid item:")
    print("  ", handle_request("POST", "/items", '{"id": 1, "name": "keyboard"}', store=memory_store))
    print("2. GET items:")
    print("  ", handle_request("GET", "/items", store=memory_store))
    print("3. POST malformed JSON:")
    print("  ", handle_request("POST", "/items", "{invalid_json}", store=memory_store))
    print("4. Unsupported DELETE method:")
    print("  ", handle_request("DELETE", "/items", store=memory_store))
    print("5. Mutant POST status code:")
    print("  ", handle_request_mutant("POST", "/items", '{"id": 2}', store=[])[0])
