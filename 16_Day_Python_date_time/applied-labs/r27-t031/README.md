# Applied Lab R27-T031: Timezone-Aware Timestamps in UTC

## Objective
Parse ISO-8601 formatted timestamps with timezone offsets, validate offset presence, and calculate elapsed duration in seconds normalized to UTC.

## Contract
- Rejects naive ISO-8601 strings (without timezone offset) by raising ValueError.
- Evaluates the fixture difference:
  - 2024-01-01T10:00:00+05:30 (UTC: 2024-01-01 04:30:00)
  - 2024-01-01T05:00:00+00:00 (UTC: 2024-01-01 05:00:00)
  - Difference: 1800.0 seconds.

## Running Tests
Execute test discovery from the repository root:

