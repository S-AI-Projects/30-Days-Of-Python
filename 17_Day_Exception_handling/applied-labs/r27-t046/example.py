DEFAULTS = {"limit": 10, "reverse": False}
ALLOWED = {"limit", "reverse"}  # the explicit allowed-key set


# --- Step 1: the WORKING VERSION. It does two jobs in one function. ---
def merge_options_original(defaults, allowed, /, **overrides):
    unknown = sorted(key for key in overrides if key not in allowed)
    if unknown:
        raise ValueError(f"Unknown option(s): {', '.join(unknown)}")
    merged = dict(defaults)
    merged.update(overrides)
    return merged


# --- Step 2: ONE clearly named responsibility, extracted. ---
def reject_unknown_keys(overrides, allowed):
    """Raise ValueError naming every override key that is not allowed."""
    unknown = sorted(key for key in overrides if key not in allowed)
    if unknown:
        raise ValueError(f"Unknown option(s): {', '.join(unknown)}")


# --- Step 3: the REFACTORED VERSION. Same contract, clearer structure. ---
def merge_options(defaults, allowed, /, **overrides):
    """Merge defaults with keyword overrides.

    Only keys in `allowed` may be overridden; any other key raises
    ValueError. `defaults` and `overrides` are never modified.
    `defaults` and `allowed` are positional-only, so an override that is
    literally named "defaults" or "allowed" is rejected as an unknown key
    instead of clashing with the parameter names.
    """
    reject_unknown_keys(overrides, allowed)
    merged = dict(defaults)
    merged.update(overrides)
    return merged


if __name__ == "__main__":
    print(merge_options(DEFAULTS, ALLOWED, limit=3))
    try:
        merge_options(DEFAULTS, ALLOWED, limt=3)  # typo for "limit"
    except ValueError as exc:
        print(f"rejected: {exc}")
        