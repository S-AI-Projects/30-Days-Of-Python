# R27-T052: Missing-value summary (boundary-focused)

`missing_value_summary(observations)` calculates `count`, `missing_count`, `mean`, and `median` for numeric observations containing `None` values.

## Contract and Boundary Conditions

- `[1, None, 3, 5]` returns `count=3, missing_count=1, mean=3, median=3`.
- **All-missing boundary**: `[None, None]` returns `count=0, missing_count=2, mean=None, median=None`.
- **Empty-input boundary**: `[]` returns `count=0, missing_count=0, mean=None, median=None`.
- When non-missing `count == 0`, `mean` and `median` evaluate to `None` (null) because dividing by zero or taking the median of an empty set is undefined.
- Invalid non-iterable input or unsupported non-numeric elements raise `TypeError`.

## Run the tests

From the repository root:

    python3 -m unittest discover -s 24_Day_Statistics/applied-labs/r27-t052 -p "test_*.py"

