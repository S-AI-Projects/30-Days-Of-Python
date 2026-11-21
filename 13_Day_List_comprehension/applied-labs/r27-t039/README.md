# Applied Lab R27-T039: Filtered Comprehension Lab

## Objective
Build a mapping from even integers to their squares without modifying the input, with input-scale operation count verification.

## Contract
- Fixture: `[-2, -1, 0, 1, 2]` → `{-2: 4, 0: 0, 2: 4}`
- Odd-only: `[1, 3, 5]` → `{}`
- No input mutation.
- Three bounded input scales (10, 50, 100) verified with operation counts.

## Running Tests
Run test discovery from the repository root:
```bash
python3 -m unittest discover -s 13_Day_List_comprehension/applied-labs/r27-t039 -p "test_*.py"
```
