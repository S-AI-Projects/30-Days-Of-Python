# Applied Lab R27-T033: Discount Calculation – Reference Comparison Lab

## Objective
Calculate percentage discounts using Python's `Decimal` module and round currency to two decimal places using `ROUND_HALF_UP`.

## Contract
- Fixture: 100.00 at 15% produces 85.00.
- Boundary: 100.00 at 0% returns 100.00 unchanged.
- Boundary Validation: Percentages outside 0..100 (e.g. -1, 101) raise `ValueError`.
- Reference Comparison: Outputs are validated against an independent reference implementation.

## Running Tests
Run test discovery from repository root:
```bash
python3 -m unittest discover -s 03_Day_Operators/applied-labs/r27-t033 -p "test_*.py"
@``@
