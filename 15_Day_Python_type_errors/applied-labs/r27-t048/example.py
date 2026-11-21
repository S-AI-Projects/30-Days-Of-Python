def parse_integers(records):
    """Parse integers from a list of text records.

    Returns (values, errors):
    - values: the integers that parsed successfully, in order
    - errors: a list of (index, record, reason) for records that were not
      valid integers. The index is the position in the input list.

    Only ValueError is caught (text that is not an integer, like "bad" or "").
    Unrelated problems, such as a record that is None (TypeError), are NOT
    swallowed: they propagate so the real bug is visible. There is no bare
    except anywhere.
    """
    values = []
    errors = []
    for index, record in enumerate(records):
        try:
            values.append(int(record))
        except ValueError as exc:  # decisive: catch ONLY ValueError
            errors.append((index, record, str(exc)))
    return values, errors


if __name__ == "__main__":
    # One session, no restart: empty state, then an error, then recovery.
    print("empty input:   ", parse_integers([]))
    print("main example:  ", parse_integers(["3", "bad", "-2"]))
    print("only bad input:", parse_integers(["bad"]))
    print("next valid one:", parse_integers(["7"]))