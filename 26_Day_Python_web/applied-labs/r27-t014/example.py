"""A stateless JSON addition handler with a Flask adapter."""

from __future__ import annotations

from math import isfinite
from typing import TypeAlias, TypeGuard

ResponseBody: TypeAlias = dict[str, int | float | str]
HandlerResult: TypeAlias = tuple[int, ResponseBody]

_ERROR_BODY: ResponseBody = {
    "error": "Expected a JSON object with numeric 'a' and 'b'."
}


def handle_add(payload: object) -> HandlerResult:
    """Return a result determined only by this request's numeric ``a`` and ``b``."""
    if not isinstance(payload, dict):
        return 400, _ERROR_BODY.copy()

    a = payload.get("a")
    b = payload.get("b")
    if not _is_json_number(a) or not _is_json_number(b):
        return 400, _ERROR_BODY.copy()

    return 200, {"sum": a + b}


def _is_json_number(value: object) -> TypeGuard[int | float]:
    return (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and (not isinstance(value, float) or isfinite(value))
    )


def create_app():
    """Create the Flask app; import Flask only when the web adapter is used."""
    from flask import Flask, jsonify, request

    app = Flask(__name__)

    @app.post("/add")
    def add():
        status, body = handle_add(request.get_json(silent=True))
        return jsonify(body), status

    return app


if __name__ == "__main__":
    create_app().run()
