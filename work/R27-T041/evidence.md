# Evidence for R27-T041

## Inputs and expected results
- 0 C -> expected 32 F
- 100 C -> expected 212 F
- -40 C -> expected -40 F
- import example (fresh process, standard input closed) -> expected: no output, no input read, exit code 0
- CLI with typed 0 -> expected "0 C = 32 F"
- CLI with typed 100 -> expected "100 C = 212 F"

## Actual results
- 5 tests ran, all OK (see pass-result.txt, exit code 0)
- CLI output saved in cli-result.txt

## Tool versions
Python 3.14.2

## Command
python3 -m unittest discover -s 12_Day_Modules/applied-labs/r27-t041 -p "test_*.py"