import unittest
import sort

lines = [
    "2.0",
    "2.1",
    "2.2",
    "2.10",
    "3.1",
    "1.0",
    "2.3",
    "1.0.1",
    "2.4",
    "3.0",
    "2.5",
    "2.6",
    "4.0",
    "2.7",
    "1.1",
    "2.8",
    "4.1",
    "5.0",
    "2.9",
]


class TestSort(unittest.TestCase):

    def test_sort(self):
        expected = [
            "1.0",
            "1.0.1",
            "1.1",
            "2.0",
            "2.1",
            "2.2",
            "2.3",
            "2.4",
            "2.5",
            "2.6",
            "2.7",
            "2.8",
            "2.9",
            "2.10",
            "3.0",
            "3.1",
            "4.0",
            "4.1",
            "5.0"
        ]
        result = do_sort(lines)
        self.assertEqual(result, expected)


def do_sort(to_sort):
    return sort.quick_sort(to_sort, 0, len(to_sort) - 1)


if __name__ == "__main__":
    unittest.main()
