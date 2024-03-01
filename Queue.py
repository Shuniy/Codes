from typing import Optional
from DoublyLinkedList import DoublyLinkedList


class Queue(object):
    def __init__(self, initialItems: list[object]) -> None:
        self.queue: DoublyLinkedList = DoublyLinkedList(initialItems)

    def enqueue(self, value: object) -> None:
        return self.queue.insertAtTail(value)

    def dequeue(self) -> Optional[object]:
        return self.queue.removeFromHead()

    def peek(self) -> Optional[object]:
        return self.queue.getHead()

    def size(self) -> int:
        return self.queue.getLength()


class DeQueue(object):
    def __init__(self, initialItems: list[object]) -> None:
        self.queue: DoublyLinkedList = DoublyLinkedList(initialItems)

    def pushLeft(self, value: object) -> None:
        self.queue.insertAtHead(value)
        return

    def popleft(self) -> Optional[object]:
        return self.queue.removeFromHead()

    def peek(self) -> Optional[object]:
        return self.queue.getHead()

    def size(self) -> int:
        return self.queue.getLength()

    def pushRight(self, value: object) -> None:
        self.queue.insertAtTail(value)
        return

    def popRight(self, value: object) -> Optional[object]:
        return self.queue.removeFromTail()
