import http.client
import json
import threading
import unittest
from wsgiref.simple_server import make_server

from example import InMemoryItemStore, create_app, parse_item_payload


class ItemsEndpointTests(unittest.TestCase):
    def setUp(self):
        self.server = make_server(
            "127.0.0.1", 0, create_app(InMemoryItemStore())
        )
        self.server_thread = threading.Thread(
            target=self.server.serve_forever,
            daemon=True,
        )
        self.server_thread.start()

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        self.server_thread.join()

    def request(self, method, body=None):
        connection = http.client.HTTPConnection(
            "127.0.0.1", self.server.server_port
        )
        headers = {}
        if body is not None:
            headers["Content-Type"] = "application/json"
        connection.request(method, "/items", body=body, headers=headers)
        response = connection.getresponse()
        result = response.status, json.loads(response.read())
        connection.close()
        return result

    def test_post_creates_item_and_get_lists_it(self):
        status, created_item = self.request(
            "POST",
            json.dumps({"name": "notebook"}),
        )
        self.assertEqual(status, 201)
        self.assertEqual(created_item, {"id": 1, "name": "notebook"})

        status, items = self.request("GET")
        self.assertEqual(status, 200)
        self.assertEqual(items, [{"id": 1, "name": "notebook"}])

    def test_malformed_json_returns_400(self):
        status, body = self.request("POST", '{"name":')
        self.assertEqual(status, 400)
        self.assertEqual(body, {"error": "Malformed JSON"})

    def test_unsupported_method_returns_405(self):
        status, body = self.request("PUT")
        self.assertEqual(status, 405)
        self.assertEqual(body, {"error": "Method not allowed"})

    def test_parse_item_payload_has_one_clear_responsibility(self):
        self.assertEqual(
            parse_item_payload(b'{"name": " notebook "}'),
            {"name": "notebook"},
        )
        with self.assertRaisesRegex(ValueError, "Malformed JSON"):
            parse_item_payload(b'{"name":')


if __name__ == "__main__":
    unittest.main()
