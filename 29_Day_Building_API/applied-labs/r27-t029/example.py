"""Day 29 Applied Lab (R27-T029): Installable Mini-Package & Regression-Focused Lab.

Contract:
- Create an installable package exposing a `word_count` function and a CLI entry point
  (`r27-wordcount`).
- The installed CLI counts `"a b a"` as `3` words and returns exit `0`; `--help` works
  outside the source directory.
- Contribution focus: Create a temporary one-line mutant of the decisive condition
  (`len(set(tokens))` instead of `len(tokens)`); add a focused test that passes on the
  correct example and fails on that mutant.
"""

from __future__ import annotations

import os
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Callable, Dict

sys.path.insert(0, str(Path(__file__).resolve().parent))
from wordcount_pkg import word_count, word_count_unique_mutant  # noqa: E402
from wordcount_pkg.cli import main as cli_main  # noqa: E402


def verify_repeated_word_contract(counter_fn: Callable[[str], int]) -> bool:
    """Focused regression predicate: `"a b a"` must count as 3 words (not 2 unique words)."""
    return counter_fn("a b a") == 3


def install_and_exercise_cli() -> Dict[str, object]:
    """Install the package into a temporary prefix and invoke the installed CLI outside the source dir."""
    pkg_root = Path(__file__).resolve().parent
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        install_target = tmp_path / "site_pkg"
        outside_cwd = tmp_path / "outside_workdir"
        outside_cwd.mkdir(parents=True, exist_ok=True)

        install_cmd = [
            sys.executable,
            "-m",
            "pip",
            "install",
            "--no-deps",
            "--no-build-isolation",
            "--target",
            str(install_target),
            str(pkg_root),
        ]
        subprocess.run(install_cmd, check=True, capture_output=True, text=True)

        cli_script = install_target / "bin" / "r27-wordcount"
        env = dict(os.environ)
        env["PYTHONPATH"] = str(install_target)

        count_proc = subprocess.run(
            [str(cli_script), "a b a"],
            cwd=str(outside_cwd),
            env=env,
            capture_output=True,
            text=True,
            check=False,
        )
        help_proc = subprocess.run(
            [str(cli_script), "--help"],
            cwd=str(outside_cwd),
            env=env,
            capture_output=True,
            text=True,
            check=False,
        )

        return {
            "count_exit_code": count_proc.returncode,
            "count_stdout": count_proc.stdout.strip(),
            "help_exit_code": help_proc.returncode,
            "help_stdout": help_proc.stdout.strip(),
        }


if __name__ == "__main__":
    print('word_count("a b a") =', word_count("a b a"))
    print('mutant("a b a")     =', word_count_unique_mutant("a b a"))
    print("CLI check outside source dir:", install_and_exercise_cli())
