"""Day 24 Applied Lab (R27-T024): Missing-Value Summary State/Invariant Lab.

Contract:
- Calculate `count`, `missing_count`, `mean`, and `median` for numeric observations
  containing `None` values.
- `[1, None, 3, 5]` gives `count=3`, `missing_count=1`, `mean=3`, `median=3`.
- All-missing (`[None, None]` or `[]`) gives `mean=None` and `median=None` (`null` in JSON).
- Contribution focus: State and test the invariant connecting input/state to output
  across a short sequence of operations:
  1. Partition invariant: `count + missing_count == len(observations)`.
  2. Null-statistics invariant: `(count == 0) == (mean is None and median is None)`.
  3. Order/bounds invariant: when `count > 0`, `min(valid) <= mean <= max(valid)` and
     `min(valid) <= median <= max(valid)`, and appending `None` increments `missing_count`
     without changing `count`, `mean`, or `median`.
"""

from __future__ import annotations

import statistics
from typing import Dict, Iterable, List, Optional, Union

Number = Union[int, float]


def _normalize_numeric(val: float) -> Number:
    """Return an int when a float is an exact integer (e.g. 3.0 -> 3), else float."""
    return int(val) if float(val).is_integer() else float(val)


def summarize_observations(
    observations: Iterable[Optional[Number]],
) -> Dict[str, Optional[Number]]:
    """Summarize numeric observations with possible `None` entries."""
    items = list(observations)
    valid: List[Number] = [x for x in items if x is not None]
    count = len(valid)
    missing_count = len(items) - count

    if count == 0:
        mean_val: Optional[Number] = None
        median_val: Optional[Number] = None
    else:
        mean_val = _normalize_numeric(statistics.mean(valid))
        median_val = _normalize_numeric(statistics.median(valid))

    return {
        "count": count,
        "missing_count": missing_count,
        "mean": mean_val,
        "median": median_val,
    }


def check_summary_invariants(
    observations: Iterable[Optional[Number]],
    summary: Dict[str, Optional[Number]],
) -> bool:
    """Assert all state/output invariants for a given observation list and its summary."""
    items = list(observations)
    valid = [x for x in items if x is not None]
    count = summary["count"]
    missing_count = summary["missing_count"]
    mean_val = summary["mean"]
    median_val = summary["median"]

    if not isinstance(count, int) or not isinstance(missing_count, int):
        return False

    # Invariant 1: Partition of total observations into valid count + missing_count
    if count + missing_count != len(items):
        return False

    # Invariant 2: Null mean/median iff count == 0
    if count == 0:
        return mean_val is None and median_val is None

    if mean_val is None or median_val is None:
        return False

    # Invariant 3: Mean and median lie within [min(valid), max(valid)]
    low, high = min(valid), max(valid)
    return (low <= mean_val <= high) and (low <= median_val <= high)


class ObservationTracker:
    """Stateful tracker demonstrating invariant preservation across a sequence of operations."""

    def __init__(self, initial: Iterable[Optional[Number]] = ()) -> None:
        self._items: List[Optional[Number]] = list(initial)

    @property
    def observations(self) -> List[Optional[Number]]:
        return list(self._items)

    def add(self, value: Optional[Number]) -> Dict[str, Optional[Number]]:
        self._items.append(value)
        return self.summary()

    def summary(self) -> Dict[str, Optional[Number]]:
        result = summarize_observations(self._items)
        assert check_summary_invariants(self._items, result), "Summary invariant violated"
        return result


if __name__ == "__main__":
    print("Fixture [1, None, 3, 5]:", summarize_observations([1, None, 3, 5]))
    print("All-missing [None, None]:", summarize_observations([None, None]))
