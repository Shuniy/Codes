"""
Problem statement
Given a sorted array that may have duplicate values, use binary search to find the first and last indexes of a given value.

For example, if you have the array [0, 1, 2, 2, 3, 3, 3, 4, 5, 6] and the given value is 3, the answer will be [4, 6] (because the value 3 occurs first at index 4 and last at index 6 in the array).

The expected complexity of the problem is $O(log(n))$.
"""

def recursive_binary_search(target, source, left = 0):
    if len(source) == 0:
        return None
    center = (len(source) - 1) // 2
    if source[center] == target:
        return center + left
    elif source[center] < target:
        return recursive_binary_search(target, source[center + 1:], left + center + 1)
    else:
        return recursive_binary_search(target, source[:center], left)

def first_and_last_index(source, target):
    """
    Given a sorted array that may have duplicate values, use binary
    search to find the first and last indexes of a given value.

    Args:
        arr(list): Sorted array (or Python list) that may have duplicate values
        number(int): Value to search for in the array
    Returns:
        a list containing the first and last indexes of the given value
    """
    initial_index = recursive_binary_search(target, source)
    if initial_index is None:
        return [-1, 1]

    lower_index = initial_index
    while source[lower_index] == target:
        if lower_index == 0:
            lower_index = 0
            break
        if source[lower_index - 1] == target:
            lower_index -= 1
        else:
            break
    upper_index = initial_index
    while source[upper_index] == target:
        if upper_index == len(source) - 1:
            upper_index = len(source) - 1
            break
        if source[upper_index + 1] == target:
            upper_index += 1
        else:
            break
    return[lower_index, upper_index]

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    solution = test_case[2]
    output = first_and_last_index(input_list, number)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


input_list = [1]
number = 1
solution = [0, 0]
test_case_1 = [input_list, number, solution]
test_function(test_case_1)

input_list = [0, 1, 2, 3, 3, 3, 3, 4, 5, 6]
number = 3
solution = [3, 6]
test_case_2 = [input_list, number, solution]
test_function(test_case_2)

input_list = [0, 1, 2, 3, 4, 5]
number = 5
solution = [5, 5]
test_case_3 = [input_list, number, solution]
test_function(test_case_3)

input_list = [0, 1, 2, 3, 4, 5]
number = 6
solution = [-1, -1]
test_case_4 = [input_list, number, solution]
test_function(test_case_4)


