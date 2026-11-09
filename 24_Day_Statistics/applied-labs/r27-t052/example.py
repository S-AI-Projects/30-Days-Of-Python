import statistics


def missing_value_summary(observations):
    """Calculate count, missing_count, mean, and median for numeric observations with None values.

    Boundary condition:
    When count == 0 (empty input or all-missing values), mean and median are None (null)
    because dividing by zero or taking the median of an empty set is undefined.
    """
    if observations is None or not hasattr(observations, "__iter__"):
        raise TypeError("observations must be an iterable")

    valid = []
    missing_count = 0

    for x in observations:
        if x is None:
            missing_count += 1
        elif isinstance(x, (int, float)) and not isinstance(x, bool):
            valid.append(x)
        else:
            raise TypeError(
                f"Unsupported observation type: {type(x).__name__}"
            )

    count = len(valid)

    if count == 0:
        mean = None
        median = None
    else:
        mean = statistics.mean(valid)
        median = statistics.median(valid)

    return {
        "count": count,
        "missing_count": missing_count,
        "mean": mean,
        "median": median,
    }


calculate_summary = missing_value_summary


if __name__ == "__main__":
    print(missing_value_summary([1, None, 3, 5]))
    print(missing_value_summary([None, None]))
    print(missing_value_summary([]))

