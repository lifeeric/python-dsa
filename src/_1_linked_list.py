from typing import List, Optional, Dict, Union, Any


class Node:
    def __init__(self, value: Optional[Any] = None):
        self.value: Optional[Any] = value
        self.next: Optional["Node"] = None


class SLL:
    def __init__(self):
        self.head = Node()

    def append(self, value):
        new_node = Node(value)
        current = self.head

        while current.next != None:
            current = current.next
        current.next = new_node

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head.next
        self.head.next = new_node

    def length(self):
        current = self.head
        total = 0

        while current.next != None:
            total += 1
            current = current.next

        return total

    def display(self):
        items: List = []

        current = self.head

        while current.next != None:
            current = current.next
            items.append(current.value)

        print(items)

    def get(self, idx: int):
        if idx >= self.length():
            raise Exception("ERROR: 'GET' Index out of range!")

        current_node = self.head
        current_idx = 0

        while True:
            current_node = current_node.next
            if current_idx == idx:
                return current_node.value
            current_idx += 1

    def remove(self, idx: int):
        if idx >= self.length():
            raise Exception("ERROR: 'remove' Index out of ragne!")

        current_idx = 0
        current_node = self.head

        while True:
            last_node = current_node
            current_node = current_node.next
            if current_idx == idx:
                last_node.next = current_node.next
                return
            current_idx += 1


ssl = SLL()
ssl.append(55)
ssl.append("is")
ssl.append(["DSA"])
ssl.append({"name": "eric"})
ssl.append({"name": "XXX"})
ssl.insert("Nice")


ssl.display()
print(ssl.length())

# print(ssl.get(0))

# ssl.remove(4)
# ssl.display()
