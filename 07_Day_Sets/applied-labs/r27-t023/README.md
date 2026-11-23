# Day 7 Applied Lab (`R27-T023`): Enrolment Sets Reference Comparison Lab

## Overview
This lab calculates enrolment overlap between two student sets (`intersection`, `first-only`, and `union`) and compares the Python set-method implementation (`intersection`, `difference`, `union`) against both an independent expected-result table and a simple membership-loop reference implementation.

## Expected-Result Table

| Case | Group A | Group B | `intersection` | `first-only` | `union` |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `contract_fixture` | `{"Ana", "Bo"}` | `{"Bo", "Cy"}` | `{"Bo"}` | `{"Ana"}` | `{"Ana", "Bo", "Cy"}` |
| `disjoint_groups` | `{"Ana"}` | `{"Cy"}` | `set()` | `{"Ana"}` | `{"Ana", "Cy"}` |
| `identical_groups` | `{"Ana", "Bo"}` | `{"Ana", "Bo"}` | `{"Ana", "Bo"}` | `set()` | `{"Ana", "Bo"}` |
| `empty_first_group` | `set()` | `{"Bo", "Cy"}` | `set()` | `set()` | `{"Bo", "Cy"}` |

## Running the Example and Tests
From the repository root:

```bash
python3 07_Day_Sets/applied-labs/r27-t023/example.py
python3 -m unittest discover -s 07_Day_Sets/applied-labs/r27-t023 -p "test_*.py"
```
