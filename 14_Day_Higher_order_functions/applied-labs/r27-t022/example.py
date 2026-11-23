"""Day 14 Applied Lab (R27-T022): Function Composition Normalization Pipeline.

Contract:
- Compose `strip`, `lowercase`, and `whitespace-collapse` functions into a reusable
  normalization pipeline.
- `"  HELLO   World "` -> `"hello world"`.
- Idempotence boundary: applying normalization twice has the same result as once
  (`normalize(normalize(x)) == normalize(x)`).
- Boundary and invalid/empty-input behavior:
  - Empty strings `""` and whitespace-only strings `"   \t\n  "` normalize to `""`.
  - Non-string inputs (`None`, integers, lists) raise `TypeError`.
"""

from __future__ import annotations

from functools import reduce
from typing import Callable, Tuple

StringStep = Callable[[str], str]


def validate_string(text: str) -> str:
    """Ensure the input is a string before running string transformations."""
    if not isinstance(text, str):
        raise TypeError(f"Expected str input for normalization, got {type(text).__name__}")
    return text


def strip_edges(text: str) -> str:
    """Remove leading and trailing whitespace."""
    return validate_string(text).strip()


def to_lowercase(text: str) -> str:
    """Convert all characters to lowercase."""
    return validate_string(text).lower()


def collapse_whitespace(text: str) -> str:
    """Collapse any run of internal whitespace into a single ASCII space."""
    return " ".join(validate_string(text).split())


def compose_pipeline(*functions: StringStep) -> StringStep:
    """Return a reusable left-to-right composition of unary string functions."""
    def pipeline(initial_value: str) -> str:
        validated = validate_string(initial_value)
        return reduce(lambda acc, fn: fn(acc), functions, validated)

    return pipeline


normalize_text: StringStep = compose_pipeline(
    strip_edges,
    to_lowercase,
    collapse_whitespace,
)


def run_demo() -> Tuple[str, str, str]:
    """Run the contract fixture and boundary checks."""
    raw = "  HELLO   World "
    once = normalize_text(raw)
    twice = normalize_text(once)
    empty_boundary = normalize_text("   \t\n  ")
    return once, twice, empty_boundary


if __name__ == "__main__":
    first_pass, second_pass, empty_pass = run_demo()
    print(f"Once: {first_pass!r}")
    print(f"Twice (idempotent): {second_pass!r}")
    print(f"Whitespace-only boundary: {empty_pass!r}")
