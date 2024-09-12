from typing import Optional, List


class MinHeap:
    def __init__(self) -> None:
        self.heap: List[int] = []

    def parent(self, i: int) -> int:
        return (i - 1) // 2

    def left_child(self, i: int) -> int:
        return 2 * i + 1

    def right_child(self, i: int) -> int:
        return 2 * i + 2

    def swap(self, i: int, j: int) -> int:
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insert(self, data: int) -> int:
        self.heap.append(data)
        self._heapify_up(len(self.heap) - 1)

    def remove_min(self) -> None:
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)

        return min_value

    def remove(self, idx: int) -> None:
        if idx >= len(self.heap) and idx < 0:
            return None

        if idx == len(self.heap) - 1:
            return self.heap.pop()

        deleted = self.heap[idx]
        self.heap[idx] = self.heap.pop()

        if self.heap[idx] < self.heap[self.parent(idx)]:
            self._heapify_up(idx)
        else:
            self._heapify_down(idx)

        return deleted

    def sort(self) -> None:
        heap_copy: List[int] = self.heap.copy()
        sorted_heap: List[int] = []

        while self.heap:
            sorted_heap.append(self.remove_min())

        self.heap = heap_copy
        return sorted_heap

    def _heapify_up(self, idx: int) -> None:
        parent = self.parent(idx)

        if idx > 0 and self.heap[idx] < self.heap[parent]:
            self.swap(idx, parent)
            self._heapify_up(parent)

    def _heapify_down(self, idx: int) -> None:
        min_index = idx
        left_child = self.left_child(idx)
        right_child = self.right_child(idx)

        if left_child < len(self.heap) and self.heap[left_child] < self.heap[min_index]:
            min_index = left_child
        if (
            right_child < len(self.heap)
            and self.heap[right_child] < self.heap[min_index]
        ):
            min_index = right_child

        if min_index != idx:
            self.swap(idx, min_index)
            self._heapify_down(min_index)


h = MinHeap()
# h.insert(5)
# h.insert(8)
# h.insert(2)
# h.insert(9)
# h.insert(1)

# # h.remove_min()
# # h.remove(1)


# print(h.sort())

h.insert(5)
h.insert(6)
h.insert(8)
h.insert(4)
h.insert(2)


print(h.heap)
print(h.sort())

h.remove(2)
print(h.heap)
print(h.sort())
