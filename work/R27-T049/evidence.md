# Evidence for R27-T049

## Inputs and expected results
- 2024-01-01T10:00:00+05:30 -> 2024-01-01T05:00:00+00:00: expected 1800 seconds
- Reversed order: expected -1800 seconds
- Missing offset (start or end), date-only text, garbage text: expected ValueError

## Input sizes (correctness asserted, operation counts reported, no speed threshold)
- 1 pair: results correct, parse_calls = 2
- 10 pairs: results correct, parse_calls = 20
- 100 pairs: results correct, parse_calls = 200

## Actual results
- 9 tests ran, all OK (see pass-result.txt, exit code 0)

## Tool versions
Python 3.14.2

## Command
python3 -m unittest discover -s 16_Day_Python_date_time/applied-labs/r27-t049 -p "test_*.py"