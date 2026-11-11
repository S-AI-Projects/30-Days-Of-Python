# JSON sum request handler

This added activity applies the Day 26 Flask request-handler topic. Its pure
`handle_add` function returns `(200, {"sum": a + b})` for JSON-number inputs
`a` and `b`; missing values, strings, booleans, and non-finite floats return
status 400. The Flask `POST /add` adapter uses the same handler.

The invariant is that each response depends only on the current request: valid
numeric inputs produce their sum, invalid inputs produce 400, and an earlier
request cannot change a later result. The tests check this across a valid,
invalid, then valid request sequence, as well as against every fixture.

Activate a Python virtual environment and install the declared Flask
dependency:

```sh
python3 -m pip install -r 26_Day_Python_web/applied-labs/r27-t014/requirements.txt
```

Run the tests from the repository root:

```sh
python3 -m unittest discover -s 26_Day_Python_web/applied-labs/r27-t014 -p "test_*.py"
```

Start the Flask adapter with:

```sh
python3 26_Day_Python_web/applied-labs/r27-t014/example.py
```

Send a JSON `POST` to `http://127.0.0.1:5000/add`, for example
`{"a":2,"b":3}`. The response is status 200 with `{"sum":5}`. Omitting `b`
or sending a string as either operand returns status 400.
