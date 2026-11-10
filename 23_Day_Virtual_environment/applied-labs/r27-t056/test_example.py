import json
import os
import unittest
from unittest.mock import patch

from example import (
    BOUNDED_INPUT_SIZES,
    report_environment,
    run_bounded_experiment,
)


class TestEnvironmentReporting(unittest.TestCase):
    def test_json_contains_required_keys(self):
        report_str = report_environment()
        data = json.loads(report_str)

        self.assertIn("executable", data)
        self.assertIn("version", data)
        self.assertIn("system", data)

        # Ensure only allowed metadata keys are exposed
        self.assertEqual(set(data.keys()), {"executable", "version", "system"})
        self.assertTrue(len(data["executable"]) > 0)
        self.assertTrue(len(data["version"]) > 0)
        self.assertTrue(len(data["system"]) > 0)

    def test_credentials_and_secrets_are_absent(self):
        sensitive_env = {
            "SECRET_KEY": "supersecret123",
            "DATABASE_PASSWORD": "mypassword",
            "API_TOKEN": "token_abc_xyz",
            "AWS_SECRET_ACCESS_KEY": "awssecret",
        }
        with patch.dict(os.environ, sensitive_env, clear=False):
            report_str = report_environment()
            data = json.loads(report_str)

            for secret_key, secret_val in sensitive_env.items():
                self.assertNotIn(secret_key, data)
                self.assertNotIn(secret_val, report_str)

    def test_three_bounded_input_sizes_operation_counts(self):
        bounded_sizes = (1, 5, 20)
        metrics = run_bounded_experiment(bounded_sizes)

        # Assert exactly three bounded input experiments executed
        self.assertEqual(len(metrics), 3)

        for metric in metrics:
            expected_ops = metric["input_size"]
            actual_ops = metric["operation_count"]
            # Assert operation counts match bounded interaction count
            self.assertEqual(actual_ops, expected_ops)

            # Assert correctness of report
            report_data = json.loads(metric["report"])
            self.assertEqual(
                set(report_data.keys()), {"executable", "version", "system"}
            )

    def test_custom_values_formatting(self):
        custom_report = report_environment(
            custom_executable="/opt/custom/python",
            custom_version="3.15.2",
            custom_system="Linux",
        )
        self.assertEqual(
            json.loads(custom_report),
            {
                "executable": "/opt/custom/python",
                "version": "3.15.2",
                "system": "Linux",
            },
        )


if __name__ == "__main__":
    unittest.main()

