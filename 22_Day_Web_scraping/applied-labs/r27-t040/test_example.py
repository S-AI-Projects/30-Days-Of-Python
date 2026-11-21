import unittest

try:
    from .example import extract_links
except (ImportError, ValueError):
    from example import extract_links

class TestBoundedHtmlExtraction(unittest.TestCase):
    def test_fixture_relative_url_resolution(self):
        html = '<p>Check <a href="/docs">Docs</a> for details.</p>'
        base = "https://example.invalid"
        records = extract_links(html, base)
        self.assertEqual(records, [{"title": "Docs", "link": "https://example.invalid/docs"}])

    def test_links_without_href_skipped(self):
        html = '<a name="top">Top Anchor</a><a href="/docs">Docs</a><a>Empty Link</a>'
        base = "https://example.invalid"
        records = extract_links(html, base)
        self.assertEqual(records, [{"title": "Docs", "link": "https://example.invalid/docs"}])

    def test_mutant_fails_regression_check(self):
        html = '<a>Invalid Link</a><a href="/docs">Docs</a>'
        base = "https://example.invalid"
        correct_records = extract_links(html, base, mutant=False)
        self.assertEqual(len(correct_records), 1)
        self.assertEqual(correct_records[0]["title"], "Docs")

        mutant_records = extract_links(html, base, mutant=True)
        self.assertNotEqual(len(mutant_records), 1)

if __name__ == "__main__":
    unittest.main()
