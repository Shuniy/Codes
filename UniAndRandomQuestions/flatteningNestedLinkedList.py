class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, head):
        self.head = head

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(value)

    def flatten_deep(self):
        value_list = []
        node = self.head

        while node.next is not None:
            value_list.append(node.value)
            node = node.next
        value_list.append(node.value)
        return value_list

# Create a nested Linked List
class NestedLinkedList(LinkedList):
    def flatten(self):
        values = []
        for element in self.flatten_deep():
            values.append(element.flatten_deep())
        values = [item for sublist in values for item in sublist]
        values.sort()
        return values

linked_list = LinkedList(Node(1))
linked_list.append(3)
linked_list.append(5)

second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)

nested_linked_list = NestedLinkedList(Node(linked_list))
nested_linked_list.append(second_linked_list)
solution = nested_linked_list.flatten()
assert solution == [1, 2, 3, 4, 5]

def merge(list1, list2):
    merged = LinkedList(None)
    if list1 is None:
        return list2
    if list2 is None:
        return list1
    list1_elt = list1.head
    list2_elt = list2.head
    while list1_elt is not None or list2_elt is not None:
        if list1_elt is None:
            merged.append(list2_elt)
            list2_elt = list2_elt.next
        elif list2_elt is None:
            merged.append(list1_elt)
            list1_elt = list1_elt.next
        elif list1_elt.value <= list2_elt.value:
            merged.append(list1_elt)
            list1_elt = list1_elt.next
        else:
            merged.append(list2_elt)
            list2_elt = list2_elt.next
    return merged


linked_list = LinkedList(Node(1))
linked_list.append(3)
linked_list.append(5)

second_linked_list = LinkedList(Node(2))
second_linked_list.append(4)

merged = merge(linked_list, second_linked_list)
node = merged.head
while node is not None:
    #This will print 1 2 3 4 5
    print(node.value)
    node = node.next

# Lets make sure it works with a None list
merged = merge(None, linked_list)
node = merged.head
while node is not None:
    #This will print 1 2 3 4 5
    print(node.value)
    node = node.next

"""
Flattening Recursively

class NestedLinkedList(LinkedList):
    def flatten(self):
        return self._flatten(self.head)

    def _flatten(self, node):
        if node.next is None:
            return merge(node.value, None)
        return merge(node.value, self._flatten(node.next))

nested_linked_list = NestedLinkedList(Node(linked_list))
nested_linked_list.append(second_linked_list)
flattened = nested_linked_list.flatten()

node = flattened.head
while node is not None:
    #This will print 1 2 3 4 5
    print(node.value)
    node = node.next

Computational Complexity
Lets start with the computational complexity of merge. Merge takes in two lists. Let's say the lengths of the lists are $N_{1}$ and $N_{2}$. Because we assume the inputs are sorted, merge is very efficient. It looks at the first element of each list and adds the smaller one to the returned list. Every time through the loop we are appending one element to the list, so it will take $N_{1} + N_{2}$ iterations until we have the whole list.

The complexity of flatten is a little more complicated to calculate. Suppose our NestedLinkedList has $N$ linked lists and each list's length is represented by $M_{1}, M_{2}, ..., M_{N}$.

We can represent this recursion as:

$merge(M_{1}, merge(M_{2}, merge(..., merge(M_{N-1}, merge(M_{N}, None)))))$

Let's start from the inside. The inner most merge returns the $nth$ linked list. The next merge does $M_{N-1} + M_{N}$ comparisons. The next merge does $M_{N-2} + M_{N-1} + M_{N}$ comparisons.

Eventually we will do $N$ comparisons on all of the $M_{N}$ elements. We will do $N-1$ comparisons on $M_{N-1}$ elements.

This can be generalized as:

$$
\sum_n^N n*M_{n}
$$
"""
