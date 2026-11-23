# Verification Evidence: R27-T029 (Issue #32)

## Task Summary
- **Issue**: #32 (`R27-T029`: Day 29: installable mini-package — regression-focused lab `[29_Day_Building_API/29_building_API.md]`)
- **Command**: `python3 -m unittest discover -s 29_Day_Building_API/applied-labs/r27-t029 -p "test_*.py" -v`

## Tool Versions
- Python: `Python 3.15.2`
- pip: `pip 26.2.2`
- Git: `git version 2.54.0 (Apple Git-157)`

## Inputs & Expected vs. Actual Results

| Case | Input | Expected Result | Actual Result | Status |
| :--- | :--- | :--- | :--- | :--- |
| `word_count("a b a")` | `"a b a"` | `3` (`verify_repeated_word_contract == True`) | `3` (`True`) | PASS |
| One-line mutant `word_count_unique_mutant("a b a")` | `"a b a"` | `2` (`verify_repeated_word_contract == False`) | `2` (`False`) | PASS |
| Installed CLI `r27-wordcount "a b a"` (outside source dir) | `"a b a"` | `stdout="3"`, `exit_code=0` | `stdout="3"`, `exit_code=0` | PASS |
| Installed CLI `r27-wordcount --help` (outside source dir) | `--help` | `usage: r27-wordcount` in stdout, `exit_code=0` | `usage: r27-wordcount` in stdout, `exit_code=0` | PASS |

## Unittest Output
```text
test_installed_cli_counts_words_and_help_works_outside_source_dir (test_example.TestInstallableWordcountPackage.test_installed_cli_counts_words_and_help_works_outside_source_dir) ... ok
test_regression_focused_mutant_detection (test_example.TestInstallableWordcountPackage.test_regression_focused_mutant_detection) ... ok
test_word_count_function_counts_repeated_words (test_example.TestInstallableWordcountPackage.test_word_count_function_counts_repeated_words) ... ok

----------------------------------------------------------------------
Ran 3 tests in 0.511s

OK
```
