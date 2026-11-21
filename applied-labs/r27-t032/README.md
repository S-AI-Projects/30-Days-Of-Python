# Applied Lab R27-T032: Arithmetic Report – Boundary-Focused Lab

## Objective
Calculate sum, difference, and product for two integers with focus on boundary conditions and invalid input handling.

## Contract
- Fixture +7, 3): returns `{'sum': 10, 'difference': 4, 'product': 21}`.
- Boundary (0, 0): returns `['sum': 0, 'difference': 0, 'product': 0}`.
- Rejects empty/None inputs with `ValueError`.
- Rejects non-integer (float, bool, str) inputs with `TypeError`.

## Running Tests
Run test discovery from repository root:
```bash
python3 -m unittest discover -s ./applied-labs/r27-t032 -p "test_*.py"
@``@
