# Applied Lab R27-T050: Signed Stock Changes

Added activity (not an original numbered exercise).

Applies signed stock changes to a dictionary and rejects any change that
would make a stock negative. The original dictionary is never modified.

- Input: `{"tea": 3}` plus `{"tea": -2, "coffee": 4}`
- Expected: `{"tea": 1, "coffee": 4}`
- Input: `{"tea": 3}` plus `{"tea": -4}`
- Expected: `ValueError`, original stays `{"tea": 3}`

Run the tests from the repository root:

    python3 -m unittest discover -s 08_Day_Dictionaries/applied-labs/r27-t050 -p "test_*.py"

Regression focus: the condition `< 0` is the decisive check. The test
`test_exactly_zero_is_allowed` fails if it is mutated to `<= 0`.