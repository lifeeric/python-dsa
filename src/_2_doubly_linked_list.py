from typing import Optional, Dict, List, Union, Generator


class Node:
    def __init__(
        self,
        value: Optional[Union[str, int, Dict, List]] = None,
        prev: Optional["Node"] = None,
        next: Optional["Node"] = None,
    ) -> None:
        self.value = value
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.count = 0

    def insert(self, value) -> None:
        """insert at the beginning"""
        new_node: None = Node(value, None, None)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.count += 1

    def append(self, value) -> None:
        """append at the end"""
        new_node = Node(value, None, None)

        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

    def append_at_location(self, value, target) -> None:
        current = self.head
        prev = self.head

        new_node = Node(value, None, None)

        while current:
            if current.value == target:
                new_node.prev = prev
                new_node.next = current

                prev.next = new_node
                current.prev = new_node

                self.count += 1

            prev = current
            current = current.next

    def iter(self) -> Generator:
        current = self.head
        while current:
            value = current.value
            current = current.next
            yield value

    def contains(self, value):
        for node_value in self.iter():
            if value == node_value:
                print("[Exists] item exists in list.")
                return
        print("[NOT_FOUND] item not found in list.")
        return

    def remove(self, value):
        current = self.head
        node_deleted = False

        if current is None:
            print("Item is empty")
        elif current.value == value:
            """Item found at the start"""
            self.head = current.next
            self.head.prev = None
            node_deleted = True
        elif self.tail.value == value:
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True
        else:

            while current:
                if current.value == value:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted = True
                current = current.next
        if node_deleted:
            self.count -= 1
            return

        print("[NOT_FOUND]")


words = DoublyLinkedList()

words.append("egg")
words.append("Home")
words.insert("ham")
words.insert("spam")

print(f"Item:")
current = words.head
while current:
    print(current.value)
    current = current.next

# words.insert("Book")
words.append_at_location("bam", "ham")
words.contains("bam")
words.remove("egg")

print(f"\nItem 2:")
current = words.head
while current:
    print(current.value)
    current = current.next
