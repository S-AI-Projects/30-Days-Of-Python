import unittest
from example import dedupe


def check_invariant(test, original, result):
    """The invariant connecting the input to the output."""
    # 1. No repeated items in the result
    test.assertEqual(len(result), len(set(result)))
    # 2. Same distinct items as the input
    test.assertEqual(set(result), set(original))
    # 3. First-occurrence order is kept
    order = sorted(set(original), key=original.index)
    test.assertEqual(result, order)


class TestDedupe(unittest.TestCase):
    def test_main_example(self):
        self.assertEqual(dedupe([3, 1, 3, 2, 1]), [3, 1, 2])

    def test_empty_stays_empty(self):
        self.assertEqual(dedupe([]), [])

    def test_original_unchanged(self):
        original = [3, 1, 3, 2, 1]
        dedupe(original)
        self.assertEqual(original, [3, 1, 3, 2, 1])

    def test_invariant_across_sequence_of_operations(self):
        data = [3, 1, 3, 2, 1]

        first = dedupe(data)
        check_invariant(self, data, first)
        self.assertEqual(data, [3, 1, 3, 2, 1])  # input still unchanged

        # Operation 2: deduping again changes nothing
        second = dedupe(first)
        self.assertEqual(second, first)
        check_invariant(self, first, second)

        # Operation 3: change the input, then dedupe again
        data.append(4)
        data.append(3)
        third = dedupe(data)
        self.assertEqual(third, [3, 1, 2, 4])
        check_invariant(self, data, third)

        # The earlier result was not affected by changing the input
        self.assertEqual(first, [3, 1, 2])


if __name__ == "__main__":
    unittest.main()