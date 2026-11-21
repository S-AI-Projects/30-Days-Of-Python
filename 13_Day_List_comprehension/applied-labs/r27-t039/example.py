from typing import Dict, Sequence, Tuple

def even_squares_mapping(numbers: Sequence[int]) -> Dict[int, int]:
    """Build a mapping from even integers to their squares without modifying the input."""
    return {x: x**2 for x in numbers if x % 2 == 0}

def instrumented_even_squares(
    numbers: Sequence[int],
) -> Tuple[Dict[int, int], int, int]:
    """Instrumented run returning (mapping, total_evaluated, total_emitted)."""
    checks = 0
    emits = 0
    result = {}
    for x in numbers:
        checks += 1
        if x % 2 == 0:
            result[x] = x**2
            emits += 1
    return result, checks, emits

if __name__ == "__main__":
    inp = [-2, -1, 0, 1, 2]
    print("Mapping:", even_squares_mapping(inp))
