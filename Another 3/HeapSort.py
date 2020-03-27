"""
Heapsort
A heapsort is an in-place sorting algorithm that treats an array like a binary tree and moves the largest values to the end of the heap until the full array is sorted.

The main steps in a heapsort are:

Convert the array into a maxheap (a complete binary tree with decreasing values)
Swap the top element with the last element in the array (putting it in it's correct final position)
Repeat with arr[:len(arr)-1] (all but the sorted elements)
"""
def heapsort(arr):
    arr_sorted = []

    for i in range(len(arr)):
        arr = heapify(arr, i)

    swap_position = len(arr) - 1

    for i in range(len(arr) - 1):
        bigger_value = arr[0]
        arr[0] = arr[swap_position]
        arr[swap_position] = bigger_value

        for i in range(swap_position):
            arr = heapify(arr, i)
        swap_position -= 1

    return arr

def heapify(arr, index):
    if index == 0:
        return arr

    index_parent = (index - 1) // 2
    value_parent = arr[index_parent]
    value_children = arr[index]

    if value_children > value_parent:
        arr[index_parent] = value_children
        arr[index] = value_parent
        arr = heapify(arr, index_parent)

    else:
        pass

    return arr

def test_function(test_case):
    heapsort(test_case[0])
    if test_case[0] == test_case[1]:
        print("Pass")
    else:
        print("False")


arr = [3, 7, 4, 6, 1, 0, 9, 8, 9, 4, 3, 5]
solution = [0, 1, 3, 3, 4, 4, 5, 6, 7, 8, 9, 9]

test_case = [arr, solution]

test_function(test_case)

arr = [5, 5, 5, 3, 3, 3, 4, 4, 4, 4]
solution = [3, 3, 3, 4, 4, 4, 4, 5, 5, 5]
test_case = [arr, solution]
test_function(test_case)

arr = [99]
solution = [99]
test_case = [arr, solution]
test_function(test_case)

arr = [0, 1, 2, 5, 12, 21, 0]
solution = [0, 0, 1, 2, 5, 12, 21]
test_case = [arr, solution]
test_function(test_case)
