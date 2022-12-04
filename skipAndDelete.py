"""
You are given the head of a linked list and two integers, i and j. You have to retain the first i nodes and then delete the next j nodes. Continue doing so until the end of the linked list.

Example:

linked-list = 1 2 3 4 5 6 7 8 9 10 11 12
i = 2
j = 3
Output = 1 2 6 7 11 12
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def skip_i_delete_j(head ,i ,j):
    inputNode = head
    trimLinkedList = None

    positionCounter = 1
    i_node = True
    lastNode = False
    while not lastNode:
        if i_node:
            if trimLinkedList is None:
                trimLinkedList = Node(inputNode.data)
            else:
                tail = trimLinkedList
                while tail.next:
                    tail = tail.next
                tail.next = Node(inputNode.data)

            if positionCounter == i:
                i_node = False
                positionCounter = 0
        else:
            if positionCounter == j:
                i_node = True
                positionCounter = 0
        positionCounter += 1
        lastNode = inputNode.next is None
        inputNode = inputNode.next
    return trimLinkedList


def create_linked_list(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    tail = head
    for data in arr[1:]:
        tail.next = Node(data)
        tail = tail.next
    return head


def print_linked_list(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()


def test_function(test_case):
    head = test_case[0]
    i = test_case[1]
    j = test_case[2]
    solution = test_case[3]

    temp = skip_i_delete_j(head, i, j)
    index = 0
    try:
        while temp is not None:
            if temp.data != solution[index]:
                print("Fail")
                return
            index += 1
            temp = temp.next
        print("Pass")
    except Exception as e:
        print("Fail")


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
i = 2
j = 2
head = create_linked_list(arr)
solution = [1, 2, 5, 6, 9, 10]
test_case = [head, i, j, solution]
test_function(test_case)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
i = 2
j = 3
head = create_linked_list(arr)
solution = [1, 2, 6, 7, 11, 12]
test_case = [head, i, j, solution]
test_function(test_case)

arr = [1, 2, 3, 4, 5]
i = 2
j = 4
head = create_linked_list(arr)
solution = [1, 2]
test_case = [head, i, j, solution]
test_function(test_case)
