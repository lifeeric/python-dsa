from typing import Any, List, Tuple


class HashTable:

    def __init__(self, size: int = 10) -> None:
        self.size: int = size
        self.table: List[Tuple] = [[] for _ in range(self.size)]

    def _hash(self, key: int) -> int:
        return hash(key) % self.size

    def insert(self, key: Any, val: Any) -> None:
        index = self._hash(key)

        for k, v in enumerate(self.table[index]):
            if v[0] == key:
                self.table[index][k] = (key, val)
                return

        self.table[index].append((key, val))

    def lookup(self, key: Any) -> Any:
        index = self._hash(key)

        for k, v in enumerate(self.table[index]):
            if v[0] == key:
                return self.table[index][k]

        return None

    def delete(self, key: Any) -> None:
        index = self._hash(key)

        for k, v in enumerate(self.table[index]):
            if v[0] == key:
                del self.table[index][k]
                return


if __name__ == "__main__":
    h = HashTable()

    h.insert("Apple", 10)
    h.insert("Banana", 30)
    h.insert("Bon", 12)
    h.insert("Cat", 15)
    print(h.table)
    h.insert("Cat", 13)
    h.delete("Bon")
    print(h.lookup("Cat"))
    print(h.table)
