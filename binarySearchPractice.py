"""

Binary search practice
Let's get some practice doing binary search on an array of integers. We'll solve the problem two different ways—both iteratively and resursively.

Here is a reminder of how the algorithm works:

Find the center of the list (try setting an upper and lower bound to find the center)
Check to see if the element at the center is your target.
If it is, return the index.
If not, is the target greater or less than that element?
If greater, move the lower bound to just above the current center
If less, move the upper bound to just below the current center
Repeat steps 1-6 until you find the target or until the bounds are the same or cross (the upper bound is less than the lower bound).
Problem statement:
Given a sorted array of integers, and a target value, find the index of the target value in the array. If the target value is not present in the array, return -1.
"""
import math

def binary_search(array, target):
    """
    Write a function that implements the binary search algorithm using iteration
    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    """
    while True:
        center_list = round(len(array) / 2)
        if target == array[center_list]:
            return center_list

        elif target < array[center_list]:
            array = array[:center_list]
        else:
            array = array[center_list:]

        if len(array == 1):
            return -1


def test_function(test_case):
    answer = binary_search(test_case[0], test_case[1])
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")


array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 6
index = 6
test_case = [array, target, index]
test_function(test_case)


def binary_search_recursive(array, target, index):
    '''Write a function that implements the binary search algorithm using recursion

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''

    if len(array) == 1:
        if array[0] == target:
            return index
        else:
            return -1

    center_list = math.floor((len(array) - 1) / 2)
    if center_list * 2 < len(array):
        index = index - center_list - 1
    else:
        index = index - center_list

    if target == array[center_list]:
        return index
    elif target < array[center_list]:
        index_target = binary_search_recursive(array[:center_list], target, index)
    else:
        index_target = binary_search_recursive(array[center_list:], target, index)

    return index_target


def test_function(test_case):
    answer = binary_search_recursive(test_case[0], test_case[1])
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")


array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 4
index = 5
test_case = [array, target, index]
test_function(test_case)
