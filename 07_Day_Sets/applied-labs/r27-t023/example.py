"""Day 7 Applied Lab (R27-T023): Enrolment Sets Reference Comparison Lab.

Contract:
- Calculate students in both groups (`intersection`), only in the first (`first_only` / `first-only`),
  and in either group (`union`).
- For `A={"Ana", "Bo"}` and `B={"Bo", "Cy"}`:
  `intersection={"Bo"}`, `first-only={"Ana"}`, `union={"Ana", "Bo", "Cy"}`.
- Contribution focus: Provide a small independent expected-result table and a simpler
  loop-based reference implementation, and compare the Python set-method implementation
  against both.
"""

from __future__ import annotations

from typing import Dict, Iterable, List, Set

EXPECTED_RESULT_TABLE: List[Dict[str, object]] = [
    {
        "case": "contract_fixture",
        "group_a": {"Ana", "Bo"},
        "group_b": {"Bo", "Cy"},
        "expected": {
            "intersection": {"Bo"},
            "first_only": {"Ana"},
            "first-only": {"Ana"},
            "union": {"Ana", "Bo", "Cy"},
        },
    },
    {
        "case": "disjoint_groups",
        "group_a": {"Ana"},
        "group_b": {"Cy"},
        "expected": {
            "intersection": set(),
            "first_only": {"Ana"},
            "first-only": {"Ana"},
            "union": {"Ana", "Cy"},
        },
    },
    {
        "case": "identical_groups",
        "group_a": {"Ana", "Bo"},
        "group_b": {"Ana", "Bo"},
        "expected": {
            "intersection": {"Ana", "Bo"},
            "first_only": set(),
            "first-only": set(),
            "union": {"Ana", "Bo"},
        },
    },
    {
        "case": "empty_first_group",
        "group_a": set(),
        "group_b": {"Bo", "Cy"},
        "expected": {
            "intersection": set(),
            "first_only": set(),
            "first-only": set(),
            "union": {"Bo", "Cy"},
        },
    },
]


def compare_enrolments(
    group_a: Iterable[str],
    group_b: Iterable[str],
) -> Dict[str, Set[str]]:
    """Compute enrolment overlap using Python set methods."""
    set_a = set(group_a)
    set_b = set(group_b)
    intersection = set_a.intersection(set_b)
    first_only = set_a.difference(set_b)
    union = set_a.union(set_b)
    return {
        "intersection": intersection,
        "first_only": first_only,
        "first-only": first_only,
        "union": union,
    }


def reference_compare_enrolments(
    group_a: Iterable[str],
    group_b: Iterable[str],
) -> Dict[str, Set[str]]:
    """Simpler membership-loop reference implementation for independent comparison."""
    list_a = list(group_a)
    list_b = list(group_b)
    intersection = {student for student in list_a if student in list_b}
    first_only = {student for student in list_a if student not in list_b}
    union = {student for student in (list_a + list_b)}
    return {
        "intersection": intersection,
        "first_only": first_only,
        "first-only": first_only,
        "union": union,
    }


def verify_against_reference_table() -> List[Dict[str, object]]:
    """Compare `compare_enrolments` against both the reference implementation and table."""
    comparisons: List[Dict[str, object]] = []
    for row in EXPECTED_RESULT_TABLE:
        group_a = row["group_a"]
        group_b = row["group_b"]
        actual = compare_enrolments(group_a, group_b)  # type: ignore[arg-type]
        ref = reference_compare_enrolments(group_a, group_b)  # type: ignore[arg-type]
        expected = row["expected"]
        comparisons.append(
            {
                "case": row["case"],
                "actual": actual,
                "reference": ref,
                "expected": expected,
                "matches_reference": actual == ref,
                "matches_table": actual == expected,
            }
        )
    return comparisons


if __name__ == "__main__":
    fixture_result = compare_enrolments({"Ana", "Bo"}, {"Bo", "Cy"})
    print("Intersection:", fixture_result["intersection"])
    print("First-only:", fixture_result["first-only"])
    print("Union:", fixture_result["union"])
