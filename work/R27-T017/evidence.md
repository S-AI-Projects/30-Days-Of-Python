# R27-T017 Check Evidence

## Test inputs and expected versus actual results

| Input | Expected | Actual |
|---|---|---|
| `" HELLO World "` | `"hello world"` | `"hello world"` |
| `"  HELLO   World  "` | `"hello world"` | `"hello world"` |
| `"Mixed\tCASE\nText"` (tab and newline) | `"mixed case text"` | `"mixed case text"` |

Idempotence check: normalizing each input a second time produced the same expected result.

## Worked trace

```text
Input: '  HELLO   World  '
After strip: 'HELLO   World'
After lowercase: 'hello   world'
After whitespace collapse: 'hello world'
Normalized again: 'hello world'
```

## Commands and tool versions

- Python: `Python 3.14.6`
- Git: `git version 2.55.0`
- Required check: `python3 -m unittest discover -s 14_Day_Higher_order_functions/applied-labs/r27-t017 -p "test_*.py"`
- Required check result: `Ran 3 tests ... OK` (11 assertions passed across fixture results, idempotence, and fresh-process example execution).
- Virtual-environment check: `/tmp/r27-t017-venv/bin/python -m unittest discover -s 14_Day_Higher_order_functions/applied-labs/r27-t017 -p "test_*.py"` — `Ran 3 tests ... OK`.
- Fresh-process example: `python3 14_Day_Higher_order_functions/applied-labs/r27-t017/example.py` — exited successfully and printed the worked trace above.
