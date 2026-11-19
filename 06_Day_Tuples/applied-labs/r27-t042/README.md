# Applied Lab R27-T042: Translate 2D Points

Added activity (not an original numbered exercise).

Shifts every 2D point in a tuple by (dx, dy) and returns new tuples. The
input is never modified (tuples are immutable, and a new tuple is returned).

- Input: `((1, 2), (3, 4))` shifted by `(2, -1)`
- Expected: `((3, 1), (5, 3))`; the input stays `((1, 2), (3, 4))`
- Input: `()` shifted by any `(dx, dy)`
- Expected: `()`

Run the tests from the repository root:

    python3 -m unittest discover -s 06_Day_Tuples/applied-labs/r27-t042 -p "test_*.py"

Boundary condition: every point must have exactly 2 coordinates.
A point with 1 coordinate, 3 coordinates, or none raises `ValueError`.
An empty tuple of points is valid and returns an empty tuple. If the
input is not a tuple, `TypeError` is raised. The tests cover one below
the boundary (1 coordinate), one above it (3 coordinates), and the
empty cases.