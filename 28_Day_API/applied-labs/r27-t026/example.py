"""Day 28 Applied Lab (R27-T026): HTTP Contract Executable Lesson Example.

Contract:
- Test a local `/items` endpoint with `GET` and `POST` using an injected in-memory store.
- `POST` a valid item returns `201`; `GET` lists it; malformed JSON yields `400`;
  an unsupported method yields `405`.
- Contribution focus: Add a worked explanation from input through intermediate state to
  output, and make the published example executable by the test.
"""

from __future__ import annotations

import json
from typing import Dict, List, Optional


def handle_items_request(
    method: str,
    path: str,
    body: Optional[str] = None,
    store: Optional[List[Dict[str, object]]] = None,
) -> Dict[str, object]:
    """Handle an HTTP-style request against the local `/items` endpoint.

    Args:
        method: HTTP verb (`"GET"`, `"POST"`, etc.).
        path: Request path (expected `"/items"`).
        body: Optional raw JSON request body string for `POST`.
        store: Injected in-memory list serving as the item store.

    Returns:
        A dict containing `status` (int), `headers` (dict), `body` (JSON string),
        `data` (parsed JSON payload), and `trace` (worked intermediate state explanation).
    """
    target_store = store if store is not None else []
    normalized_method = method.upper().strip()

    if path != "/items":
        payload: object = {"error": "Not Found", "path": path}
        return {
            "status": 404,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(payload),
            "data": payload,
            "trace": f"Path {path!r} != '/items' -> 404 Not Found",
        }

    if normalized_method == "GET":
        snapshot = list(target_store)
        return {
            "status": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(snapshot),
            "data": snapshot,
            "trace": (
                f"GET /items -> read {len(snapshot)} item(s) from injected store -> 200 OK"
            ),
        }

    if normalized_method == "POST":
        if body is None or not body.strip():
            err_payload = {"error": "Bad Request: empty body"}
            return {
                "status": 400,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps(err_payload),
                "data": err_payload,
                "trace": "POST /items with empty body -> store unchanged -> 400 Bad Request",
            }
        try:
            parsed = json.loads(body)
        except json.JSONDecodeError:
            err_payload = {"error": "Bad Request: malformed JSON"}
            return {
                "status": 400,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps(err_payload),
                "data": err_payload,
                "trace": "POST /items with malformed JSON -> JSONDecodeError -> 400 Bad Request",
            }

        if not isinstance(parsed, dict) or not parsed:
            err_payload = {"error": "Bad Request: expected non-empty JSON object"}
            return {
                "status": 400,
                "headers": {"Content-Type": "application/json"},
                "body": json.dumps(err_payload),
                "data": err_payload,
                "trace": "POST /items with non-object JSON -> store unchanged -> 400 Bad Request",
            }

        created_item = dict(parsed)
        target_store.append(created_item)
        return {
            "status": 201,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(created_item),
            "data": created_item,
            "trace": (
                f"POST /items parsed valid JSON object -> appended to store "
                f"(size now {len(target_store)}) -> 201 Created"
            ),
        }

    err_payload = {
        "error": f"Method {normalized_method} Not Allowed",
        "allowed": ["GET", "POST"],
    }
    return {
        "status": 405,
        "headers": {
            "Content-Type": "application/json",
            "Allow": "GET, POST",
        },
        "body": json.dumps(err_payload),
        "data": err_payload,
        "trace": (
            f"{normalized_method} /items not in allowed methods ['GET', 'POST'] -> "
            f"store unchanged -> 405 Method Not Allowed"
        ),
    }


def run_published_lesson_example() -> Dict[str, object]:
    """Execute the worked lesson walkthrough from initial state through 4 requests."""
    store: List[Dict[str, object]] = []

    post_res = handle_items_request(
        "POST", "/items", body='{"id": 1, "name": "notebook"}', store=store
    )
    get_res = handle_items_request("GET", "/items", store=store)
    bad_json_res = handle_items_request(
        "POST", "/items", body='{"id": 2, "name": ', store=store
    )
    bad_method_res = handle_items_request("DELETE", "/items", store=store)

    return {
        "final_store": list(store),
        "steps": [
            {"step": "POST valid item", "status": post_res["status"], "data": post_res["data"], "trace": post_res["trace"]},
            {"step": "GET items list", "status": get_res["status"], "data": get_res["data"], "trace": get_res["trace"]},
            {"step": "POST malformed JSON", "status": bad_json_res["status"], "data": bad_json_res["data"], "trace": bad_json_res["trace"]},
            {"step": "DELETE unsupported method", "status": bad_method_res["status"], "data": bad_method_res["data"], "trace": bad_method_res["trace"]},
        ],
    }


if __name__ == "__main__":
    walkthrough = run_published_lesson_example()
    for entry in walkthrough["steps"]:
        print(f"{entry['step']}: status={entry['status']} | {entry['trace']}")
