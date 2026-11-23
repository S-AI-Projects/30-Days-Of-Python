"""Installable `wordcount_pkg` mini-package for Day 29 Applied Lab (R27-T029)."""

from __future__ import annotations


def word_count(text: str) -> int:
    """Count total whitespace-delimited words in `text` (including repeated words).

    Decisive condition: counts every token in `tokens = text.split()` (`len(tokens)`),
    so `"a b a"` has 3 words.
    """
    tokens = text.split()
    return len(tokens)


def word_count_unique_mutant(text: str) -> int:
    """One-line mutant of the decisive condition: deduplicates tokens with `set(tokens)`.

    Fails on inputs with repeated words such as `"a b a"` (returns 2 instead of 3).
    """
    tokens = text.split()
    return len(set(tokens))
