"""Day 19 Applied Lab (R27-T027): CSV Round Trip Failure-and-Recovery Lab.

Contract:
- Read and write UTF-8 CSV records using `csv.DictReader` / `csv.DictWriter`,
  preserving quoted commas.
- A record with `name="Ada, Jr."` and `score=7` survives write/read; empty data (`[]`)
  produces only the header (`"name,score\\n"`).
- Contribution focus: Demonstrate the stated error or empty state, then a successful
  recovery on the next valid input without restarting the example.
"""

from __future__ import annotations

import csv
import io
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Union

FIELDNAMES: Sequence[str] = ("name", "score")


def write_csv_records(
    records: Iterable[Dict[str, object]],
    target: Optional[Union[str, Path]] = None,
    fieldnames: Sequence[str] = FIELDNAMES,
) -> str:
    """Serialize `records` to UTF-8 CSV text (and optionally a UTF-8 file) with `csv.DictWriter`."""
    validated: List[Dict[str, object]] = []
    for index, record in enumerate(records):
        if not isinstance(record, dict):
            raise ValueError(f"Record {index} must be a dict")
        missing = [f for f in fieldnames if f not in record]
        if missing:
            raise ValueError(f"Record {index} missing required field(s): {missing}")
        try:
            score_int = int(record["score"])  # type: ignore[arg-type]
        except (TypeError, ValueError) as exc:
            raise ValueError(f"Record {index} has non-integer score: {record['score']!r}") from exc
        validated.append({"name": str(record["name"]), "score": score_int})

    buffer = io.StringIO()
    writer = csv.DictWriter(buffer, fieldnames=list(fieldnames), lineterminator="\n")
    writer.writeheader()
    for row in validated:
        writer.writerow(row)
    csv_text = buffer.getvalue()

    if target is not None:
        Path(target).write_text(csv_text, encoding="utf-8")

    return csv_text


def read_csv_records(
    source: Union[str, Path],
) -> List[Dict[str, object]]:
    """Read UTF-8 CSV records from a file path or raw CSV string using `csv.DictReader`."""
    if isinstance(source, Path) or (
        isinstance(source, str) and "\n" not in source and Path(source).exists()
    ):
        csv_text = Path(source).read_text(encoding="utf-8")
    else:
        csv_text = str(source)

    reader = csv.DictReader(io.StringIO(csv_text))
    records: List[Dict[str, object]] = []
    for line_no, row in enumerate(reader, start=2):
        if row.get("name") is None or row.get("score") is None:
            raise ValueError(f"Line {line_no}: missing required CSV columns")
        records.append({"name": row["name"], "score": int(row["score"])})
    return records


class CsvRoundTripSession:
    """Stateful CSV session demonstrating empty/error states followed by recovery."""

    def __init__(self, file_path: Optional[Union[str, Path]] = None) -> None:
        self.file_path = Path(file_path) if file_path is not None else None
        self.last_csv: str = ""
        self.last_records: List[Dict[str, object]] = []
        self.history: List[Dict[str, object]] = []

    def round_trip(
        self, records: Iterable[Dict[str, object]]
    ) -> Dict[str, object]:
        """Write and read back `records`, recovering cleanly after empty or invalid inputs."""
        try:
            csv_text = write_csv_records(records, target=self.file_path)
            read_source: Union[str, Path] = (
                self.file_path if self.file_path is not None else csv_text
            )
            parsed = read_csv_records(read_source)
            self.last_csv = csv_text
            self.last_records = parsed
            state = "empty_header_only" if len(parsed) == 0 else "ok"
            outcome: Dict[str, object] = {
                "status": state,
                "csv_text": csv_text,
                "records": parsed,
                "error": None,
            }
        except ValueError as exc:
            outcome = {
                "status": "error",
                "csv_text": self.last_csv,
                "records": list(self.last_records),
                "error": str(exc),
            }

        self.history.append(outcome)
        return outcome


def run_recovery_demo() -> List[Dict[str, object]]:
    """Run empty state + error state + valid recovery without restarting the session."""
    session = CsvRoundTripSession()
    # 1. Empty state -> produces only header
    session.round_trip([])
    # 2. Invalid record -> reports error without crashing session
    session.round_trip([{"name": "Broken", "score": "not-an-int"}])
    # 3. Recovery on next valid input -> quoted comma survives round trip
    session.round_trip([{"name": "Ada, Jr.", "score": 7}])
    return session.history


if __name__ == "__main__":
    for idx, step in enumerate(run_recovery_demo(), start=1):
        print(f"Step {idx} ({step['status']}): records={step['records']} csv={step['csv_text']!r}")
