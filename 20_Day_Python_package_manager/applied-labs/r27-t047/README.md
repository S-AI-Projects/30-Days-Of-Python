# R27-T047: Isolated dependencies and text statistics

`text_statistics(text)` calculates total and distinct word counts with clean virtual environment isolation.

## Contract and Behavior

- `"one two two"` yields `3` total words and `2` distinct words.
- Import succeeds without user-site packages (`python3 -s`).
- Clean virtual environment setup with declared dependencies in `requirements.txt`.

## Worked Explanation: Input -> Intermediate State -> Output

1. **Input**:
   `"one two two"`
2. **Intermediate State**:
   - Word token list: `["one", "two", "two"]` (length: 3)
   - Unique word set: `{"one", "two"}` (length: 2)
3. **Output**:
   `{"total_words": 3, "distinct_words": 2}`

## Run the tests

From the repository root:

    python3 -m unittest discover -s 20_Day_Python_package_manager/applied-labs/r27-t047 -p "test_*.py"
