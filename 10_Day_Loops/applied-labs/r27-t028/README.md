# Day 10 Applied Lab (`R27-T028`): Run-Length Encoding Input-Scale Experiment

## Overview
This applied lab converts consecutive repeated symbols into `(symbol, count)` tuples in a single pass and reports deterministic operation counts (`symbol_inspections`, `comparisons`, `run_emissions`) across three bounded input sizes rather than relying on wall-clock speed thresholds.

## Contract & Bounded Input-Scale Table

| Bounded Input | Input String | Expected Output | `symbol_inspections` | `comparisons` | `run_emissions` |
| :--- | :--- | :--- | :---: | :---: | :---: |
| Scale $N=0$ | `""` | `[]` | `0` | `0` | `0` |
| Single-run $N=3$ | `"aaa"` | `[("a", 3)]` | `3` | `2` | `1` |
| Scale $N=6$ | `"aaabbc"` | `[("a", 3), ("b", 2), ("c", 1)]` | `6` | `5` | `3` |
| Scale $N=60$ | `"aaabbc" * 10` | `[("a", 3), ("b", 2), ("c", 1)] * 10` | `60` | `59` | `30` |

## Running the Example and Tests
From the repository root:

```bash
python3 10_Day_Loops/applied-labs/r27-t028/example.py
python3 -m unittest discover -s 10_Day_Loops/applied-labs/r27-t028 -p "test_*.py"
```
