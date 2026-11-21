# Evidence for R27-T047

## Inputs and expected results
- "one two two" -> expected 3 words and 2 distinct words
- "" -> expected 0 words and 0 distinct
- "  one   two\ttwo\n" (extra whitespace) -> expected 3 words and 2 distinct
- "One one" (case-sensitive) -> expected 2 words and 2 distinct
- Worked example output -> expected to match the README exactly (checked by the test)
- requirements.txt -> expected to declare no dependencies
- Import with user-site packages disabled (python -s) -> expected to succeed

## Actual results
- Normal run: 9 tests ran, all OK (see pass-result.txt, exit code 0)
- Clean virtual environment run: 9 tests ran, all OK (see venv-result.txt, exit code 0)

## Tool versions
See tool-versions.txt. Python 3.14.2
## Commands
python3 -m unittest discover -s 20_Day_Python_package_manager/applied-labs/r27-t047 -p "test_*.py"
python3 -m venv /tmp/r27-t047-venv, then run the same unittest command with /tmp/r27-t047-venv/bin/python