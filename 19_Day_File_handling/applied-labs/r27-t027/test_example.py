"""Unit tests for Day 19 Applied Lab (R27-T027): CSV Round Trip Failure and Recovery."""

import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))
import example  # noqa: E402


class TestCsvRoundTripRecovery(unittest.TestCase):
    def test_quoted_comma_record_survives_utf8_file_round_trip(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            csv_path = Path(tmp_dir) / "scores.csv"
            input_records = [{"name": "Ada, Jr.", "score": 7}]
            csv_text = example.write_csv_records(input_records, target=csv_path)
            self.assertIn('"Ada, Jr.",7', csv_text)

            loaded = example.read_csv_records(csv_path)
            self.assertEqual(loaded, [{"name": "Ada, Jr.", "score": 7}])

    def test_empty_data_produces_only_header(self) -> None:
        csv_text = example.write_csv_records([])
        self.assertEqual(csv_text, "name,score\n")
        self.assertEqual(example.read_csv_records(csv_text), [])

    def test_failure_and_empty_state_then_recovery_without_restart(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            session = example.CsvRoundTripSession(Path(tmp_dir) / "session.csv")

            empty_step = session.round_trip([])
            self.assertEqual(empty_step["status"], "empty_header_only")
            self.assertEqual(empty_step["csv_text"], "name,score\n")
            self.assertEqual(empty_step["records"], [])

            error_step = session.round_trip([{"name": "Ada, Jr.", "score": "bad"}])
            self.assertEqual(error_step["status"], "error")
            self.assertIsNotNone(error_step["error"])

            recovered_step = session.round_trip([{"name": "Ada, Jr.", "score": 7}])
            self.assertEqual(recovered_step["status"], "ok")
            self.assertEqual(recovered_step["records"], [{"name": "Ada, Jr.", "score": 7}])
            self.assertEqual(len(session.history), 3)


if __name__ == "__main__":
    unittest.main()
