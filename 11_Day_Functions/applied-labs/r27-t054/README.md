# R27-T054: Price function

`price(quantity, *, unit_price, discount=0)` returns the total price.

- `quantity` is positional; `unit_price` and `discount` are keyword-only.
- `price(3, unit_price=10, discount=0.1)` returns 27.
- `price(0, unit_price=10, discount=0.1)` returns 0.
- A negative quantity raises `ValueError`.

## Refactor

The negative-quantity check was extracted into `validate_quantity()`.
The behavior of `price()` is unchanged.

## Run the tests

From the repository root:

    python3 -m unittest discover -s 11_Day_Functions/applied-labs/r27-t054 -p "test_*.py"