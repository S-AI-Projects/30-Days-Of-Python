## Description

Adds a Day 4 applied lab that lowercases and counts words, strips punctuation
at word boundaries, and retains internal apostrophes. The lab includes an
independent expected-result table, tests, and recorded check evidence.

## Related Issue

No related issue was provided.

## Fixes

Not applicable.

## Type of Change

- [x] New Feature
- [x] Tests
- [x] Documentation

## Changes Made

- Added `04_Day_Strings/applied-labs/r27-t013/` with the implementation,
  reference-result tests, and README.
- Linked and summarized the added activity in `04_Day_Strings/04_strings.md`
  without changing or renumbering the original exercises.
- Saved inputs, expected and actual mappings, test output, and tool versions
  under `work/R27-T013/`.

## Screenshots / Recordings

Not applicable; this change has no UI.

## Testing

- `python3 -m unittest discover -s 04_Day_Strings/applied-labs/r27-t013 -p "test_*.py"` — 5 tests passed.
- `python3 04_Day_Strings/applied-labs/r27-t013/example.py` — printed `{'tea': 2, "isn't": 1, 'coffee': 1}`.

## Checklist

- [x] I have tested my changes locally.
- [x] I have added or updated tests, if needed.
- [x] I have updated documentation, if needed.
- [x] I have followed the project's coding guidelines.
- [x] I have run the relevant tests and checks.
- [x] I have addressed previous review feedback, if applicable.

## Additional Notes

The `work/R27-T013/` evidence is for this coursework submission and should not
be included in a later upstream contribution.
