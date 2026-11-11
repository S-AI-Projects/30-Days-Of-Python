import unittest
from pathlib import Path

from example import FIXTURE_PATH, load_groups, run


EXPECTED = {
    "intersection": ["Bo"],
    "first_only": ["Ana"],
    "union": ["Ana", "Bo", "Cy"],
}


class MembershipTests(unittest.TestCase):
    def test_injected_local_storage_produces_expected_results(self) -> None:
        reads = []

        def fixture_storage():
            reads.append(FIXTURE_PATH)
            return load_groups(FIXTURE_PATH)

        self.assertEqual(EXPECTED, run(fixture_storage))
        self.assertEqual([FIXTURE_PATH], reads)

    def test_independent_fixture_reads_agree(self) -> None:
        def first_storage():
            return load_groups(Path(FIXTURE_PATH))

        def second_storage():
            return load_groups(Path(FIXTURE_PATH))

        first_run = run(first_storage)
        second_run = run(second_storage)

        self.assertIsNot(first_storage, second_storage)
        self.assertEqual(EXPECTED, first_run)
        self.assertEqual(EXPECTED, second_run)
        self.assertEqual(first_run, second_run)


if __name__ == "__main__":
    unittest.main()
