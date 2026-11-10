# R27-T053: Coordinate tuples translation with reference comparison

`translate_points(points, shift)` translates a tuple of 2D points by `(dx, dy)`, returning new tuples.

## Behavior and Reference Comparison

- `((1, 2), (3, 4))` shifted by `(2, -1)` returns `((3, 1), (5, 3))`.
- Input tuples remain unchanged (demonstrating tuple immutability).
- A simpler reference implementation `reference_translate_points` and an independent expected-result table `EXPECTED_TABLE` are provided to verify the implementation against defined reference behaviors.

## Run the tests

From the repository root:

    python3 -m unittest discover -s 06_Day_Tuples/applied-labs/r27-t053 -p "test_*.py"

