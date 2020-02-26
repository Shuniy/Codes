class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            previousHead = self.head
            self.head = Node(value)
            self.head.next = previousHead

    def append(self, value):
        tail = self.head
        if tail is None:
            self.head = Node(value)
        else:
            while tail.next:
                tail = tail.next
            tail.next = Node(value)

    def search(self, value):
        tail = self.head
        while tail.next:
            if tail.value == value:
                return tail
            tail = tail.next
        return

    def remove(self, value):
        previousTail = None
        tail = self.head
        while tail:
            if tail.value == value:
                if previousTail is None:
                    self.head = tail.next
                    break
                else:
                    previousTail.next = tail.next
                    break
            previousTail = tail
            tail.next = tail.next

    def pop(self):
        firstNode = self.head
        self.head = self.head.next
        return firstNode

    def insertAtPosition(self, value, pos):
        tailContinuity = None
        positionTail = self.head

        if pos == 0:
            tailContinuity = self.head
            self.head = Node(value)
            self.head.next = tailContinuity
            return
        else:
            for _ in range(1, pos - 1):
                if positionTail.next is None:
                    positionTail.next = Node(value)
                    return
                positionTail = positionTail.next
            tailContinuity = positionTail.next
            positionTail.next = Node(value)
            positionTail = positionTail.next
            positionTail.next = tailContinuity
            return

    def size(self):
        tail = self.head
        length = 0
        while tail is not None:
            tail = tail.next
            length += 1
        return length

    def toList(self):
        output = []
        node = self.head
        while node:
            output.append(node.value)
            node = node.next
        return output

## Test your implementation here


# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)
assert linked_list.toList() == [1], f"list contents: {linked_list.toList()}"
linked_list.append(3)
linked_list.prepend(2)
assert linked_list.toList() == [
    2, 1, 3], f"list contents: {linked_list.toList()}"

# Test append
linked_list = LinkedList()
linked_list.append(1)
assert linked_list.toList() == [1], f"list contents: {linked_list.toList()}"
linked_list.append(3)
assert linked_list.toList() == [
    1, 3], f"list contents: {linked_list.toList()}"

# Test search
linked_list.prepend(2)
linked_list.prepend(1)
linked_list.append(4)
linked_list.append(3)
assert linked_list.search(
    1).value == 1, f"list contents: {linked_list.toList()}"
assert linked_list.search(
    4).value == 4, f"list contents: {linked_list.toList()}"

# Test remove
linked_list.remove(1)
assert linked_list.toList() == [2, 1, 3, 4,
                                 3], f"list contents: {linked_list.toList()}"
linked_list.remove(3)
assert linked_list.toList() == [
    2, 1, 4, 3], f"list contents: {linked_list.toList()}"
linked_list.remove(3)
assert linked_list.toList() == [
    2, 1, 4], f"list contents: {linked_list.toList()}"

# Test pop
value = linked_list.pop()
assert value == 2, f"list contents: {linked_list.toList()}"
assert linked_list.head.value == 1, f"list contents: {linked_list.toList()}"

# Test insert
linked_list.insert(5, 0)
assert linked_list.toList() == [
    5, 1, 4], f"list contents: {linked_list.toList()}"
linked_list.insert(2, 1)
assert linked_list.toList() == [
    5, 2, 1, 4], f"list contents: {linked_list.toList()}"
linked_list.insert(3, 6)
assert linked_list.toList() == [5, 2, 1, 4,
                                 3], f"list contents: {linked_list.toList()}"

# Test size
assert linked_list.size() == 5, f"list contents: {linked_list.toList()}"
