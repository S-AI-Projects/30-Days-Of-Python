"""Day 5 Applied Lab (R27-T025): Ordered Deduplication Deterministic Fixture Lab.

Contract:
- Remove duplicate items from a list while preserving the first occurrence and leaving
  the input list unchanged.
- `[3, 1, 3, 2, 1]` becomes `[3, 1, 2]`; `[]` stays `[]`; the original list remains
  `[3, 1, 3, 2, 1]`.
- Contribution focus: Inject time, storage, events, or network where used; use repeatable
  local fixtures and show that two isolated runs agree.
"""

from __future__ import annotations

from typing import Callable, Dict, List, Optional, TypeVar

T = TypeVar("T")

REPEATABLE_FIXTURES: Dict[str, List[int]] = {
    "contract_sample": [3, 1, 3, 2, 1],
    "empty_sample": [],
    "all_duplicates": [7, 7, 7],
    "already_unique": [4, 5, 6],
}


def deduplicate_ordered(
    items: List[T],
    event_sink: Optional[List[Dict[str, object]]] = None,
    clock: Callable[[], str] = lambda: "2026-11-03T00:00:00Z",
) -> List[T]:
    """Return a new list with duplicates removed in first-occurrence order.

    Does not mutate `items`. Optionally records deterministic keep/skip events into an
    injected `event_sink` stamped by an injected `clock`.
    """
    seen = set()
    result: List[T] = []
    timestamp = clock()

    for index, item in enumerate(items):
        if item not in seen:
            seen.add(item)
            result.append(item)
            if event_sink is not None:
                event_sink.append(
                    {
                        "index": index,
                        "item": item,
                        "action": "kept",
                        "timestamp": timestamp,
                    }
                )
        else:
            if event_sink is not None:
                event_sink.append(
                    {
                        "index": index,
                        "item": item,
                        "action": "skipped_duplicate",
                        "timestamp": timestamp,
                    }
                )

    return result


def run_isolated_fixture(
    fixture_name: str = "contract_sample",
    fixed_timestamp: str = "2026-11-03T00:00:00Z",
) -> Dict[str, object]:
    """Execute an isolated run on a fresh copy of a named local fixture."""
    original = list(REPEATABLE_FIXTURES[fixture_name])
    snapshot_before = list(original)
    events: List[Dict[str, object]] = []
    output = deduplicate_ordered(
        original,
        event_sink=events,
        clock=lambda: fixed_timestamp,
    )
    return {
        "input_before": snapshot_before,
        "input_after": original,
        "output": output,
        "events": events,
    }


if __name__ == "__main__":
    run_one = run_isolated_fixture("contract_sample")
    run_two = run_isolated_fixture("contract_sample")
    print("Original after deduplication:", run_one["input_after"])
    print("Deduplicated output:", run_one["output"])
    print("Two isolated runs agree:", run_one == run_two)
