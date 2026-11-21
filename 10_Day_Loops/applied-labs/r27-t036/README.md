# Applied Lab R27-T036: Run-Length Encoding Lab

## Objective
Convert consecutive repeated symbols into (symbol, count) pairs, refactored to delegate run extraction to `extract_run`.

## Contract
- `"aaabbc"` → `[("a", 3), ("b", 2), ("c", 1)]`
- `""` → `[]`
- `"aaa"` → `[("a", 3)]`

## Running Tests
Run test discovery from the repository root:
```bash
python3 -m unittest discover -s 10_Day_Loops/applied-labs/r27-t036 -p "test_*.py"
```
