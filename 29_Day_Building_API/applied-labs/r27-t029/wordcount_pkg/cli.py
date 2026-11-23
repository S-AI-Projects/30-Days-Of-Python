"""CLI entry point for `wordcount_pkg` (`r27-wordcount`)."""

from __future__ import annotations

import argparse
import sys
from typing import Optional, Sequence

from wordcount_pkg import word_count


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="r27-wordcount",
        description="Count whitespace-separated words in the provided text.",
    )
    parser.add_argument(
        "text",
        help="Input string whose words will be counted (e.g. 'a b a').",
    )
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    count = word_count(args.text)
    print(count)
    return 0


if __name__ == "__main__":
    sys.exit(main())
