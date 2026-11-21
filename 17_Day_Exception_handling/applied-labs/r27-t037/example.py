from typing import Any, Dict, Optional, Set

def merge_keywords(
    defaults: Dict[str, Any],
    overrides: Dict[str, Any],
    allowed_keys: Optional[Set[str]] = None,
) -> Dict[str, Any]:
    """
    Merge defaults with keyword overrides using an explicit allowed-key set.
    Step 1: Validate allowed keys (rejects unknown keys with KeyError).
    Step 2: Create intermediate copy of defaults.
    Step 3: Apply overrides and return final state.
    """
    if allowed_keys is None:
        allowed_keys = set(defaults.keys())

    for key in overrides:
        if key not in allowed_keys:
            raise KeyError(f"Unknown keyword '{key}'. Allowed keys: {sorted(allowed_keys)}")

    merged = dict(defaults)
    merged.update(overrides)
    return merged

if __name__ == "__main__":
    d = {"limit": 10, "reverse": False}
    print(merge_keywords(d, {"limit": 3}))
