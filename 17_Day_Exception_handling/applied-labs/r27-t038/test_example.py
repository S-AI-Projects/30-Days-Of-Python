import unittest

try:
    from .example import merge_keywords, process_with_recovery
except (ImportError, ValueError):
    from example import merge_keywords, process_with_recovery

class TestKeywordMergingRecovery(unittest.TestCase):
    def test_fixture_override_limit(self):
        defaults = {"limit": 10, "reverse": False}
        overrides = {"limit": 3}
        result = merge_keywords(defaults, overrides)
        self.assertEqual(result, {"limit": 3, "reverse": False})

    def test_fixture_unknown_key_rejected(self):
        defaults = {"limit": 10, "reverse": False}
        overrides = {"limt": 3}
        with self.assertRaises(KeyError):
            merge_keywords(defaults, overrides)

    def test_failure_and_recovery_without_restart(self):
        defaults = {"limit": 10, "reverse": False}
        ok1, res1, err1 = process_with_recovery(defaults, {"limt": 3})
        self.assertFalse(ok1)
        self.assertIsNotNone(err1)
        self.assertEqual(res1, {"limit": 10, "reverse": False})

        ok2, res2, err2 = process_with_recovery(defaults, {"limit": 3})
        self.assertTrue(ok2)
        self.assertIsNone(err2)
        self.assertEqual(res2, {"limit": 3, "reverse": False})

if __name__ == "__main__":
    unittest.main()
