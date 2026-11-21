import pathlib
import subprocess
import sys
import unittest

from example import celsius_to_fahrenheit

HERE = pathlib.Path(__file__).parent


class TestConversion(unittest.TestCase):
    def test_zero_celsius(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32)

    def test_hundred_celsius(self):
        self.assertEqual(celsius_to_fahrenheit(100), 212)

    def test_minus_forty_is_the_same_in_both_scales(self):
        self.assertEqual(celsius_to_fahrenheit(-40), -40)


class TestModuleVersusCli(unittest.TestCase):
    def test_import_prints_nothing_and_never_reads_input(self):
        # Fresh process. Standard input is closed, so if the import called
        # input() it would crash with EOFError and the return code would not be 0.
        result = subprocess.run(
            [sys.executable, "-c", "import example"],
            cwd=HERE,
            stdin=subprocess.DEVNULL,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, "")

    def run_cli(self, typed):
        return subprocess.run(
            [sys.executable, str(HERE / "example.py")],
            input=typed,
            capture_output=True,
            text=True,
        )

    def test_cli_converts_zero(self):
        result = self.run_cli("0\n")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("0 C = 32 F", result.stdout)

    def test_cli_converts_hundred(self):
        result = self.run_cli("100\n")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("100 C = 212 F", result.stdout)


if __name__ == "__main__":
    unittest.main()