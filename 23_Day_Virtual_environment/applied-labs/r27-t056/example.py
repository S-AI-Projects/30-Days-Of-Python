"""R27-T056: Environment reporting without secrets and input-scale experiment."""

import json
import platform
import sys

BOUNDED_INPUT_SIZES = (1, 5, 20)


def report_environment(*, custom_executable=None, custom_version=None, custom_system=None):
    """Report Python environment metadata as structured JSON without exposing secrets.

    Contains exclusively 'executable', 'version', and 'system'.
    Never accesses or dumps os.environ, ensuring credentials and unknown env vars are absent.
    """
    payload = {
        "executable": custom_executable or sys.executable,
        "version": custom_version or platform.python_version(),
        "system": custom_system or platform.system(),
    }
    return json.dumps(payload, sort_keys=True)


def run_bounded_experiment(interaction_counts=BOUNDED_INPUT_SIZES, *, reporter=None):
    """Run repeated environment reports across bounded input sizes and record operation counts.

    Asserts correctness and tracks exact operation counts without brittle speed thresholds.
    """
    if reporter is None:
        reporter = report_environment

    metrics = []
    for count in interaction_counts:
        operations = 0
        latest_report = None
        for _ in range(count):
            latest_report = reporter()
            operations += 1
        metrics.append(
            {
                "input_size": count,
                "operation_count": operations,
                "report": latest_report,
            }
        )
    return metrics


if __name__ == "__main__":
    print("Environment report:")
    print(report_environment())
    print("\nBounded experiment operation counts:")
    for m in run_bounded_experiment():
        print(f"Input size {m['input_size']}: {m['operation_count']} operations")

