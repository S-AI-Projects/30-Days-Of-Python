# Day 30 Applied Lab (`R27-T021`): Capstone Local Expense Summarizer

## Overview
This applied lab combines CSV parsing, line-by-line validation, and category aggregation into a small, self-contained expense summarizer using only the Python standard library.

## Contract
- **Input**: CSV rows in `<category>,<amount>` format.
- **Fixture**:
  ```text
  food,12.50
  food,7.50
  travel,5.00
  ```
- **Expected Output**:
  - Category totals: `food=20.00` and `travel=5.00` (`{"food": "20.00", "travel": "5.00"}`).
  - Any negative expense (e.g. `food,-3.00` on line 2) is rejected and reported by its 1-based line number in `errors` and `error_lines`.

## Running the Example and Tests
From the repository root:

```bash
python3 30_Day_Conclusions/applied-labs/r27-t021/example.py
python3 -m unittest discover -s 30_Day_Conclusions/applied-labs/r27-t021 -p "test_*.py"
```
