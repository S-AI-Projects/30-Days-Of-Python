"""A small in-memory document store, separate from a real MongoDB connection."""

from collections.abc import Mapping
from typing import Protocol

Document = dict[str, object]


class DuplicateIDError(ValueError):
    """Raised when a document uses an ID that is already stored."""


class DocumentStore(Protocol):
    def insert(self, document: Mapping[str, object]) -> None: ...

    def find(self, document_id: int) -> Document | None: ...

    def update(self, document_id: int, changes: Mapping[str, object]) -> bool: ...


class InMemoryDocumentStore:
    """Store document copies in a dictionary for local examples and tests."""

    def __init__(self) -> None:
        self._documents: dict[int, Document] = {}

    def insert(self, document: Mapping[str, object]) -> None:
        document_id = document.get("id")
        if type(document_id) is not int:
            raise ValueError("document must include an integer 'id'")
        if document_id in self._documents:
            raise DuplicateIDError(f"document with id {document_id} already exists")
        self._documents[document_id] = dict(document)

    def find(self, document_id: int) -> Document | None:
        document = self._documents.get(document_id)
        return dict(document) if document is not None else None

    def update(self, document_id: int, changes: Mapping[str, object]) -> bool:
        if "id" in changes:
            raise ValueError("document IDs cannot be changed")
        document = self._documents.get(document_id)
        if document is None:
            return False
        document.update(changes)
        return True


def main() -> None:
    store: DocumentStore = InMemoryDocumentStore()
    print(f"Initial find id 1: {store.find(1)}")

    store.insert({"id": 1, "name": "Ada"})
    print(f"Inserted: {store.find(1)}")

    try:
        store.insert({"id": 1, "name": "Duplicate"})
    except DuplicateIDError as error:
        print(f"Duplicate rejected: {error}")

    if not store.update(1, {"name": "Grace"}):
        raise LookupError("cannot update missing document with id 1")
    print("Recovered on the next valid input: updated name to Grace")
    print(f"Find id 1: {store.find(1)}")


if __name__ == "__main__":
    main()
