from html.parser import HTMLParser
from typing import Dict, List, Optional
from urllib.parse import urljoin

class LinkExtractor(HTMLParser):
    def __init__(self, base_url: str, mutant: bool = False):
        super().__init__()
        self.base_url = base_url
        self.mutant = mutant
        self.records: List[Dict[str, str]] = []
        self._current_href: Optional[str] = None
        self._current_text: List[str] = []

    def handle_starttag(self, tag: str, attrs: list):
        if tag == "a":
            attrs_dict = dict(attrs)
            if not self.mutant:
                self._current_href = attrs_dict.get("href")
            else:
                self._current_href = attrs_dict.get("href", "")
            self._current_text = []

    def handle_data(self, data: str):
        if self._current_href is not None:
            self._current_text.append(data)

    def handle_endtag(self, tag: str):
        if tag == "a" and self._current_href is not None:
            title = "".join(self._current_text).strip()
            resolved_link = urljoin(self.base_url, self._current_href)
            self.records.append({"title": title, "link": resolved_link})
            self._current_href = None
            self._current_text = []

def extract_links(html_content: str, base_url: str, mutant: bool = False) -> List[Dict[str, str]]:
    """Parses local HTML into title/link records and resolves relative URLs without network requests."""
    parser = LinkExtractor(base_url, mutant=mutant)
    parser.feed(html_content)
    return parser.records

if __name__ == "__main__":
    sample = '<a href="/docs">Docs</a><a>No Link</a>'
    print(extract_links(sample, "https://example.invalid"))
