import unittest
from src._5_heap import MinHeap


class HeapTest(unittest.TestCase):

    def setUp(self) -> None:
        self.h = MinHeap()
        self.h.insert(5)
        self.h.insert(9)
        self.h.insert(2)
        self.h.insert(10)
        self.h.insert(20)

    def test_insert(self) -> None:

        self.assertEqual(self.h.heap, [2, 9, 5, 10, 20])

    def test_remove(self) -> None:

        self.h.remove(2)

        self.assertEqual(self.h.heap, [2, 9, 20, 10])

    def test_sort(self) -> None:
        self.assertEqual(self.h.sort(), [2, 5, 9, 10, 20])

    def test_min_remove(self) -> None:
        self.h.remove_min()
        self.assertEqual(self.h.heap, [5, 9, 20, 10])
