# Day 19 Applied Lab (`R27-T027`): UTF-8 CSV Round Trip Failure-and-Recovery Lab

## Overview
This applied lab uses `csv.DictWriter` and `csv.DictReader` to write and read UTF-8 CSV records containing quoted commas, and demonstrates handling an empty state (`[]` producing only the header `name,score\n`) and a validation failure before recovering cleanly on the next valid input (`{"name": "Ada, Jr.", "score": 7}`) in the same session without restarting.

## Contract Fixtures & Recovery Flow
1. **Empty State**: `write_csv_records([])` outputs `"name,score\n"` and reads back as `[]`.
2. **Error State**: Passing a malformed score (`{"name": "Broken", "score": "not-an-int"}`) is caught by `CsvRoundTripSession.round_trip`, recording `status="error"` while keeping the session alive.
3. **Recovery State**: Passing `[{"name": "Ada, Jr.", "score": 7}]` on the next call writes `"name,score\n\"Ada, Jr.\",7\n"` and reads back `[{"name": "Ada, Jr.", "score": 7}]`.

## Running the Example and Tests
From the repository root:

```bash
python3 19_Day_File_handling/applied-labs/r27-t027/example.py
python3 -m unittest discover -s 19_Day_File_handling/applied-labs/r27-t027 -p "test_*.py"
```
