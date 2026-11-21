def text_stats(text):
    """Return the number of words and the number of distinct words.

    Words are separated by whitespace and are case-sensitive:
    "One" and "one" count as different words.
    """
    words = text.split()
    return {"words": len(words), "distinct": len(set(words))}


def reference_text_stats(text):
    """Independent reference implementation of the same behavior.

    It is built differently on purpose: it walks the text one character at
    a time, with no split() and no set(). If both versions agree on many
    inputs, a mistake in one of them is very unlikely to be hidden.
    """
    words = []
    current = ""
    for char in text:
        if char.isspace():
            if current:
                words.append(current)
                current = ""
        else:
            current += char
    if current:
        words.append(current)

    distinct = []
    for word in words:
        if word not in distinct:
            distinct.append(word)
    return {"words": len(words), "distinct": len(distinct)}


if __name__ == "__main__":
    print("text_stats:", text_stats("one two two"))
    print("reference:", reference_text_stats("one two two"))