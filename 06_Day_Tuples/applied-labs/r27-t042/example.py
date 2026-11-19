def translate(points, dx, dy):
    """Shift every 2D point by (dx, dy) and return NEW tuples.
    The input is never modified.

    Boundary rules:
    - An empty tuple of points is valid and returns an empty tuple.
    - Every point must be a tuple with EXACTLY 2 coordinates.
      A point with 1 or 3 coordinates (or an empty point) raises ValueError.
    - If points is not a tuple, raise TypeError.
    """
    if not isinstance(points, tuple):
        raise TypeError("points must be a tuple")
    result = []
    for point in points:
        if not isinstance(point, tuple) or len(point) != 2:  # decisive boundary
            raise ValueError(f"Each point must be a tuple of exactly 2 coordinates: {point!r}")
        x, y = point
        result.append((x + dx, y + dy))
    return tuple(result)


if __name__ == "__main__":
    print(translate(((1, 2), (3, 4)), 2, -1))