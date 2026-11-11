"""Compose text transformations into a reusable normalization pipeline."""

from collections.abc import Callable


def strip_text(value: str) -> str:
    return value.strip()


def lowercase_text(value: str) -> str:
    return value.lower()


def collapse_whitespace(value: str) -> str:
    return " ".join(value.split())


def compose(*functions: Callable[[str], str]) -> Callable[[str], str]:
    def composed(value: str) -> str:
        for function in functions:
            value = function(value)
        return value

    return composed


normalize = compose(strip_text, lowercase_text, collapse_whitespace)

EXAMPLES = (
    (" HELLO World ", "hello world"),
    ("  HELLO   World  ", "hello world"),
    ("Mixed\tCASE\nText", "mixed case text"),
)


def main() -> None:
    value = EXAMPLES[1][0]
    after_strip = strip_text(value)
    after_lowercase = lowercase_text(after_strip)
    result = collapse_whitespace(after_lowercase)

    print(f"Input: {value!r}")
    print(f"After strip: {after_strip!r}")
    print(f"After lowercase: {after_lowercase!r}")
    print(f"After whitespace collapse: {result!r}")
    print(f"Normalized again: {normalize(result)!r}")


if __name__ == "__main__":
    main()
