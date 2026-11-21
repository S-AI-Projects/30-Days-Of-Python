# Applied Lab R27-T038: Keyword Merging (Failure-and-Recovery Lab)

## Objective
Merge default keywords with overrides using an explicit allowed-key set, demonstrating an error followed by successful recovery without restarting.

## Contract
- Defaults: `{"limit": 10, "reverse": False}`
- Override `limit=3` → `{"limit": 3, "reverse": False}`
- Unknown key `limt` → rejected with `KeyError`.
- Recovery: after failure, subsequent valid input succeeds in the same session.

## Running Tests
Run test discovery from the repository root:
```bash
python3 -m unittest discover -s 17_Day_Exception_handling/applied-labs/r27-t038 -p "test_*.py"
```
