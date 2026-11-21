# Applied Lab R27-T040: Bounded HTML Extraction Lab

## Objective
Parse local HTML fixtures into title/link records, resolve relative URLs without network requests, and skip links lacking href.

## Contract
- `<a href="/docs">Docs</a>` under `https://example.invalid` → `{title: "Docs", link: "https://example.invalid/docs"}`.
- Links without `href` are skipped.
- Mutant of the decisive condition is tested and fails regression checks.

## Running Tests
Run test discovery from the repository root:
```bash
python3 -m unittest discover -s 22_Day_Web_scraping/applied-labs/r27-t040 -p "test_*.py"
```
