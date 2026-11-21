import csv
import io

# Repeatable local fixtures: the data lives here, not in a file or on a network.
FIXTURE = "category,amount\nA,2\nA,3\nB,4\n"
BAD_FIXTURE = "category,amount\nA,2\nA,oops\nB\nB,4\n,7\n"


def group_csv(lines):
    """Group CSV rows by category and calculate count and sum.

    `lines` is any iterable of text lines (an open file, io.StringIO, or a
    plain list). The source is passed IN, so nothing here opens files,
    reads the clock, or uses the network.

    The first line is a header: category,amount. Line numbers count the
    header as line 1, so the first data row is line 2.

    Returns (groups, errors):
    - groups: {category: {"count": n, "sum": total}}
    - errors: [(line_number, reason)] for every malformed row.
      A malformed row is never silently dropped.
    """
    reader = csv.reader(lines)
    next(reader, None)  # skip the header row
    groups = {}
    errors = []
    for row in reader:
        line_no = reader.line_num
        if len(row) != 2:
            errors.append((line_no, f"expected 2 fields, got {len(row)}"))
            continue
        category, amount_text = row[0].strip(), row[1].strip()
        if not category:
            errors.append((line_no, "empty category"))
            continue
        try:
            amount = int(amount_text)
        except ValueError:  # decisive: only bad numbers are caught here
            errors.append((line_no, f"amount is not an integer: {amount_text!r}"))
            continue
        entry = groups.setdefault(category, {"count": 0, "sum": 0})
        entry["count"] += 1
        entry["sum"] += amount
    return groups, errors


def report(lines):
    """Text report. Categories are sorted so the output is always the same."""
    groups, errors = group_csv(lines)
    out = []
    for category in sorted(groups):
        entry = groups[category]
        out.append(f"{category}: count={entry['count']} sum={entry['sum']}")
    for line_no, reason in errors:
        out.append(f"line {line_no}: {reason}")
    return out


if __name__ == "__main__":
    for line in report(io.StringIO(FIXTURE)):
        print(line)
    print("---")
    for line in report(io.StringIO(BAD_FIXTURE)):
        print(line)
        