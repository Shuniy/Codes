"""
Given a linked list with integer data, arrange the elements in such a manner that all nodes with even numbers are placed after odd numbers. Do not create any new nodes and avoid using any other data structure. The relative order of even and odd elements must not change.

Example:

linked list = 1 2 3 4 5 6
output = 1 3 5 2 4 6
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def even_after_odd(head):
    linked_list_end = False
    even_linked_list = None
    odd_linked_list = None
    node= head

    while not linked_list_end:
        if node.data % 2 == 0:
            if even_linked_list is None:
                even_linked_list = Node(node.data)
            else:
                position_tail = even_linked_list
                while position_tail.next:
                    position_tail = position_tail.next
                position_tail.next = Node(node.data)
        else:
            if odd_linked_list is None:
                odd_linked_list = Node(node.data)
            else:
                position_tail = odd_linked_list
                while position_tail.next:
                    position_tail = position_tail.next
                position_tail.next = Node(node.data)

        linked_list_end = node.next is None
        node = node.next

    position_tail = odd_linked_list

    while position_tail.next:
        position_tail = position_tail.next
    position_tail.next = even_linked_list

    return odd_linked_list

def create_linked_list(arr):
    if len(arr) ==0:
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
    solution = test_case[1]

    node_tracker = dict({})
    node_tracker['nodes'] = list()
    temp = head
    while temp:
        node_tracker['nodes'].append(temp)
        temp = temp.next

    head = even_after_odd(head)
    temp = head
    index = 0
    try:
        while temp:
            if temp.data != solution[index] or temp not in node_tracker['nodes']:
                print("Fail")
                return
            temp = temp.next
            index += 1
        print("Pass")
    except Exception as e:
        print("Fail")


arr = [1, 2, 3, 4, 5, 6]
solution = [1, 3, 5, 2, 4, 6]

head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)

arr = [1, 3, 5, 7]
solution = [1, 3, 5, 7]

head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)

arr = [2, 4, 6, 8]
solution = [2, 4, 6, 8]
head = create_linked_list(arr)
test_case = [head, solution]
test_function(test_case)
