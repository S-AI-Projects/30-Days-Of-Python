def dedupe(items):
    """Remove duplicates, keep the first occurrence of each item, in order.
    The input list is never modified.

    Invariant: the result has no repeated items, contains exactly the same
    distinct items as the input, and keeps first-occurrence order.
    """
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result


if __name__ == "__main__":
    print(dedupe([3, 1, 3, 2, 1]))