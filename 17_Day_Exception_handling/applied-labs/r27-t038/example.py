from typing import Any, Dict, Optional, Set, Tuple

def merge_keywords(
    defaults: Dict[str, Any],
    overrides: Dict[str, Any],
    allowed_keys: Optional[Set[str]] = None,
) -> Dict[str, Any]:
    """Merge defaults with keyword overrides using an explicit allowed-key set."""
    if allowed_keys is None:
        allowed_keys = set(defaults.keys())

    for key in overrides:
        if key not in allowed_keys:
            raise KeyError(f"Unknown keyword '{key}'. Allowed keys: {sorted(allowed_keys)}")

    merged = dict(defaults)
    merged.update(overrides)
    return merged

def process_with_recovery(
    defaults: Dict[str, Any],
    overrides: Dict[str, Any]
) -> Tuple[bool, Dict[str, Any], Optional[str]]:
    """Demonstrates handling an error followed by recovery without restarting."""
    try:
        res = merge_keywords(defaults, overrides)
        return True, res, None
    except KeyError as err:
        return False, dict(defaults), str(err)

if __name__ == "__main__":
    defs = {"limit": 10, "reverse": False}
    ok1, r1, e1 = process_with_recovery(defs, {"limt": 3})
    print(f"Attempt 1 (invalid): ok={ok1}")
    ok2, r2, e2 = process_with_recovery(defs, {"limit": 3})
    print(f"Attempt 2 (valid): ok={ok2}, result={r2}")
