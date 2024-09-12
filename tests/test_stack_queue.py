import unittest
from src._3_stack_queue import QueueList


class TestQueue(unittest.TestCase):

    def setUp(self) -> None:
        self.q = QueueList()

    def test_enqueue(self) -> None:
        self.q.enqueue("Javscript")
        self.assertFalse(self.q.is_empty())
        self.assertEqual(self.q.peek(), "Javscript")

    def test_dequeue(self) -> None:
        self.q.enqueue("Python")
        self.q.enqueue("Rust")
        self.assertEqual(self.q.dequeue(), "Python")

    def test_is_empty(self) -> None:
        self.q.enqueue("Rust")
        self.q.enqueue("golang")
        self.q.dequeue()
        self.assertFalse(self.q.is_empty())

    def test_peek(self) -> None:
        self.q.enqueue("Rust")
        self.assertEqual(self.q.peek(), "Rust")


if __name__ == "__main__":
    unittest.main()
