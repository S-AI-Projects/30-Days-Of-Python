# Evidence for R27-T045

## Inputs and expected results
- Rows A,2 / A,3 / B,4 -> expected A(count=2, sum=5), B(count=1, sum=4), no errors
- A,5 and A,-2 -> expected A(count=2, sum=3)
- Empty input and header-only input -> expected no groups, no errors
- Rows A,2 / A,oops / B / B,4 / ,7 -> expected errors at line 3, line 4 and line 6, good rows still counted
- Row count check -> counted rows + errors = 5 data rows (nothing silently dropped)
- Blank line in the middle -> expected an error at its line number, not skipped
- Same data from io.StringIO and from a list -> expected identical results (injected source)
- Two isolated processes -> expected identical output (see run1.txt, run2.txt, runs-compare.txt)
- example.py imports -> expected only csv and io (no time, random or network)

## Actual results
- 11 tests ran, all OK (see pass-result.txt, exit code 0)
- run1.txt and run2.txt are identical (see runs-compare.txt)

## Tool versions
Python 3.14.2

## Command
python3 -m unittest discover -s 25_Day_Pandas/applied-labs/r27-t045 -p "test_*.py"