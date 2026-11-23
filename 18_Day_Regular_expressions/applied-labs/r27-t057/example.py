"""R27-T057: Regular-expression groups with separate calendar validation and worked explanation."""

import datetime
import re

DATE_PATTERN = re.compile(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})")


def validate_date(year, month, day):
    """Validate calendar date separately from regex pattern matching."""
    return datetime.date(year, month, day)


def extract_date(text):
    """Extract a YYYY-MM-DD token using named groups and validate calendar date.

    - 2024-02-29 is accepted
    - 2023-02-29 is rejected despite matching pattern (raises ValueError)
    - text without a token gives None
    """
    match = DATE_PATTERN.search(text)
    if not match:
        return None

    year = int(match.group("year"))
    month = int(match.group("month"))
    day = int(match.group("day"))

    validate_date(year, month, day)
    return match.group(0)


def explain_date_extraction(text):
    """Worked explanation tracing input -> intermediate state -> output.

    1. Input: raw text string.
    2. Intermediate state:
       - token: regex match substring
       - groups: named group dictionary {'year': ..., 'month': ..., 'day': ...}
       - parsed_date: integer tuple (year, month, day)
       - is_valid_calendar: boolean validation flag
    3. Output: extracted date token string, or None if no token found.
    """
    match = DATE_PATTERN.search(text)
    if not match:
        return {
            "input": text,
            "intermediate": {
                "matched": False,
                "token": None,
                "groups": None,
                "calendar_valid": False,
            },
            "output": None,
        }

    raw_token = match.group(0)
    groups = match.groupdict()
    year = int(groups["year"])
    month = int(groups["month"])
    day = int(groups["day"])

    is_valid = False
    try:
        validate_date(year, month, day)
        is_valid = True
    except ValueError:
        is_valid = False

    return {
        "input": text,
        "intermediate": {
            "matched": True,
            "token": raw_token,
            "groups": groups,
            "parsed_ints": {"year": year, "month": month, "day": day},
            "calendar_valid": is_valid,
        },
        "output": raw_token if is_valid else "ValueError",
    }


if __name__ == "__main__":
    print("extract_date('2024-02-29'):", extract_date("2024-02-29"))
    try:
        extract_date("2023-02-29")
    except ValueError as e:
        print("extract_date('2023-02-29'): Rejected with ValueError:", e)
    print("extract_date('no date here'):", extract_date("no date here"))

    print("\nWorked explanation for 'Event on 2024-02-29 confirmed':")
    explanation = explain_date_extraction("Event on 2024-02-29 confirmed")
    print("  Input:       ", explanation["input"])
    print("  Intermediate:", explanation["intermediate"])
    print("  Output:      ", explanation["output"])
