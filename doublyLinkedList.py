from typing import Optional


class Node(object):
    def __init__(self, value: object | None = None) -> None:
        self.value: object = value
        self.next: Node | None = None
        self.prev: Optional[Node] = None

    def __str__(self) -> str:
        nextValue: Optional[object] = None
        prevValue: Optional[object] = None
        if self.next:
            nextValue = self.next.value

        if self.prev:
            prevValue = self.prev.value
        return f'{prevValue} ---> {self.value} ---> {nextValue}'


class DoublyLinkedList(object):
    def __init__(self, initialItems: list[object]) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.length: int = 0
        if len(initialItems) > 0:
            for item in initialItems:
                self.insertAtTail(item)
            self.length = len(initialItems)

    def getHead(self) -> object:
        if self.head:
            return self.head.value
        else:
            return None

    def getTail(self) -> object:
        if self.tail:
            return self.tail.value
        else:
            return None

    def getLength(self) -> int:
        return self.length

    def asArray(self) -> list[object]:
        result: list[object] = []
        temp = self.head
        while temp:
            result.append(temp.value)
            temp = temp.next
        del temp
        return result

    def asRevertedArray(self) -> list[object]:
        result: list[object] = []
        temp = self.tail
        while temp:
            result.append(temp.value)
            temp = temp.prev
        del temp
        return result

    def insertAtHead(self, value: object) -> None:
        newNode = Node(value)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
        self.length += 1
        return

    def insertAtTail(self, value: object) -> None:
        newNode = Node(value)
        if not self.tail:
            self.tail = newNode
            self.head = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.length += 1
        return

    def removeFromHead(self) -> Optional[object]:
        if not self.head:
            self.length = 0
            return None
        else:
            self.length -= 1
            temp = self.head
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return temp.value

    def removeFromTail(self) -> Optional[object]:
        if not self.tail:
            self.length = 0
            return None
        else:
            self.length -= 1
            temp = self.tail
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            return temp.value

    def insertAtIndex(self, index: int, value: object) -> None:
        newNode = Node(value)
        if not self.head or not self.tail:
            self.head = newNode
            self.tail = newNode
            print("Empty Linked List, Inserting at Head")
            return
        if index == 0:
            self.insertAtHead(value=value)
            return
        if index >= self.length:
            self.insertAtTail(value=value)
            return

        temp: Optional[Node] = None
        i: int = 0
        if index <= self.length // 2:
            # Insert from head
            i: int = 0
            temp = self.head
            while i < index and temp:
                temp = temp.next
                i += 1
        else:
            # Insert from tail
            i: int = self.length - 1
            temp = self.tail
            while i > index and temp:
                temp = temp.prev
                i -= 1

        if temp:
            newNode.prev = temp.prev
            newNode.next = temp
            if temp.prev:
                temp.prev.next = newNode
            temp.prev = newNode
        self.length += 1
        del temp, i
        return

    def removeFromIndex(self, index: int) -> object:
        if not self.head or not self.tail:
            print("Linked List Empty")
            return None
        if index == 0:
            self.removeFromHead()
            return
        if index >= self.length - 1:
            self.removeFromTail()
            return
        temp: Optional[Node] = None
        i: int = 0
        if index <= self.length // 2:
            # delete from head
            i = 0
            temp = self.head
            while i < index and temp:
                temp = temp.next
                i += 1
        else:
            # delete from tail
            i = self.length - 1
            temp = self.tail
            while i >= index and temp:
                temp = temp.prev
                i -= 1
        if temp:
            newTemp = temp
            if temp.prev:
                temp.prev.next = newTemp.next
            if temp.next:
                temp.next.prev = newTemp.prev
        self.length -= 1
        deletedItem = None
        if temp:
            deletedItem = temp.value
        del temp, i
        return deletedItem

    def changeElementAtIndex(self, index: int, newValue: object):
        if not self.head or not self.tail:
            newNode = Node(value=newValue)
            self.head = newNode
            self.tail = newNode
            print("Empty Linked List, Inserting at Head")
            return
        if index == 0:
            self.head.value = newValue
            return
        if index >= self.length:
            self.tail.value = newValue
            return
        i: int = 0
        if index <= self.length // 2:
            # traverse from head
            i = 0
            temp = self.head
            while i < index and temp:
                temp = temp.next
                i += 1
        else:
            # traverse from tail
            i = self.length - 1
            temp = self.tail
            while i > index and temp:
                temp = temp.prev
                i -= 1
        if temp:
            temp.value = newValue
        return


doublyLinkedList: DoublyLinkedList = DoublyLinkedList(
    [1, 2, 3, 4, 5, 6, 7, 8, 9])
print("Linked List from Head: ", doublyLinkedList.asArray())
print("Linked List from Tail: ", doublyLinkedList.asRevertedArray())
print("Length of Linked List: ", doublyLinkedList.getLength())
doublyLinkedList.insertAtHead(0)
doublyLinkedList.insertAtTail(0)
doublyLinkedList.insertAtHead(99)
doublyLinkedList.insertAtTail(99)
print("Length of Linked List: ", doublyLinkedList.getLength())
print("Linked List from Head: ", doublyLinkedList.asArray())
print("Linked List from Tail: ", doublyLinkedList.asRevertedArray())
print("Deleted Item from Head: ", doublyLinkedList.removeFromHead())
print("Deleted Item from Tail: ", doublyLinkedList.removeFromTail())
print("Length of Linked List: ", doublyLinkedList.getLength())
print("Linked List from Head: ", doublyLinkedList.asArray())
print("Linked List from Tail: ", doublyLinkedList.asRevertedArray())
doublyLinkedList.insertAtIndex(4, 99)
doublyLinkedList.insertAtIndex(7, 99)
print("Linked List from Head: ", doublyLinkedList.asArray())
print("Linked List from Tail: ", doublyLinkedList.asRevertedArray())
print("Deleted Linked List Item: ", doublyLinkedList.removeFromIndex(4))
print("Deleted Linked List Item: ", doublyLinkedList.removeFromIndex(7))
print("Linked List from Head: ", doublyLinkedList.asArray())
print("Linked List from Tail: ", doublyLinkedList.asRevertedArray())
doublyLinkedList.changeElementAtIndex(4, 16)
doublyLinkedList.changeElementAtIndex(7, 61)
print("Linked List from Head: ", doublyLinkedList.asArray())
print("Linked List from Tail: ", doublyLinkedList.asRevertedArray())
