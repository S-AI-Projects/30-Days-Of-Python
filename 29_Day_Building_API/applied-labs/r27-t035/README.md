# Applied Lab R27-T035: Installable Mini-Package (Deterministic Fixture Lab)

## Objective
Provide an installable word-count function and CLI entry point with deterministic fixtures and isolated test agreement.

## Contract
- Function `count_words("a b a")` returns `3`.
- CLI counts `"a b a"` as 3 words and exits with code `0`.
- Supports `--help`.
- Demonstrates deterministic fixture execution across isolated runs and injected storage.

## Running Tests
Run test discovery from the repository root:
```bash
python3 -m unittest discover -s 29_Day_Building_API/applied-labs/r27-t035 -p "test_*.py"
```
