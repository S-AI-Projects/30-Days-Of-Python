from typing import Any, Dict

def arithmetic_report(a: Any, b: Any) -> Dict[str, int]:
    """
    Return sum, difference, and product for two integers.
    Handles boundary values (0, 0) and rejects non-integer or empty inputs.
    """
    if a is None or b is None:
        raise ValueError("Inputs cannot be None or empty.")
    
    if isinstance(a, bool) or isinstance(b, bool):
        raise TypeError("Inputs must be integers, not booleans.")
    
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Inputs must be integers.")
    
    return {
        "sum": a + b,
        "difference": a - b,
        "product": a * b
    }
