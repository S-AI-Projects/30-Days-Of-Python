import datetime
import re

DATE_PATTERN = re.compile(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})")


def validate_date(year, month, day):
    """Validate calendar date separately from regex pattern matching."""
    return datetime.date(year, month, day)


def extract_date(text):
    """Extract a YYYY-MM-DD token using named groups and validate calendar date."""
    match = DATE_PATTERN.search(text)
    if not match:
        return None

    year = int(match.group("year"))
    month = int(match.group("month"))
    day = int(match.group("day"))

    validate_date(year, month, day)
    return match.group(0)


if __name__ == "__main__":
    print(extract_date("2024-02-29"))
    try:
        extract_date("2023-02-29")
    except ValueError as e:
        print("Rejected:", e)
    print(extract_date("no date here"))
