"""
Doubly Linked List
"""
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def check(self, pos):
        if pos < 0 or pos > self.length:
            print('Failed, Check Position !')
            return True
        return False

    def isEmpty(self):
        return self.length == 0

    def getLength(self):
        """Return length of the linked list"""
        return self.length

    def getValueAtPosition(self, pos):
        """Returns value at position, with index starting at 1"""
        if self.check(pos):
            return

        if pos == 1:
            return self.getHead()

        if pos == self.length:
            return self.getTail()

        if pos > self.length // 2:
            temp = self.tail
            print(self.tail)
            curr = pos
            while self.length -  curr - 1:
                print(temp.value)
                curr -= 1
                temp = temp.prev

            return temp.value
        else:
            temp = self.head
            curr = pos
            while curr - 1:
                curr -= 1
                temp = temp.next

            return temp.value

    def setValueAtPosition(self, pos, value):
        """Changes value at position, with index starting at 1"""
        if self.check(pos):
            return

        if pos == 1:
            self.setHead(value)
            return

        if pos == self.length:
            self.setTail(value)
            return

        if pos > self.length // 2:
            temp = self.tail
            curr = pos
            while self.length - curr:
                curr -= 1
                print(temp.value)
                temp = temp.prev

            temp.value = value
        else:
            temp = self.head
            curr = pos
            while curr:
                curr -= 1
                temp = temp.next

            temp.value = value

    def getHead(self):
        return self.head.value

    def getTail(self):
        """return tail"""
        return self.tail.value

    def setHead(self, value):
        """
        Changes the value of head but doesn't add a new Node
        """
        if self.head is None:
            print('No head is found, linked list is empty')
            return
        else:
            self.head.value = value

    def setTail(self, value):
        """
        Changes the value of tail but doesn't add a new Node
        """
        if self.head is None:
            print('No tail is found, linked list is empty')
            return
        else:
            self.tail.value = value

    def makeHead(self, value):
        """Make Head"""
        self.head = Node(value)

    def insert(self, value):
        self.length += 1
        if self.head is None:
            self.makeHead(value)
            self.tail = self.head
            return
        else:
            newNode = Node(value)
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            return

    def delete(self):
        if self.head is None:
            print('Nothing to Delete')
            return
        else:
            self.length -= 1
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            del temp
            return 

    def insertAtHead(self, value):
        self.insert(value)
        return

    def insertAtTail(self, value):
        if self.head is None:
            self.insert()

        newNode = Node(value)
        newNode.prev = self.tail
        self.tail.next = newNode
        self.tail = newNode
        return 

    def insertAtPosition(self, value, pos):
        if self.check(pos):
            return

        if pos > self.length // 2:
            curr = pos
            temp = self.tail

            while curr - 1:
                curr -= 1
                temp = temp.prev

            newNode = Node(value)

        else:
            pass 

        

    def insertBeforeNode(self, toInsert, beforeNode):
        pass

    def deleteAtHead(self):
        self.delete()
        return

    def deleteAtEnd(self):
        pass

    def deleteAtPosition(self, pos):
        if self.check(pos):
            return

    def deleteBeforeNode(self, beforeNode):
        pass

    def print(self):
        """Print the linked list from Head"""
        if self.head is None:
            return self.head.value
        else:
            temp = self.head
            while temp and temp.next:
                print(temp.value, end='->')
                temp = temp.next

            print(temp.value)

    def printBack(self):
        pass


# creating a linked list object
doublyLinkedList = DoublyLinkedList()

# insert and delete
doublyLinkedList.insert(5)
doublyLinkedList.insert(6)
doublyLinkedList.insert(7)
doublyLinkedList.insert(8)
doublyLinkedList.insertAtHead(9)
doublyLinkedList.insertAtTail(10)
print('Length of the linked list', doublyLinkedList.getLength())
print('Head of the linked list', doublyLinkedList.getHead())
print('Tail of the linked list', doublyLinkedList.getTail())
print('Value at position 3 of the linked list', doublyLinkedList.getValueAtPosition(3))
print('Value at position 2 of the linked list', doublyLinkedList.getValueAtPosition(2))
print('Value at position 1 of the linked list', doublyLinkedList.getValueAtPosition(1))
print('Value at position 4 of the linked list', doublyLinkedList.getValueAtPosition(4))
doublyLinkedList.print()

doublyLinkedList.delete()
doublyLinkedList.delete()
print('Value at position 1 of the linked list', doublyLinkedList.getValueAtPosition(1))
print('Value at position 2 of the linked list', doublyLinkedList.getValueAtPosition(2))
print('Length of the linked list', doublyLinkedList.getLength())
print('Head of the linked list', doublyLinkedList.getHead())
print('Tail of the linked list', doublyLinkedList.getTail())
doublyLinkedList.print()



print('Is linked list empty : ', doublyLinkedList.isEmpty())
