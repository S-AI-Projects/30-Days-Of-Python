"""
Applied Lab R27-T031: Timezone-aware ISO-8601 timestamp parsing and elapsed seconds calculation.
"""
from datetime import datetime, timezone


def parse_iso_aware(timestamp_str: str) -> datetime:
    """
    Parses an ISO-8601 string and ensures it has a timezone offset.
    Raises ValueError if the string is naive (lacks timezone offset).
    """
    dt = datetime.fromisoformat(timestamp_str)
    if dt.tzinfo is None or dt.tzinfo.utcoffset(dt) is None:
        raise ValueError(f"Timestamp '{timestamp_str}' lacks a timezone offset.")
    return dt


def elapsed_seconds_utc(ts1_str: str, ts2_str: str) -> float:
    """
    Calculates the absolute elapsed difference in seconds between two ISO-8601
    timestamp strings converted to UTC.
    """
    dt1 = parse_iso_aware(ts1_str).astimezone(timezone.utc)
    dt2 = parse_iso_aware(ts2_str).astimezone(timezone.utc)
    return abs((dt2 - dt1).total_seconds())


if __name__ == "__main__":
    t1 = "2024-01-01T10:00:00+05:30"
    t2 = "2024-01-01T05:00:00+00:00"
    diff = elapsed_seconds_utc(t1, t2)
    print(f"Difference between {t1} and {t2}: {diff} seconds")