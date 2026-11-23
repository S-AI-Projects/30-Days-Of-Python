"""Day 30 Capstone Applied Lab (R27-T021): Local CSV Expense Summarizer.

Contract:
- Parse CSV expense lines of the form `<category>,<amount>`.
- Validate each row: report negative expenses (and malformed rows) by 1-based line number.
- Aggregate valid non-negative expenses into category totals formatted to two decimal places
  (and numeric totals), so `food,12.50`, `food,7.50`, and `travel,5.00` yield
  `food=20.00` and `travel=5.00`.
"""

from __future__ import annotations

import csv
import io
from decimal import Decimal, InvalidOperation
from typing import Dict, Iterable, List, Tuple, Union


def summarize_expenses(
    csv_source: Union[str, Iterable[str]],
) -> Dict[str, object]:
    """Parse, validate, and summarize local CSV expense rows by category.

    Args:
        csv_source: A multi-line CSV string or an iterable of CSV line strings.

    Returns:
        A dictionary containing:
        - `totals`: dict mapping category name to float total (rounded to 2 decimal places)
        - `formatted_totals`: dict mapping category name to `"%.2f"` string (e.g. `"20.00"`)
        - `summary`: formatted summary string (e.g. `"food=20.00, travel=5.00"`)
        - `errors`: list of dicts `{"line": <1-based line int>, "raw": <str>, "reason": <str>}`
        - `error_lines`: list of 1-based line numbers that failed validation
    """
    if isinstance(csv_source, str):
        lines = csv_source.splitlines()
    else:
        lines = list(csv_source)

    category_decimals: Dict[str, Decimal] = {}
    errors: List[Dict[str, object]] = []

    for line_number, raw_line in enumerate(lines, start=1):
        stripped = raw_line.strip()
        if not stripped:
            continue

        parsed_rows = list(csv.reader(io.StringIO(stripped)))
        if not parsed_rows or len(parsed_rows[0]) != 2:
            errors.append(
                {
                    "line": line_number,
                    "raw": raw_line,
                    "reason": f"Line {line_number}: expected '<category>,<amount>'",
                }
            )
            continue

        category_raw, amount_raw = parsed_rows[0]
        category = category_raw.strip()
        if not category:
            errors.append(
                {
                    "line": line_number,
                    "raw": raw_line,
                    "reason": f"Line {line_number}: missing category",
                }
            )
            continue

        try:
            amount = Decimal(amount_raw.strip())
        except InvalidOperation:
            errors.append(
                {
                    "line": line_number,
                    "raw": raw_line,
                    "reason": f"Line {line_number}: invalid numeric amount '{amount_raw.strip()}'",
                }
            )
            continue

        if amount < Decimal("0"):
            errors.append(
                {
                    "line": line_number,
                    "raw": raw_line,
                    "reason": f"Line {line_number}: negative expense ({amount:.2f}) is invalid",
                }
            )
            continue

        category_decimals[category] = (
            category_decimals.get(category, Decimal("0.00")) + amount
        )

    formatted_totals: Dict[str, str] = {
        cat: f"{total:.2f}" for cat, total in category_decimals.items()
    }
    totals: Dict[str, float] = {
        cat: float(round(total, 2)) for cat, total in category_decimals.items()
    }
    summary = ", ".join(f"{cat}={val}" for cat, val in formatted_totals.items())
    error_lines = [int(err["line"]) for err in errors]

    return {
        "totals": totals,
        "formatted_totals": formatted_totals,
        "summary": summary,
        "errors": errors,
        "error_lines": error_lines,
    }


def run_demo() -> Tuple[Dict[str, object], Dict[str, object]]:
    """Run the smallest useful complete example from the contract."""
    valid_csv = "food,12.50\nfood,7.50\ntravel,5.00"
    mixed_csv = "food,12.50\nfood,-3.00\nfood,7.50\ntravel,5.00\nlodging,-10.25"
    return summarize_expenses(valid_csv), summarize_expenses(mixed_csv)


if __name__ == "__main__":
    clean_result, mixed_result = run_demo()
    print("Clean fixture summary:", clean_result["summary"])
    print("Mixed fixture summary:", mixed_result["summary"])
    print("Reported invalid lines:", mixed_result["error_lines"])
