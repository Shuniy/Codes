"""
Single Linked List
"""
# Node Structure
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def length(self):
        if self.head is None:
            return 0
        else:
            temp = self.head
            length = 0
            while temp:
                length += 1
                temp = temp.next

        return length

    def makeHead(self, value):
        self.head = Node(value)
        print(f'Node with value : {value} inserted at Head and is also a Head')

    def insert(self, value):
        self.insertAtHead(value)

    def insertAtHead(self, value):
        if self.head is None:
            self.makeHead(value)
        else:
            new_head = Node(value)
            new_head.next = self.head
            self.head = new_head
            print(f'Node with value : {value} insert at Head')

    def insertAtEnd(self, value):
        if self.head is None:
            self.makeHead(value)
        else:
            temp_node = self.head
            while temp_node.next:
                temp_node = temp_node.next

            temp_node.next = Node(value)
            print(f'Node with value : {value} inserted at end')

    def insertAtPosition(self, value, pos):
        curr_size = self.length()
        if self.head is None:
            self.insertAtHead(value)
        elif pos == 1:
            self.insertAtHead(value)
        elif pos > curr_size:
            self.insertAtEnd(value)
        else:
            temp = self.head
            temp_pos = pos - 2
            while temp_pos:
                temp_pos -= 1
                temp = temp.next

            nxt = temp.next
            temp.next = Node(value)
            temp.next.next = nxt
            print(f'Node with value {value} inserted at position {pos}')

    def print(self):
        temp = self.head
        print('Linked List : ', end = '')
        while temp:
            print(temp.value, end=' -> ')
            temp = temp.next
        print(None)

    def getHead(self):
        if self.head is None:
            return None
        return self.head.value

    def getLast(self):
        temp = self.head
        while temp.next:
            temp = temp.next

        return temp.value

    def getValueAtPosition(self, pos):
        length = self.length()
        if pos == 1:
            return self.getHead()
        elif pos > length:
            return self.getLast()
        else:
            temp_pos = pos - 1
            temp = self.head
            while temp_pos:
                temp_pos -= 1
                temp = temp.next

            return temp.value

    def setHead(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            self.head.value = value
            print(f'Value of Head changed to {value} ')

    def setLast(self, value):
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.value = value

        print('Value of Last Element Changed to {value}')

    def setValueAtPosition(self, value, pos):
        length = self.length()
        if pos == 1:
            return self.setHead(value)
        elif pos > length:
            return self.setLast(value)
        else:
            temp_pos = pos - 1
            temp = self.head
            while temp_pos:
                temp_pos -= 1
                temp = temp.next

            temp.value = value
            print(f'Value at position {pos} changed to {value}')

    def isEmpty(self):
        if self.head is None:
            print('Linked List is Empty')
            return True
        else:
            return False

    def delete(self):
        if self.isEmpty():
            return None
        else:
            self.deleteAtHead()

    def deleteAtHead(self):
        if self.isEmpty():
            return
        else:
            self.head = self.head.next

    def deleteAtEnd(self):
        if self.isEmpty():
            return
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp = temp

# Basic Operations : Insertion and Deletion
linkedList = LinkedList()

# Insertion
linkedList.insertAtHead(5)
linkedList.insertAtHead(6)
linkedList.insertAtEnd(8)
linkedList.insertAtEnd(9)
linkedList.insertAtPosition(1, 3)
linkedList.insertAtPosition(2, 2)
linkedList.insertAtPosition(4, 6)
linkedList.insertAtPosition(3, 7)
linkedList.insertAtPosition(0, 9)
linkedList.insertAtPosition(7, 1)

# Deletion
linkedList.delete()


# Length of Linked List
print('Length of Linked List : ', linkedList.length())
# Printing Linked List
linkedList.print()

# Getters
print('Value at End', linkedList.getLast())
print('Value at Head : ', linkedList.getHead())
print('Value at Position 1 : ', linkedList.getValueAtPosition(1))
print('Value at Position 11 : ', linkedList.getValueAtPosition(11))
print('Value at Position 10 : ', linkedList.getValueAtPosition(10))
print('Value at Position 5 : ', linkedList.getValueAtPosition(5))
print('Value at Position 9 : ', linkedList.getValueAtPosition(9))

# Setters
linkedList.setLast(7)
linkedList.setHead(0)
linkedList.setValueAtPosition(11, 1)
linkedList.setValueAtPosition(13, 11)
linkedList.setValueAtPosition(21, 10)
linkedList.setValueAtPosition(41, 5)
linkedList.setValueAtPosition(69, 9)

linkedList.print()
