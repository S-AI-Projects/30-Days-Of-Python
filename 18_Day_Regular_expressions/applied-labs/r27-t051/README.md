# R27-T051: Regular-expression groups and date validation

`extract_date(text)` extracts a date-like token `YYYY-MM-DD` using named groups and validates the calendar date separately.

- Token extraction uses named regex groups: `(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})`.
- Calendar validation is handled separately via `validate_date(year, month, day)`.
- `extract_date("2024-02-29")` is accepted and returns `"2024-02-29"`.
- `extract_date("2023-02-29")` matches the regex pattern but is rejected with `ValueError`.
- Text without a date token returns `None`.

## Run the tests

From the repository root:

    python3 -m unittest discover -s 18_Day_Regular_expressions/applied-labs/r27-t051 -p "test_*.py"
