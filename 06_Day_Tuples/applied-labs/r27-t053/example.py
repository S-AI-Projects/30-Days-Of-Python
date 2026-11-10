"""R27-T053: Translate coordinate tuples with reference comparison."""

# Independent expected-result table for the defined translation behavior
EXPECTED_TABLE = (
    {
        "points": ((1, 2), (3, 4)),
        "shift": (2, -1),
        "expected": ((3, 1), (5, 3)),
    },
    {
        "points": ((0, 0),),
        "shift": (5, 5),
        "expected": ((5, 5),),
    },
    {
        "points": (),
        "shift": (1, 1),
        "expected": (),
    },
)


def reference_translate_points(points, shift):
    """Simpler, explicit reference implementation used for comparison."""
    dx, dy = shift
    result = []
    for pt in points:
        result.append((pt[0] + dx, pt[1] + dy))
    return tuple(result)


def translate_points(points, shift):
    """Translate a tuple of 2D points by (dx, dy), returning new tuples.

    The original input tuple remains unchanged.
    """
    dx, dy = shift
    return tuple((x + dx, y + dy) for x, y in points)


if __name__ == "__main__":
    coords = ((1, 2), (3, 4))
    delta = (2, -1)
    translated = translate_points(coords, delta)
    print("Input:     ", coords)
    print("Shift:     ", delta)
    print("Translated:", translated)
    print("Input unchanged:", coords == ((1, 2), (3, 4)))

