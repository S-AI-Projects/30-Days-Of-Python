import argparse
import sys
from typing import Callable, List, Optional

def count_words(text: str, storage_reader: Optional[Callable[[str], str]] = None) -> int:
    """Count words in text string, with optional injected storage reader."""
    if storage_reader and text.startswith("storage://"):
        content = storage_reader(text)
    else:
        content = text
    return len(content.split())

def cli(args: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(prog="wordcount", description="Count words in text")
    parser.add_argument("text", nargs="*", help="Text to count words from")
    parsed = parser.parse_args(args)
    input_text = " ".join(parsed.text)
    count = count_words(input_text)
    print(count)
    return 0

if __name__ == "__main__":
    sys.exit(cli(sys.argv[1:]))
