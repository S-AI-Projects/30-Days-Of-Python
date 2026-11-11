import json
from collections.abc import Callable, Mapping
from pathlib import Path


FIXTURE_PATH = Path(__file__).with_name("students.json")


def load_groups(path: Path = FIXTURE_PATH) -> dict[str, list[str]]:
    with path.open(encoding="utf-8") as fixture:
        return json.load(fixture)


def calculate_membership(
    groups: Mapping[str, list[str]],
) -> dict[str, list[str]]:
    group_a = set(groups["A"])
    group_b = set(groups["B"])
    return {
        "intersection": sorted(group_a & group_b),
        "first_only": sorted(group_a - group_b),
        "union": sorted(group_a | group_b),
    }


def run(
    storage: Callable[[], Mapping[str, list[str]]],
) -> dict[str, list[str]]:
    return calculate_membership(storage())


def main() -> None:
    print(json.dumps(run(load_groups), indent=2))


if __name__ == "__main__":
    main()
