class node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

head = node(2)
head.next = node(1)
head.next.next = node(4)
head.next.next.next = node(3)
head.next.next.next = node(5)

def traverseList(head):
    currNode = head
    while currNode is not None:
        print(currNode.value)
        currNode = currNode.next
print(traverseList(head))

def createLinkedList1(inputList):
    try:
        head = node(inputList.pop(0))
        while len(inputList) > 0:
            currNode = head
            while currNode.next:
                currNode = currNode.next
            currNode.next = node(inputList.pop(0))
    except IndexError:
        head = None
    return head

# Efficient Solution is to take a tail node which saves traversing time

def createLinkedList2(inputList):
    try:
        head = node(inputList.pop(0))
        tail = head
        while len(inputList) > 0:
            tail.next = node(inputList.pop(0))
            tail = tail.next
    except IndexError:
        head = None
    return head

