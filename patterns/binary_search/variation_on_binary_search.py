"""
Find First
The binary search function is guaranteed to return an index for the element you're looking for in an array, but what if the element appears more than once?

Consider this array:

[1, 3, 5, 7, 7, 7, 8, 11, 12]

Let's find the number 7:
multiple = [1, 3, 5, 7, 7, 7, 8, 11, 12]
recursive_binary_search(7, multiple)
Ans: 4

Hmm...
Looks like we got the index 4, which is correct, but what if we wanted to find the first occurrence of an element, rather than just any occurrence?

Write a new function: find_first() that uses binary_search as a starting point.

Hint: You shouldn't need to modify binary_search() at all.
"""
def recursive_binary_search(target, source, left = 0):
    if len(source) == 0:
        return None
    center = (len(source)-1) // 2
    if source[center] == target:
        return center + left
    elif source[center] < target:
        return recursive_binary_search(target, source[center+1:], left+center+1)
    else:
        return recursive_binary_search(target, source[:center], left)

def find_first(target, source):
    index = recursive_binary_search(target, source)
    if not index:
        return None

    while source[index] == target:
        if index == 0:
            return 0
        if source[index - 1] == target:
            index -= 1
        else:
            return index

multiple = [1, 3, 5, 7, 7, 7, 8, 11, 12, 13, 14, 15]
print(find_first(7, multiple))  # Should return 3
print(find_first(9, multiple))  # Should return None

"""
Contains
The second variation is a function that returns a boolean value indicating whether an element is present, but with no information about the location of that element.

For example:

letters = ['a', 'c', 'd', 'f', 'g']
print(contains('a', letters)) ## True
print(contains('b', letters)) ## False
"""

def contains(target, source):
    return recursive_binary_search(target, source) is not None


letters = ['a', 'c', 'd', 'f', 'g']
print(contains('a', letters))  # True
print(contains('b', letters))  # False
