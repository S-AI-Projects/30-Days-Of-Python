# Word Counter Applied Lab

This added activity practices string handling by counting lowercase words,
ignoring punctuation at word boundaries, and retaining apostrophes inside
words. Run the example with `python3 example.py`; run its reference comparisons
with:

```sh
python3 -m unittest discover -s 04_Day_Strings/applied-labs/r27-t013 -p "test_*.py"
```

The independent expected-result table in `test_example.py` covers these inputs:

| Input | Expected result |
|---|---|
| `Tea, tea! isn't coffee.` | `{"tea": 2, "isn't": 1, "coffee": 1}` |
| empty string | `{}` |
| `'TEA' tea!` | `{"tea": 2}` |
| `ISN'T isn't` | `{"isn't": 2}` |
| `... !!!` | `{}` |
