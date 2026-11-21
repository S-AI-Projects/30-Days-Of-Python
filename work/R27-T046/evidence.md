# Evidence for R27-T046

## Inputs and expected results
Defaults {limit: 10, reverse: False}, allowed keys {limit, reverse}.
- no overrides -> expected {limit: 10, reverse: False}
- limit=3 -> expected {limit: 3, reverse: False}
- reverse=True -> expected {limit: 10, reverse: True}
- limit=3, reverse=True -> expected {limit: 3, reverse: True}
- limt=3 (typo) -> expected ValueError "Unknown option(s): limt"
- revers=True, limt=3 -> expected ValueError "Unknown option(s): limt, revers"
- an override named "defaults" or "allowed" -> expected ValueError (unknown key), not a name clash
- Original version and refactored version -> expected identical on every row above
- merge_options -> expected to call reject_unknown_keys; the original version does not

## Actual results
- 8 tests ran, all OK (see pass-result.txt, exit code 0)
- Example output saved in example-output.txt

## Tool versions
Python 3.14.2
## Command
python3 -m unittest discover -s 17_Day_Exception_handling/applied-labs/r27-t046 -p "test_*.py"