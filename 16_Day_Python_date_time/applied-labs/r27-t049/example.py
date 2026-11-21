from datetime import datetime, timezone


def parse_timestamp(text):
    """Parse an ISO-8601 timestamp that has an offset; return it in UTC.

    A timestamp WITHOUT an offset (like '2024-01-01T10:00:00') is rejected
    with ValueError, because we cannot know which time zone it means.
    """
    parsed = datetime.fromisoformat(text)  # raises ValueError for bad text
    if parsed.utcoffset() is None:  # decisive check: no offset -> reject
        raise ValueError(f"Timestamp has no offset: {text!r}")
    return parsed.astimezone(timezone.utc)


def elapsed_seconds(start, end):
    """Seconds from start to end, both converted to UTC first."""
    return (parse_timestamp(end) - parse_timestamp(start)).total_seconds()


def elapsed_many(pairs):
    """Compute elapsed seconds for many (start, end) pairs.

    Returns (results, parse_calls). parse_calls counts how many times a
    timestamp was parsed, so we can report the amount of work done
    instead of measuring speed.
    """
    results = []
    parse_calls = 0
    for start, end in pairs:
        start_utc = parse_timestamp(start)
        end_utc = parse_timestamp(end)
        parse_calls += 2
        results.append((end_utc - start_utc).total_seconds())
    return results, parse_calls


if __name__ == "__main__":
    print(elapsed_seconds("2024-01-01T10:00:00+05:30", "2024-01-01T05:00:00+00:00"))