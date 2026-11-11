# Reusable Text Normalization Pipeline

This added activity demonstrates a higher-order function that composes transformations into one reusable pipeline.

Run the published example and its tests from the repository root:

```sh
python3 14_Day_Higher_order_functions/applied-labs/r27-t017/example.py
python3 -m unittest discover -s 14_Day_Higher_order_functions/applied-labs/r27-t017 -p "test_*.py"
```

The pipeline strips surrounding whitespace, lowercases the text, then collapses every run of whitespace to one space.

Worked example:

```text
Input: '  HELLO   World  '
After strip: 'HELLO   World'
After lowercase: 'hello   world'
After whitespace collapse: 'hello world'
Normalized again: 'hello world'
```

The fixture also includes the required input `" HELLO World "` with expected result `"hello world"`. Applying normalization again does not change the result.
