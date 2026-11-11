import unittest

from example import count_words


# This expected-result table is independent of the regex used by count_words.
EXPECTED_RESULTS = {
    "sample": (
        "Tea, tea! isn't coffee.",
        {"tea": 2, "isn't": 1, "coffee": 1},
    ),
    "empty": ("", {}),
    "boundary punctuation": ("'TEA' tea!", {"tea": 2}),
    "internal apostrophe": ("ISN'T isn't", {"isn't": 2}),
    "punctuation only": ("... !!!", {}),
}


class WordCountReferenceTests(unittest.TestCase):
    def assert_matches_reference(self, case_name):
        text, expected = EXPECTED_RESULTS[case_name]
        self.assertEqual(count_words(text), expected)

    def test_sample_sentence(self):
        self.assert_matches_reference("sample")

    def test_empty_input(self):
        self.assert_matches_reference("empty")

    def test_boundary_punctuation_and_case(self):
        self.assert_matches_reference("boundary punctuation")

    def test_internal_apostrophe(self):
        self.assert_matches_reference("internal apostrophe")

    def test_punctuation_only_input(self):
        self.assert_matches_reference("punctuation only")


if __name__ == "__main__":
    unittest.main()
