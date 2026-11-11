import unittest

from example import DuplicateIDError, InMemoryDocumentStore


class InMemoryDocumentStoreTests(unittest.TestCase):
    def test_insert_and_find(self) -> None:
        store = InMemoryDocumentStore()

        self.assertIsNone(store.find(1))
        store.insert({"id": 1, "name": "Ada"})
        self.assertEqual(store.find(1), {"id": 1, "name": "Ada"})

    def test_duplicate_rejection_then_valid_update_recovers(self) -> None:
        store = InMemoryDocumentStore()
        store.insert({"id": 1, "name": "Ada"})

        with self.assertRaisesRegex(DuplicateIDError, "id 1 already exists"):
            store.insert({"id": 1, "name": "Duplicate"})

        self.assertEqual(store.find(1), {"id": 1, "name": "Ada"})
        self.assertTrue(store.update(1, {"name": "Grace"}))
        self.assertEqual(store.find(1), {"id": 1, "name": "Grace"})

    def test_update_missing_document_returns_false(self) -> None:
        store = InMemoryDocumentStore()

        self.assertFalse(store.update(1, {"name": "Grace"}))
        self.assertIsNone(store.find(1))


if __name__ == "__main__":
    unittest.main()
