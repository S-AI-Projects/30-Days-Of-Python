"""Day 1 Applied Lab (R27-T030): Arithmetic Report Refactoring Lab.

Contract:
- Return `sum`, `difference`, and `product` for two integers.
- For `(7, 3)`, return `{"sum": 10, "difference": 4, "product": 21}`.
- For `(0, 0)`, all values are `0` (`{"sum": 0, "difference": 0, "product": 0}`).
- Contribution focus: Start from a working version, capture its behavior, and extract
  one clearly named responsibility (`validate_integer_pair`) without changing the contract.
"""

from __future__ import annotations

from typing import Dict, Tuple


def arithmetic_report_initial(a: int, b: int) -> Dict[str, int]:
    """Working pre-refactor version combining operand validation and arithmetic calculation."""
    if isinstance(a, bool) or isinstance(b, bool) or not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both operands must be integers")
    return {
        "sum": a + b,
        "difference": a - b,
        "product": a * b,
    }


def validate_integer_pair(a: int, b: int) -> Tuple[int, int]:
    """Extracted single responsibility: verify that `(a, b)` are true Python integers (excluding `bool`)."""
    if isinstance(a, bool) or isinstance(b, bool) or not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both operands must be integers")
    return a, b


def arithmetic_report(a: int, b: int) -> Dict[str, int]:
    """Refactored arithmetic report that delegates validation to `validate_integer_pair`."""
    left, right = validate_integer_pair(a, b)
    return {
        "sum": left + right,
        "difference": left - right,
        "product": left * right,
    }


if __name__ == "__main__":
    print("(7, 3) ->", arithmetic_report(7, 3))
    print("(0, 0) ->", arithmetic_report(0, 0))
