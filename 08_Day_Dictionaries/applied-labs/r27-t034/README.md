# Applied Lab R27-T034: Inventory Mapping – State/Invariant Lab

## Objective
Apply signed stock changes to an inventory dictionary while preserving the invariant that no stock value may become negative.

## Contract
- Fixture: {tea:3} plus {tea:-2, coffee:4} yields {tea:1, coffee:4}.
- Invariant Violation: {tea:-4} on {tea:3} raises `ValueError` and leaves the original unchanged.
- Sequence Verification: Invariant `(all(value >= 0))` is inspected and preserved across multiple sequential transactions.

## Running Tests
Run test discovery from repository root:
```bash
python3 -m unittest discover -s 08_Day_Dictionaries/applied-labs/r27-t034 -p "test_*.py"
@``@
