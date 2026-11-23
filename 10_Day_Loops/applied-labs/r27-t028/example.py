"""Day 10 Applied Lab (R27-T028): Run-Length Encoding Input-Scale Experiment.

Contract:
- Convert consecutive repeated symbols into `(symbol, count)` pairs.
- `"aaabbc"` -> `[("a", 3), ("b", 2), ("c", 1)]`; `""` -> `[]`; `"aaa"` -> `[("a", 3)]`.
- Contribution focus: Check three bounded input sizes or repeated interaction counts;
  assert correctness and report operation counts rather than imposing a speed threshold.
"""

from __future__ import annotations

from typing import Dict, List, Tuple


def run_length_encode_with_stats(text: str) -> Tuple[List[Tuple[str, int]], Dict[str, int]]:
    """Run-length encode `text` and return `(encoded_pairs, operation_stats)`.

    Operation stats reported:
    - `input_length`: `len(text)`
    - `symbol_inspections`: number of loop iterations over characters (equals `len(text)`)
    - `comparisons`: number of adjacent-symbol comparisons (`max(0, len(text) - 1)`)
    - `run_emissions`: number of `(symbol, count)` pairs emitted (`len(encoded_pairs)`)
    """
    if not text:
        return [], {
            "input_length": 0,
            "symbol_inspections": 0,
            "comparisons": 0,
            "run_emissions": 0,
        }

    encoded: List[Tuple[str, int]] = []
    current_symbol = text[0]
    current_count = 1
    symbol_inspections = 1
    comparisons = 0

    for char in text[1:]:
        symbol_inspections += 1
        comparisons += 1
        if char == current_symbol:
            current_count += 1
        else:
            encoded.append((current_symbol, current_count))
            current_symbol = char
            current_count = 1

    encoded.append((current_symbol, current_count))
    return encoded, {
        "input_length": len(text),
        "symbol_inspections": symbol_inspections,
        "comparisons": comparisons,
        "run_emissions": len(encoded),
    }


def run_length_encode(text: str) -> List[Tuple[str, int]]:
    """Convert consecutive repeated symbols in `text` into `(symbol, count)` pairs."""
    encoded, _ = run_length_encode_with_stats(text)
    return encoded


def run_input_scale_experiment() -> List[Dict[str, object]]:
    """Check three bounded input sizes (0, 6, 60) and report exact operation counts."""
    bounded_inputs = [
        ("empty_scale_0", ""),
        ("small_scale_6", "aaabbc"),
        ("medium_scale_60", "aaabbc" * 10),
    ]
    report: List[Dict[str, object]] = []
    for label, sample in bounded_inputs:
        encoded, stats = run_length_encode_with_stats(sample)
        report.append(
            {
                "label": label,
                "input_length": stats["input_length"],
                "encoded": encoded,
                "stats": stats,
            }
        )
    return report


if __name__ == "__main__":
    print('encode("aaabbc") =', run_length_encode("aaabbc"))
    print('encode("")       =', run_length_encode(""))
    print('encode("aaa")    =', run_length_encode("aaa"))
    for row in run_input_scale_experiment():
        print(f"{row['label']}: stats={row['stats']}")
