class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

# Singly Linked Lists
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next :
            node = node.next
        node.next = Node(value)
        return

    def toList(self):
        nodeValues = []
        node = self.head
        while node:
            nodeValues.append(node.value)
            node = node.next
        return nodeValues

linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(4)

node = linked_list.head
while node:
    print(node.value)
    node = node.next

print(linked_list.toList())

# Doubly Linked List
class DoubleNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        if self.head is None:
            self.head = DoubleNode(value)
            self.tail = self.head

        else:
            self.tail.next = DoubleNode(value)
            self.tail.next.previous = self.tail
            self.tail = self.tail.next
        return


linked_list = DoublyLinkedList()
linked_list.append(1)
linked_list.append(-2)
linked_list.append(4)

print("Going forward through the list, should print 1, -2, 4")
node = linked_list.head
while node:
    print(node.value)
    node = node.next

print("\nGoing backward through the list, should print 4, -2, 1")
node = linked_list.tail
while node:
    print(node.value)
    node = node.previous


# Circular Linked List
class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        if self.head is None:
            self.head = DoubleNode(value)
            self.tail = self.head

        else:
            self.tail.next = DoubleNode(value)
            self.tail.next.previous = self.tail
            self.tail.next.next = self.head
            self.tail = self.tail.next
        return
