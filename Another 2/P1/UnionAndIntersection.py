"""
Union and Intersection of Two Linked Lists
Your task for this problem is to fill out the union and intersection functions. The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both the sets A and B.

You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively. Once you have completed the problem you will create your own test cases and perform your own run time analysis on the code.

For the union and intersection problem, the approach has been to transform the linked lists, a format which is harder to work with, on something much simpler as is a list. Once the transformation has been done, the combination with the handy object sets, has done all the work.

Time and Space complexity
In the study of the time complexity, we find that the transformation from linked list to list, takes O(n) time complexity, the the set function is in the same or less order of magnitude, as for the variations:

Union: we find the creation of the final array, again O(n), making n*O(n) be resulting to O(n)
Intersection: we find the creation of the final array, which is a double for-loop (operation x in s, acts with O(n)), resulting finally in O(n^n)
In respect to the space time complexity, we generate for both functions, 3 auxiliary lists, being O(3n); and resulting in O(n).
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        """
            Append a value to the end of the list
        """
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        """
            Return the size or length of the linked list
        """
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size

    def to_list(self):
        """
            Transform the linked list content into the list
        """
        out = []
        node = self.head
        while node:
            out.append(node.value)
            node = node.next
        return out

def union(linkedlist_1: LinkedList, linkedlist_2: LinkedList) -> list:
    """
    For two given linked list, returns all the values present in whichever, one time each value
    :param linkedlist_1: first linked list
    :param linkedlist_2: second linked list
    :return: set of all values
    """
    list_1 = linkedlist_1.to_list()
    list_2 = linkedlist_2.to_list()

    list_all = list(set(list_1 + list_2))
    linked_list = LinkedList()
    for i in list_all:
        linked_list.append(i)

    return linked_list

def intersection(linkedlist_1 : LinkedList, linkedlist_2 : LinkedList) -> list:
    """
    For two given linked list, returns all the values present in both lists, one time each value
    :param linkedlist_1: first linked list
    :param linkedlist_2: second linked list
    :return: set of all coincident values
    """
    set_1 = set(linkedlist_1.to_list())
    set_2 = set(linkedlist_2.to_list())

    common_set = []
    for element in set_1:
        if element in set_2:
            common_set.append(element)

    linked_list = LinkedList()

    for i in common_set:
        linked_list.append(i)
    return linked_list


# Normal Cases:
# Test case 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1, linked_list_2))
# 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 ->
print(intersection(linked_list_1, linked_list_2))
# 4 -> 6 -> 21 ->

# Test case 2
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
# 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 ->
print(intersection(linked_list_3, linked_list_4))
#

# Test case 3
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [22, 7, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 65, 11, 21, 1]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print(union(linked_list_5, linked_list_6))
# 65 -> 1 -> 35 -> 4 -> 3 -> 6 -> 7 -> 8 -> 11 -> 21 -> 22 -> 23 ->
print(intersection(linked_list_5, linked_list_6))
# 65 -> 7 ->


# Edge Cases:
# Test case 4
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = []
element_2 = [1, 7, 8]

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print(union(linked_list_7, linked_list_8))
# 8 -> 1 -> 7 ->
print(intersection(linked_list_7, linked_list_8))
#

# Test case 5
linked_list_9 = LinkedList()
linked_list_10 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_9.append(i)

for i in element_2:
    linked_list_10.append(i)

print(union(linked_list_9, linked_list_10))
#
print(intersection(linked_list_9, linked_list_10))
#
