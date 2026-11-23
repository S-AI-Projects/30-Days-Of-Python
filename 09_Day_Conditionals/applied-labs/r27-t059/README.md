# R27-T059: Shipping bands (state and invariant lab)

`calculate_shipping(total)` computes shipping cost with banded conditional logic, and `ShoppingCart` models state transitions while verifying the state/invariant connecting input/state to output.

## Contract and Fixtures

- `total >= 100` -> `0` (free shipping, e.g. `100 -> 0`)
- `50 <= total < 100` -> `5` (e.g. `50 -> 5`, `99.99 -> 5`)
- `0 <= total < 50` -> `10` (e.g. `49.99 -> 10`)
- `total < 0` -> raises `ValueError` (e.g. `-1` raises `ValueError`)

## State and Invariant Verification

The `ShoppingCart` model ensures that across every operation in a sequence:
1. Non-negative total invariant: `total >= 0`.
2. Band mapping invariant: shipping rate strictly matches the conditional bracket.
3. Total composition invariant: `grand_total == total + shipping`.

## Run the tests

From the repository root:

    python3 -m unittest discover -s 09_Day_Conditionals/applied-labs/r27-t059 -p "test_*.py"
