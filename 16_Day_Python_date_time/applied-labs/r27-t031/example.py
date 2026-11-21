from datetime import datetime, timezone

def parse_iso_offset(ts_str: str) -> datetime:
    """
    Parse an ISO-8601 timestamp string and require a timezone offset.
    Raises ValueError if naive (no timezone offset).
    """
    dt = datetime.fromisoformat(ts_str)
    if dt.tzinfo is None or dt.utcoffset() is None:
        raise ValueError(f"Timestamp '{ts_str}' lacks a required timezone offset.")
    return dt

def elapsed_seconds_utc(ts1: str, ts2: str) -> float:
    """
    Calculate elapsed seconds between two ISO-8601 timestamps normalized to UTC.
    """
    dt1 = parse_iso_offset(ts1).astimezone(timezone.utc)
    dt2 = parse_iso_offset(ts2).astimezone(timezone.utc)
    return abs((dt2 - dt1).total_seconds())

if __name__ == "__main__":
    t1 = "2024-01-01T10:00:00+05:30"
    t2 = "2024-01-01T05:00:00+00:00"
    print(f"Elapsed seconds: {elapsed_seconds_utc(t1, t2)}")
