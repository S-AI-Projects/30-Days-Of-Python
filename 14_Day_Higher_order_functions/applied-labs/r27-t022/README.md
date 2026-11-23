# Day 14 Applied Lab (`R27-T022`): Function Composition Normalization Pipeline

## Overview
This boundary-focused lab composes `strip_edges`, `to_lowercase`, and `collapse_whitespace` using a higher-order `compose_pipeline` helper built with `functools.reduce`.

## Boundary Conditions & Idempotence
- **Standard Fixture**: `"  HELLO   World "` $\rightarrow$ `"hello world"`.
- **Idempotence Boundary**: Because a normalized string has no leading/trailing spaces, no uppercase letters, and at most a single ASCII space between non-empty tokens, applying `normalize_text` a second time is a fixed-point operation: `normalize_text(normalize_text(x)) == normalize_text(x)`.
- **Empty / Whitespace-Only Boundary**: `""` and `"   \t\n  "` collapse to `""` without error.
- **Invalid Input Boundary**: Non-string values (`None`, numbers, lists) fail fast with `TypeError`.

## Running the Example and Tests
From the repository root:

```bash
python3 14_Day_Higher_order_functions/applied-labs/r27-t022/example.py
python3 -m unittest discover -s 14_Day_Higher_order_functions/applied-labs/r27-t022 -p "test_*.py"
```
