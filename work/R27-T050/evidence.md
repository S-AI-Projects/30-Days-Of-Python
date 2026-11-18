# Evidence for R27-T050

## Inputs and expected results
- {"tea": 3} + {"tea": -2, "coffee": 4} -> expected {"tea": 1, "coffee": 4}
- {"tea": 3} + {"tea": -4} -> expected ValueError, original stays {"tea": 3}
- {"tea": 2} + {"tea": -2} -> expected {"tea": 0} (zero is allowed)

## Actual results
- Correct code: 4 tests ran, all OK (see pass-result.txt)
- Mutant (`< 0` changed to `<= 0`): test_exactly_zero_is_allowed FAILED (see mutant-result.txt)
- After reverting the mutant: 4 tests OK again

## Tool versions
See tool-versions.txt (Python 3)

## Command
python3 -m unittest discover -s 08_Day_Dictionaries/applied-labs/r27-t050 -p "test_*.py"