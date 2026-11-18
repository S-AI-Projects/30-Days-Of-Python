# Evidence for R27-T044

## Inputs and expected results
- [3, 1, 3, 2, 1] -> expected [3, 1, 2]; original stays [3, 1, 3, 2, 1]
- [] -> expected []
- Sequence: dedupe, dedupe again (same result), append 4 and 3 then dedupe -> [3, 1, 2, 4]

## Actual results
- 4 tests ran, all OK (see pass-result.txt, exit code 0)

## Tool versions
Python 3.14.2  <- replace with the line from tool-versions.txt

## Command
python3 -m unittest discover -s 05_Day_Lists/applied-labs/r27-t044 -p "test_*.py"