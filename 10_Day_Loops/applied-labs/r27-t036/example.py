from typing import List, Tuple

def extract_run(sequence: str, start: int) -> Tuple[str, int, int]:
    """Extracted responsibility: extract a single consecutive run of identical symbols."""
    char = sequence[start]
    idx = start
    while idx < len(sequence) and sequence[idx] == char:
        idx += 1
    return char, idx - start, idx

def run_length_encode(sequence: str) -> List[Tuple[str, int]]:
    """Convert consecutive repeated symbols into (symbol, count) pairs."""
    if not sequence:
        return []
    
    encoded = []
    idx = 0
    while idx < len(sequence):
        symbol, count, idx = extract_run(sequence, idx)
        encoded.append((symbol, count))
    return encoded

if __name__ == "__main__":
    print(run_length_encode("aaabbc"))
