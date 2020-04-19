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
        head = None
        tail = None
        for value in input_list:
            if head is None:
                head = node(value)
                tail = head
            else:
                tail.next = node(value)
                tail = tail.next
    except IndexError:
        head = None
    return head


def test_function(input_list, head):
    try:
        if len(input_list) == 0:
            if head is not None:
                print("Fail")
                return
        for value in input_list:
            if head.value != value:
                print("Fail")
                return
            else:
                head = head.next
        print("Pass")
    except Exception as e:
        print("Fail: " + e)


input_list = [1, 2, 3, 4, 5, 6]
head = createLinkedList2(input_list)
test_function(input_list, head)

input_list = [1]
head = createLinkedList2(input_list)
test_function(input_list, head)

input_list = []
head = createLinkedList2(input_list)
test_function(input_list, head)
