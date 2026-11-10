# R27-T056: Environment reporting without exposing secrets

`report_environment()` generates a structured JSON report of system and Python interpreter metadata without leaking credentials or environment variables.

## Behavior and Guarantees

- **Structured Output**: Emits JSON with `executable`, `version`, and `system`.
- **Secret Safety**: Does not access or expose `os.environ`, ensuring unknown environment variables, secrets, and credentials remain absent.
- **Input-Scale Experiment**: Evaluates three bounded input sizes (`(1, 5, 20)`) and tracks exact operation counts to verify correctness without imposing fragile wall-clock speed thresholds.

## Run the tests

From the repository root:

    python3 -m unittest discover -s 23_Day_Virtual_environment/applied-labs/r27-t056 -p "test_*.py"
