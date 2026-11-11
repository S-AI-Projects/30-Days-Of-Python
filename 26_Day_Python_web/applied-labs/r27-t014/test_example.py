import unittest

from example import create_app, handle_add


ERROR_BODY = {"error": "Expected a JSON object with numeric 'a' and 'b'."}
CASES = (
    ("integer addition", {"a": 2, "b": 3}, (200, {"sum": 5})),
    ("decimal addition", {"a": 1.5, "b": 2.25}, (200, {"sum": 3.75})),
    ("missing b", {"a": 2}, (400, ERROR_BODY)),
    ("string a", {"a": "2", "b": 3}, (400, ERROR_BODY)),
    ("string b", {"a": 2, "b": "3"}, (400, ERROR_BODY)),
    ("boolean input", {"a": True, "b": 3}, (400, ERROR_BODY)),
)


class AddRequestHandlerTests(unittest.TestCase):
    def test_every_fixture_result(self):
        for name, payload, expected in CASES:
            with self.subTest(name=name):
                self.assertEqual(handle_add(payload), expected)

    def test_invariant_holds_across_a_sequence_of_requests(self):
        sequence = (CASES[0], CASES[2], CASES[1])
        for name, payload, expected in sequence:
            with self.subTest(name=name):
                original_payload = payload.copy()
                actual = handle_add(payload)

                self.assertEqual(actual, expected)
                self.assertEqual(payload, original_payload)
                if expected[0] == 200:
                    self.assertEqual(actual[1]["sum"], payload["a"] + payload["b"])


class FlaskAdapterTests(unittest.TestCase):
    def test_post_route_returns_every_fixture_result(self):
        client = create_app().test_client()
        for name, payload, expected in CASES:
            with self.subTest(name=name):
                response = client.post("/add", json=payload)

                self.assertEqual(response.status_code, expected[0])
                self.assertEqual(response.get_json(), expected[1])


if __name__ == "__main__":
    unittest.main()
