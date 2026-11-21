# Evidence for R27-T043

## Inputs and expected results
Expected-result table (worked out by hand), text -> words, distinct:
- "one two two" -> 3, 2
- "" -> 0, 0
- "   " (spaces only) -> 0, 0
- "one" -> 1, 1
- "a a a" -> 3, 1
- "One one" (case-sensitive) -> 2, 2
- "  one   two\ttwo\n" -> 3, 2
- "a\nb\nc" -> 3, 3
- Reference implementation (no split, no set) -> expected to match the table too
- All 5461 strings of length 0 to 6 over the characters a, b, space, tab -> expected: text_stats and the reference agree on every one
- requirements.txt -> expected to declare no dependencies
- Import with user-site packages disabled (python -s) -> expected to succeed

## Actual results
- Normal run: 9 tests ran, all OK (see pass-result.txt, exit code 0), 5461 strings compared and all agree
- Clean virtual environment run: 9 tests ran, all OK (see venv-result.txt, exit code 0)

## Tool versions
See tool-versions.txt. Python 3.14.2

## Commands
python3 -m unittest discover -s 20_Day_Python_package_manager/applied-labs/r27-t043 -p "test_*.py"
python3 -m venv /tmp/r27-t043-venv, then run the same unittest command with /tmp/r27-t043-venv/bin/python