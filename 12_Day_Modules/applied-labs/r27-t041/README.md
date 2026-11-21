# Applied Lab R27-T041: Temperature Conversion Module and CLI

Added activity (not an original numbered exercise).

Splits temperature conversion into an importable module and a CLI
protected by a main guard (`if __name__ == "__main__":`).

- Input: `0` Celsius
- Expected: `32` Fahrenheit
- Input: `100` Celsius
- Expected: `212` Fahrenheit
- Importing the module prints nothing and never reads input.

## Smallest useful complete example

As a module:

```python
import example
print(example.celsius_to_fahrenheit(100))  # 212.0
```

As a CLI (type `100` and press Enter when asked):

    python3 example.py

It prints `100 C = 212 F`.

## Run the tests

From the repository root:

    python3 -m unittest discover -s 12_Day_Modules/applied-labs/r27-t041 -p "test_*.py"

## Why the main guard matters

When Python imports a file, it runs the whole file. Without the guard,
`import example` would immediately ask for input and print. With the
guard, `main()` runs only when the file is executed directly. The test
`test_import_prints_nothing_and_never_reads_input` imports the module in
a fresh process with standard input closed, and checks that nothing is
printed and nothing crashes.