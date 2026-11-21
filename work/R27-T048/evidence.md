# Evidence for R27-T048

## Inputs and expected results
- ["3", "bad", "-2"] -> expected values [3, -2], one error at index 1
- [] -> expected ([], []) (empty state)
- ["bad", "", "1.5"] -> expected no values, errors at indexes 0, 1, 2
- ["bad"] then ["7"] in the same session -> expected error first, then recovery with [7]
- ["3", None, "5"] -> expected TypeError (not swallowed)
- Source code check -> expected only `except ValueError`, no bare except

## Actual results
- 6 tests ran, all OK (see pass-result.txt, exit code 0)

## Tool versions
Python 3.14.2

## Command
python3 -m unittest discover -s 15_Day_Python_type_errors/applied-labs/r27-t048 -p "test_*.py"