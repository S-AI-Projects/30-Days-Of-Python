# Added activity: in-memory `/items` endpoint

This supplemental lab applies the lesson's HTTP methods, JSON message bodies, and
status codes. It does not add or replace an original numbered exercise.

Run the API locally with `python3 28_Day_API/applied-labs/r27-t016/example.py`.
It listens only on `127.0.0.1:8000` and stores items in memory.

Send `POST /items` with `{"name": "notebook"}` to receive `201 Created` and
`{"id": 1, "name": "notebook"}`. Then `GET /items` returns
`200 OK` and `[{"id": 1, "name": "notebook"}]`. Malformed JSON returns `400
Bad Request`; a method other than GET or POST returns `405 Method Not Allowed`.

The app receives its store as a dependency. Its initial working implementation
decoded and validated the POST JSON in the request branch; that behavior was
captured by the endpoint tests before the decoding and validation were extracted
into the clearly named `parse_item_payload` responsibility.

Run the endpoint tests from the repository root:

```sh
python3 -m unittest discover -s 28_Day_API/applied-labs/r27-t016 -p "test_*.py"
```
