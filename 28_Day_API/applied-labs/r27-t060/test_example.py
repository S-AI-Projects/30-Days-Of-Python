import unittest
from example import handle_request, handle_request_mutant


class TestHTTPContract(unittest.TestCase):
    def setUp(self):
        self.store = []

    def test_post_valid_item_returns_201(self):
        status, data = handle_request(
            "POST", "/items", '{"id": 1, "name": "notebook"}', store=self.store
        )
        self.assertEqual(status, 201)
        self.assertEqual(data, {"id": 1, "name": "notebook"})
        self.assertEqual(len(self.store), 1)

    def test_get_lists_items(self):
        handle_request(
            "POST", "/items", '{"id": 10, "item": "pen"}', store=self.store
        )
        status, data = handle_request("GET", "/items", store=self.store)
        self.assertEqual(status, 200)
        self.assertEqual(data, [{"id": 10, "item": "pen"}])

    def test_malformed_json_yields_400(self):
        status, data = handle_request(
            "POST", "/items", "{bad:json", store=self.store
        )
        self.assertEqual(status, 400)
        self.assertIn("error", data)

        # None body also rejected
        status_none, _ = handle_request(
            "POST", "/items", None, store=self.store
        )
        self.assertEqual(status_none, 400)

    def test_unsupported_method_yields_405(self):
        for method in ("DELETE", "PUT", "PATCH"):
            status, data = handle_request(method, "/items", store=self.store)
            self.assertEqual(status, 405)
            self.assertEqual(data["error"], "Method Not Allowed")

    def test_focused_regression_passes_on_correct_and_fails_on_mutant(self):
        """Focused test asserting the decisive condition (201 Created on POST).

        Passes on the correct implementation and fails on the mutant.
        """
        def assert_post_creation_contract(handler):
            temp_store = []
            status, _ = handler(
                "POST", "/items", '{"id": 99}', store=temp_store
            )
            if status != 201:
                raise AssertionError(
                    f"Contract violation: expected 201 Created, got {status}"
                )
            return True

        # Correct example must PASS
        self.assertTrue(assert_post_creation_contract(handle_request))

        # Mutant must FAIL
        with self.assertRaises(AssertionError) as cm:
            assert_post_creation_contract(handle_request_mutant)
        self.assertIn("expected 201 Created, got 200", str(cm.exception))


if __name__ == "__main__":
    unittest.main()
