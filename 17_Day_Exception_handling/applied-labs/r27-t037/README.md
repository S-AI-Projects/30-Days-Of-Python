# Applied Lab R27-T037: Keyword Merging Lab

## Objective
Merge default keywords with overrides using an explicit allowed-key set, rejecting unknown keys with `KeyError`.

## Contract
- Defaults: `{"limit": 10, "reverse": False}`
- Override `limit=3` → `{"limit": 3, "reverse": False}`
- Unknown key `limt` → raises `KeyError`.

## Running Tests
Run test discovery from the repository root:
```bash
python3 -m unittest discover -s 17_Day_Exception_handling/applied-labs/r27-t037 -p "test_*.py"
```
