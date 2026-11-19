# Evidence for R27-T042

## Inputs and expected results
- ((1, 2), (3, 4)) shifted by (2, -1) -> expected ((3, 1), (5, 3)); input unchanged
- () shifted by (5, 5) -> expected ()
- ((1,),) -> expected ValueError (1 coordinate, below the boundary of 2)
- ((1, 2, 3),) -> expected ValueError (3 coordinates, above the boundary of 2)
- ((),) -> expected ValueError (empty point)
- [(1, 2)] (a list, not a tuple) -> expected TypeError

## Actual results
- 9 tests ran, all OK (see pass-result.txt, exit code 0)

## Tool versions
Python 3.14.2  

## Command
python3 -m unittest discover -s 06_Day_Tuples/applied-labs/r27-t042 -p "test_*.py"