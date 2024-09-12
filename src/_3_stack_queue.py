from collections import deque

# size = 3
# data = [0] * (size)
# top = -1


# def push(item) -> None:
#     global top

#     if top >= size - 1:
#         raise Exception("[ERROR] Stack Overflow")

#     top += 1
#     data[top] = item


# def pop() -> None:
#     global top

#     if top == -1:
#         raise Exception("[ERROR] Stack Underflow")

#     popout = data[top]
#     data[top] = 0
#     top -= 1

#     return popout


# def peek():
#     if top == -1:
#         print("Stack empty")
#         return

#     print(data[top])


class QueueList:
    def __init__(self) -> None:
        self.items = deque()
        self.front = self.rear = 0
        self.size = 3

    def enqueue(self, data) -> None:
        if self.rear == self.size:
            print("Queue is full.")
            return
        self.items.append(data)
        self.rear += 1

    def dequeue(self) -> None:
        if self.rear == 0:
            print("Queue is empty.")
            return
        self.rear -= 1
        return self.items.popleft()

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def peek(self) -> str:
        if self.rear == 0:
            print("Queue is empty")
            return
        return self.items[0]
