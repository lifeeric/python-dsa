import unittest
from src._7_hash_tables import HashTable


class HashTableTest(unittest.TestCase):
    def setUp(self) -> None:
        self.h = HashTable()
        self.h.insert("Apple", 10)

    def test_insert(self) -> None:
        self.assertEqual(self.h.lookup("Apple"), ("Apple", 10))

    def test_delete(self) -> None:
        self.assertIsNone(self.h.delete("Apple"))
        self.assertEqual(self.h.lookup("Apple"), None)

    def test_lookup(self) -> None:
        self.assertEqual(self.h.lookup("Apple"), ("Apple", 10))
