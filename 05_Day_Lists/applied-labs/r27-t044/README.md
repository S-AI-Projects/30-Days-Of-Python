# Applied Lab R27-T044: Remove Duplicates, Keep First Occurrence

Added activity (not an original numbered exercise).

Removes duplicate items from a list, keeping the first occurrence of each
item. The input list is never modified.

- Input: `[3, 1, 3, 2, 1]`
- Expected: `[3, 1, 2]` (the original stays `[3, 1, 3, 2, 1]`)
- Input: `[]`
- Expected: `[]`

Run the tests from the repository root:

    python3 -m unittest discover -s 05_Day_Lists/applied-labs/r27-t044 -p "test_*.py"

Invariant: the result has no repeated items, contains exactly the same
distinct items as the input, and keeps first-occurrence order. The test
`test_invariant_across_sequence_of_operations` checks this after several
operations in a row: dedupe, dedupe again, then change the input and
dedupe once more.