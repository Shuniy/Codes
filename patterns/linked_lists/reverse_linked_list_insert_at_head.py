class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Helping class for linked list
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __repr__(self):
        return str([v for v in self])



# Inserting at head of the linked list
def insert_at_head(linked_list, value):
    position_tail_continuity = linked_list.head
    linked_list.head = Node(value)
    linked_list.head.next = position_tail_continuity

# To reverse a linked list
def reverse(linked_list):
    tail = linked_list.head
    reversed_linked_list = LinkedList()
    while tail is not None:
        value = tail.value
        reversed_linked_list = insert_at_head(reversed_linked_list, value)
        tail = tail.next

# Checking if it works or not
llist = LinkedList()
for value in [4, 2, 5, 1, -3, 0]:
    llist.append(value)

flipped = reverse(llist)
is_correct = list(flipped) == list(
    [0, -3, 1, 5, 2, 4]) and list(llist) == list(reverse(flipped))
print("Pass" if is_correct else "Fail")
