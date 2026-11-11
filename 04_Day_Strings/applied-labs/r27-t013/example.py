import re
from collections import Counter


WORD_PATTERN = re.compile(r"[^\W_]+(?:['’][^\W_]+)*", re.UNICODE)


def count_words(text):
    """Return lowercase word counts, keeping apostrophes inside words."""
    words = WORD_PATTERN.findall(text.lower())
    return dict(Counter(words))


if __name__ == "__main__":
    print(count_words("Tea, tea! isn't coffee."))
