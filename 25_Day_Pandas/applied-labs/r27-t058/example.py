"""R27-T058: Small CSV analysis with failure and recovery handling."""


class MalformedRowError(ValueError):
    """Raised when a CSV row contains a malformed amount, identifying the line number."""

    def __init__(self, line_number, raw_value):
        super().__init__(
            f"Malformed amount on line {line_number}: {raw_value!r}"
        )
        self.line_number = line_number
        self.raw_value = raw_value


class CSVAnalyzer:
    """Stateful CSV analyzer demonstrating error recovery without restarting."""

    def __init__(self):
        self.last_status = "uninitialized"
        self.error_count = 0
        self.success_count = 0

    def analyze(self, csv_input):
        """Group supplied CSV by category and calculate count and sum.

        Does not silently drop malformed amounts; raises MalformedRowError
        identifying the exact line number.
        """
        if not isinstance(csv_input, str):
            raise TypeError("csv_input must be a string")

        text = csv_input.strip()
        if not text:
            self.last_status = "empty"
            return {}

        if "\n" in text:
            lines = text.splitlines()
        elif "," in text and ":" in text:
            lines = text.split(",")
        else:
            lines = text.splitlines()

        counts = {}
        sums = {}

        for line_num, line in enumerate(lines, start=1):
            line = line.strip()
            if not line:
                continue

            delim = ":" if ":" in line else ","
            parts = [p.strip() for p in line.split(delim, 1)]
            if len(parts) != 2:
                self.last_status = "error"
                self.error_count += 1
                raise MalformedRowError(line_num, line)

            category, amount_str = parts

            # Skip header line if present
            if (
                line_num == 1
                and category.lower() in ("category", "cat")
                and amount_str.lower() in ("amount", "amt", "value", "sum")
            ):
                continue

            try:
                amount = float(amount_str)
                if amount.is_integer():
                    amount = int(amount)
            except ValueError:
                self.last_status = "error"
                self.error_count += 1
                raise MalformedRowError(line_num, amount_str)

            counts[category] = counts.get(category, 0) + 1
            sums[category] = sums.get(category, 0) + amount

        self.last_status = "success"
        self.success_count += 1
        return {
            category: {"count": counts[category], "sum": sums[category]}
            for category in counts
        }


def analyze_csv(csv_input):
    """Functional wrapper for CSV analysis."""
    return CSVAnalyzer().analyze(csv_input)


if __name__ == "__main__":
    analyzer = CSVAnalyzer()

    # 1. Successful run
    valid_data = "A:2,A:3,B:4"
    print("Valid run:", analyzer.analyze(valid_data))

    # 2. Failure run
    invalid_data = "A:2\nA:invalid\nB:4"
    try:
        analyzer.analyze(invalid_data)
    except MalformedRowError as e:
        print(f"Caught error (line {e.line_number}): {e}")

    # 3. Successful recovery without restarting
    recovered_data = "A:10\nB:20"
    print("Recovered run:", analyzer.analyze(recovered_data))
    print(f"Status: {analyzer.last_status}, successes: {analyzer.success_count}")
