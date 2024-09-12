from typing import Tuple, List, Any


class PriorityQueue:

    def __init__(self):
        self._heap: List[Tuple] = []

    def push(self, info: Any, priority: int) -> None:
        self._heap.append((info, priority))

        self._heap.sort(key=lambda x: x[1], reverse=True)

    def pop(self) -> int:

        if not self._heap:
            raise IndexError("Error: 'pop' from the empty priority queue.")

        return self._heap.pop(0)[0]

    def peek(self) -> int:
        if not self._heap:
            raise IndexError("Error: 'peek' from the empty priority queue.")

        return self._heap[0][0]

    def is_empty(self) -> int:
        return len(self._heap) == 0

    def __len__(self):
        return len(self._heap)


if __name__ == "__main__":

    pq = PriorityQueue()

    pq.push("Deploy", priority=1)
    pq.push("Testing", priority=2)
    pq.push("Code", priority=3)

    print(pq.peek())

    print("Items in order of priority")
    while not pq.is_empty():
        print(pq.pop())
