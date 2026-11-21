# Applied Lab R27-T043: Text Statistics with a Reference Comparison

Added activity (not an original numbered exercise).

A small text statistics function packaged with a declared dependency set
(`requirements.txt`, which is empty because only the standard library is
used) and a command that runs in a clean virtual environment.

- Input: `"one two two"`
- Expected: 3 words and 2 distinct words

Words are separated by whitespace and are case-sensitive.

## Independent expected-result table

Worked out by hand. The tests check the function against every row.

| Text                  | Words | Distinct |
| --------------------- | ----- | -------- |
| `"one two two"`       | 3     | 2        |
| `""`                  | 0     | 0        |
| `"   "` (spaces only) | 0     | 0        |
| `"one"`               | 1     | 1        |
| `"a a a"`             | 3     | 1        |
| `"One one"`           | 2     | 2        |
| `"  one   two\ttwo\n"` | 3    | 2        |
| `"a\nb\nc"`           | 3     | 3        |

## Independent reference implementation

`text_stats` uses `split()` and `set()`. `reference_text_stats` gives the
same answers a different way: it walks the text one character at a time
and uses neither `split()` nor `set()`. The tests compare the two on
every string of length 0 to 6 made from the characters `a`, `b`, space
and tab. That is 5461 strings, with no randomness, and every one must
agree. A test also checks that the reference really does not use
`split` or `set`, so it stays independent.

## Run the tests

From the repository root:

    python3 -m unittest discover -s 20_Day_Python_package_manager/applied-labs/r27-t043 -p "test_*.py"

## Run in a clean virtual environment

The environment is created outside the repository so it is not committed:

    python3 -m venv /tmp/r27-t043-venv
    /tmp/r27-t043-venv/bin/python -m pip install -r 20_Day_Python_package_manager/applied-labs/r27-t043/requirements.txt
    /tmp/r27-t043-venv/bin/python -m unittest discover -s 20_Day_Python_package_manager/applied-labs/r27-t043 -p "test_*.py"

The tests also run the example with `python -s` (user-site packages
disabled) to show that the import works without them.