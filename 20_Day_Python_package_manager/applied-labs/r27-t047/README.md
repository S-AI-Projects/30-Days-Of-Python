# Applied Lab R27-T047: Text Statistics Package

Added activity (not an original numbered exercise).

A small text statistics function packaged with a declared dependency set
(`requirements.txt`, which is empty because only the standard library is
used) and a command that runs in a clean virtual environment.

- Input: `"one two two"`
- Expected: 3 words and 2 distinct words

## Worked explanation

1. Input: the text `"one two two"`.
2. Intermediate state 1: splitting on whitespace gives the list
   `['one', 'two', 'two']`. It has 3 items, so `words = 3`.
3. Intermediate state 2: removing duplicates gives `['one', 'two']`.
   It has 2 items, so `distinct = 2`.
4. Output: `{'words': 3, 'distinct': 2}`.

Running `python3 example.py` prints exactly this (the test checks it):

```
input: 'one two two'
split into words: ['one', 'two', 'two']
distinct words: ['one', 'two']
output: {'words': 3, 'distinct': 2}
```

## Run the tests

From the repository root:

    python3 -m unittest discover -s 20_Day_Python_package_manager/applied-labs/r27-t047 -p "test_*.py"

## Run in a clean virtual environment

The environment is created outside the repository so it is not committed:

    python3 -m venv /tmp/r27-t047-venv
    /tmp/r27-t047-venv/bin/python -m pip install -r 20_Day_Python_package_manager/applied-labs/r27-t047/requirements.txt
    /tmp/r27-t047-venv/bin/python -m unittest discover -s 20_Day_Python_package_manager/applied-labs/r27-t047 -p "test_*.py"

The tests also run the example with `python -s` (user-site packages
disabled) to show that the import works without them.