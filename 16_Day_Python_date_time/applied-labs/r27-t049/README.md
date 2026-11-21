# Applied Lab R27-T049: Elapsed Seconds Between Timestamps

Added activity (not an original numbered exercise).

Parses ISO-8601 timestamps that include an offset, converts them to UTC,
and returns the elapsed seconds between them. A timestamp with no offset
is rejected with `ValueError`.

- Input: `2024-01-01T10:00:00+05:30` and `2024-01-01T05:00:00+00:00`
- Expected: `1800` seconds (the first is 04:30 UTC, the second 05:00 UTC)
- Input: `2024-01-01T10:00:00` (no offset)
- Expected: `ValueError`

Run the tests from the repository root:

    python3 -m unittest discover -s 16_Day_Python_date_time/applied-labs/r27-t049 -p "test_*.py"

Input sizes: the tests run 1, 10 and 100 pairs. Each test asserts that
every result is correct and that the parser ran exactly 2 times per pair
(2, 20 and 200 parse calls). The counts are printed. No speed threshold
is used, because timing varies between machines.