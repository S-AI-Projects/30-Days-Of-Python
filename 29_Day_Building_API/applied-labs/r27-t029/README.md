# Day 29 Applied Lab (`R27-T029`): Installable Mini-Package Regression-Focused Lab

## Overview
This applied lab provides an installable Python mini-package (`r27-t029-wordcount` / `wordcount_pkg`) with a zero-dependency PEP 517 backend (`pyproject.toml` + `_pep517_backend.py`), exposing both `word_count(text)` and the `r27-wordcount` console script entry point.

## Contract & Regression Mutant Check
- **Decisive condition**: `word_count("a b a")` counts every whitespace-separated token (`return len(tokens)` $\rightarrow$ `3`).
- **One-line mutant**: `word_count_unique_mutant("a b a")` replaces the decisive line with `return len(set(tokens))` $\rightarrow$ `2`.
- **Focused regression test**: `verify_repeated_word_contract` asserts `counter_fn("a b a") == 3`, passing on `word_count` and failing on `word_count_unique_mutant`.
- **Installed CLI verification**: Installing the package with `pip install --no-deps --no-build-isolation --target <dir>` and running `r27-wordcount "a b a"` and `r27-wordcount --help` from an external working directory prints `3` and the help usage banner with exit code `0`.

## Running the Example and Tests
From the repository root:

```bash
python3 29_Day_Building_API/applied-labs/r27-t029/example.py
python3 -m unittest discover -s 29_Day_Building_API/applied-labs/r27-t029 -p "test_*.py"
```
