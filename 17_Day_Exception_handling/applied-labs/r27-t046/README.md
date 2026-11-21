# Applied Lab R27-T046: Merge Defaults with Allowed Keyword Overrides

Added activity (not an original numbered exercise).

Merges a defaults dictionary with keyword overrides, using an explicit
allowed-key set. An override key that is not in the set is rejected with
`ValueError`.

- Defaults: `{"limit": 10, "reverse": False}`, allowed keys: `{"limit", "reverse"}`
- Input: override `limit=3`
- Expected: `{"limit": 3, "reverse": False}`
- Input: override `limt=3` (a typo)
- Expected: `ValueError: Unknown option(s): limt`

The defaults and the allowed set are never modified.

## Refactoring: extract one responsibility

1. **Working version.** `merge_options_original` does two jobs in one
   function: it checks the keys and it merges.
2. **Capture its behavior.** The `CAPTURED` table in `test_example.py`
   records what the working version returns or raises for 8 inputs.
3. **Extract one responsibility.** The key check moves into
   `reject_unknown_keys`, a function with one clear name and one job.
   `merge_options` calls it and then merges.
4. **Prove the contract did not change.** The tests run both versions
   against the same `CAPTURED` table, and both must match every row.

`defaults` and `allowed` are positional-only (the `/` in the signature), so
an override literally named `defaults` or `allowed` is rejected as an
unknown key instead of clashing with the parameter names. This needs
Python 3.8 or newer.

## Run the tests

From the repository root:

    python3 -m unittest discover -s 17_Day_Exception_handling/applied-labs/r27-t046 -p "test_*.py"

## Run the example

    python3 17_Day_Exception_handling/applied-labs/r27-t046/example.py