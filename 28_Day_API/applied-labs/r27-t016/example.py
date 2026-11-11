"""A small in-memory /items API implemented with the Python standard library."""

import json
from http import HTTPStatus
from wsgiref.simple_server import make_server


class InMemoryItemStore:
    """Keep items in memory for the lifetime of the application."""

    def __init__(self):
        self._items = []

    def create(self, name):
        item = {"id": len(self._items) + 1, "name": name}
        self._items.append(item)
        return item

    def list(self):
        return [item.copy() for item in self._items]


def parse_item_payload(raw_body):
    """Decode and validate the JSON body for a new item."""
    try:
        item_data = json.loads(raw_body)
    except (json.JSONDecodeError, UnicodeDecodeError) as error:
        raise ValueError("Malformed JSON") from error

    if (
        not isinstance(item_data, dict)
        or not isinstance(item_data.get("name"), str)
        or not item_data["name"].strip()
    ):
        raise ValueError("Item must have a non-empty name")

    return {"name": item_data["name"].strip()}


def create_app(store):
    """Create a WSGI app that uses the supplied item store."""

    def app(environ, start_response):
        method = environ["REQUEST_METHOD"]
        path = environ.get("PATH_INFO", "/")

        if method not in {"GET", "POST"}:
            status = HTTPStatus.METHOD_NOT_ALLOWED
            headers = [("Allow", "GET, POST")]
            body = {"error": "Method not allowed"}
        elif path != "/items":
            status = HTTPStatus.NOT_FOUND
            headers = []
            body = {"error": "Not found"}
        elif method == "GET":
            status = HTTPStatus.OK
            headers = []
            body = store.list()
        else:
            length = int(environ.get("CONTENT_LENGTH") or 0)
            raw_body = environ["wsgi.input"].read(length)
            try:
                item_data = parse_item_payload(raw_body)
            except ValueError as error:
                status = HTTPStatus.BAD_REQUEST
                headers = []
                body = {"error": str(error)}
            else:
                item = store.create(item_data["name"])
                status = HTTPStatus.CREATED
                headers = [("Location", f"/items/{item['id']}")]
                body = item

        encoded_body = json.dumps(body).encode("utf-8")
        response_headers = [
            ("Content-Type", "application/json; charset=utf-8"),
            ("Content-Length", str(len(encoded_body))),
            *headers,
        ]
        start_response(
            f"{status.value} {status.phrase}",
            response_headers,
        )
        return [encoded_body]

    return app


if __name__ == "__main__":
    with make_server("127.0.0.1", 8000, create_app(InMemoryItemStore())) as server:
        print("Serving http://127.0.0.1:8000/items")
        server.serve_forever()
