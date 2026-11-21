def tokenize(text):
    """Step 1: split the text on any whitespace into a list of words."""
    return text.split()


def text_stats(text):
    """Return the number of words and the number of distinct words.

    Words are case-sensitive: "One" and "one" count as different words.
    """
    words = tokenize(text)  # intermediate state 1: the list of words
    distinct = set(words)  # intermediate state 2: duplicates removed
    return {"words": len(words), "distinct": len(distinct)}


def explain(text):
    """Worked explanation: input -> intermediate state -> output."""
    words = tokenize(text)
    distinct = sorted(set(words))  # sorted so the output is always the same
    return [
        f"input: {text!r}",
        f"split into words: {words}",
        f"distinct words: {distinct}",
        f"output: {text_stats(text)}",
    ]


if __name__ == "__main__":
    for line in explain("one two two"):
        print(line)