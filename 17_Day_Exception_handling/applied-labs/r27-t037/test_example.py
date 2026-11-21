import unittest

try:
    from .example import merge_keywords
except (ImportError, ValueError):
    from example import merge_keywords

class TestKeywordMerging(unittest.TestCase):
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

    def test_no_overrides(self):
        defaults = {"limit": 10, "reverse": False}
        result = merge_keywords(defaults, {})
        self.assertEqual(result, {"limit": 10, "reverse": False})

    def test_override_multiple_keys(self):
        defaults = {"limit": 10, "reverse": False}
        overrides = {"limit": 5, "reverse": True}
        result = merge_keywords(defaults, overrides)
        self.assertEqual(result, {"limit": 5, "reverse": True})

if __name__ == "__main__":
    unittest.main()
