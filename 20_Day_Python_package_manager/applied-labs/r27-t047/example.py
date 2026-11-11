"""R27-T047: Text statistics package with declared dependencies and isolated execution."""


def text_statistics(text):
    """Calculate word count and distinct word count for a given text string.

    Contract:
    'one two two' has 3 words and 2 distinct words.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    words = text.split()
    return {
        "total_words": len(words),
        "distinct_words": len(set(words)),
        "word_count": len(words),
        "distinct_word_count": len(set(words)),
    }


def explain_text_statistics(text):
    """Worked explanation tracing execution from input through intermediate state to output.

    1. Input: raw text string.
    2. Intermediate state:
       - tokens: list of whitespace-split word tokens.
       - unique_tokens: set of distinct tokens.
    3. Output: mapping of total words and distinct word counts.
    """
    raw_input = text
    tokens = raw_input.split()
    unique_tokens = set(tokens)
    stats = {
        "total_words": len(tokens),
        "distinct_words": len(unique_tokens),
    }
    return {
        "input": raw_input,
        "intermediate": {
            "tokens": tokens,
            "unique_tokens": sorted(list(unique_tokens)),
        },
        "output": stats,
    }


if __name__ == "__main__":
    sample = "one two two"
    result = text_statistics(sample)
    print(f"Input: {sample}")
    print(
        f"Result: {result['total_words']} words, {result['distinct_words']} distinct words"
    )

    explanation = explain_text_statistics(sample)
    print("\nWorked Explanation:")
    print(f"  Input:        {explanation['input']}")
    print(f"  Intermediate: tokens={explanation['intermediate']['tokens']}")
    print(
        f"                unique_tokens={explanation['intermediate']['unique_tokens']}"
    )
    print(f"  Output:       {explanation['output']}")
