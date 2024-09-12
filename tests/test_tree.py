import unittest
from src._4_tree import Tree


class TreeTest(unittest.TestCase):

    def setUp(self) -> None:
        self.t = Tree()

    def test_insert(self) -> None:
        self.t.insert(5)

        self.assertEqual(self.t.search(5), 5)

    def test_inorder(self) -> None:
        self.t.insert(5)
        self.t.insert(4)
        self.t.insert(2)
        self.t.insert(3)

        self.assertEqual(self.t.inorder(), [2, 3, 4, 5])

    def test_preoder(self) -> None:
        self.t.insert(5)
        self.t.insert(4)
        self.t.insert(2)
        self.t.insert(3)

        self.assertEqual(self.t.preorder(), [5, 4, 2, 3])

    def test_postoder(self) -> None:
        self.t.insert(5)
        self.t.insert(4)
        self.t.insert(2)
        self.t.insert(3)

        self.assertEqual(self.t.postorder(), [3, 2, 4, 5])

    def test_remove(self) -> None:
        self.t.insert(5)
        self.t.insert(4)
        self.t.insert(2)
        self.t.insert(3)

        self.t.remove(2)

        self.assertEqual(self.t.inorder(), [3, 4, 5])
