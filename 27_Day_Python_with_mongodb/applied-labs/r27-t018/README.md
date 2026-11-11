# R27-T018: In-memory document store

This added activity demonstrates the document-store operations from Day 27 with a small `DocumentStore` interface and an in-memory adapter. It does **not** connect to MongoDB, use PyMongo, or persist data.

Run the example in a fresh Python process:

```sh
python3 27_Day_Python_with_mongodb/applied-labs/r27-t018/example.py
```

The example shows the initial empty lookup, inserts `{"id": 1, "name": "Ada"}`, and then rejects a second document with the same ID. It continues in the same process: the next valid input updates the name to Grace, and finding ID 1 returns `{"id": 1, "name": "Grace"}`.

Run the tests from the repository root:

```sh
python3 -m unittest discover -s 27_Day_Python_with_mongodb/applied-labs/r27-t018 -p "test_*.py"
```
