"""Unit tests for Day 28 Applied Lab (R27-T026): HTTP Contract Executable Lesson Example."""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(__file__))
import example  # noqa: E402


class TestHttpContractItemsEndpoint(unittest.TestCase):
    def test_post_valid_item_returns_201_and_get_lists_it(self) -> None:
        store: list[dict[str, object]] = []
        post_resp = example.handle_items_request(
            "POST", "/items", body='{"id": 1, "name": "notebook"}', store=store
        )
        self.assertEqual(post_resp["status"], 201)
        self.assertEqual(post_resp["data"], {"id": 1, "name": "notebook"})

        get_resp = example.handle_items_request("GET", "/items", store=store)
        self.assertEqual(get_resp["status"], 200)
        self.assertEqual(get_resp["data"], [{"id": 1, "name": "notebook"}])

    def test_malformed_json_yields_400_and_does_not_mutate_store(self) -> None:
        store: list[dict[str, object]] = []
        bad_resp = example.handle_items_request(
            "POST", "/items", body='{"id": 2, "broken": ', store=store
        )
        self.assertEqual(bad_resp["status"], 400)
        self.assertEqual(store, [])

    def test_unsupported_method_yields_405(self) -> None:
        store: list[dict[str, object]] = []
        for method in ("DELETE", "PUT", "PATCH"):
            with self.subTest(method=method):
                resp = example.handle_items_request(method, "/items", store=store)
                self.assertEqual(resp["status"], 405)
                self.assertEqual(store, [])

    def test_published_lesson_example_is_executable(self) -> None:
        walkthrough = example.run_published_lesson_example()
        statuses = [step["status"] for step in walkthrough["steps"]]
        self.assertEqual(statuses, [201, 200, 400, 405])
        self.assertEqual(walkthrough["final_store"], [{"id": 1, "name": "notebook"}])


if __name__ == "__main__":
    unittest.main()
