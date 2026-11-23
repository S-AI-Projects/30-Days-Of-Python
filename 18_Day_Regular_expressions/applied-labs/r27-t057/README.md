# R27-T057: Regular-expression groups and date validation (worked explanation)

`extract_date(text)` extracts a date-like token `YYYY-MM-DD` using named groups and validates the actual calendar date separately.

## Contract and Fixtures

- `extract_date("2024-02-29")` is accepted and returns `"2024-02-29"`.
- `extract_date("2023-02-29")` matches the pattern but is rejected with `ValueError` (2023 is not a leap year).
- Text without a token returns `None`.

## Worked Explanation: Input -> Intermediate State -> Output

1. **Input**: Raw text containing potential date token (e.g., `"Meeting on 2024-02-29"`).
2. **Intermediate State**:
   - Named group regex match: `(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})`
   - Named capture dictionary: `{'year': '2024', 'month': '02', 'day': '29'}`
   - Integer conversion: `year=2024, month=2, day=29`
   - Separate calendar validation: `validate_date(year, month, day)` via `datetime.date`
3. **Output**: Verified date token `"2024-02-29"`.

## Run the tests

From the repository root:

    python3 -m unittest discover -s 18_Day_Regular_expressions/applied-labs/r27-t057 -p "test_*.py"
