"""
Problem statement
Given an array arr and a target element target, find the last index of occurence of target in arr using recursion. If target is not present in arr, return -1.

For example:

For arr = [1, 2, 5, 5, 4] and target = 5, output = 3

For arr = [1, 2, 5, 5, 4] and target = 7, output = -1
"""
def last_index(arr, target):
    if len(arr) == 1:
        if arr[0] == target:
            return 0
        else:
            return -1
    else:
        prev_lvl = last_index(arr = arr[1:], target = target)
        curr_lvl = arr[0]
        if prev_lvl == -1 and curr_lvl != target:
            return -1
        return prev_lvl + 1

def test_function(test_case):
    arr = test_case[0]
    target = test_case[1]
    solution = test_case[2]
    output = last_index(arr, target)
    if output == solution:
        print("Pass")
    else:
        print("False")


arr = [1, 2, 5, 5, 4]
target = 5
solution = 3

test_case = [arr, target, solution]
test_function(test_case)

arr = [1, 2, 5, 5, 4]
target = 7
solution = -1

test_case = [arr, target, solution]
test_function(test_case)

arr = [1, 1, 1, 1, 1, 1]
target = 1
solution = 5

test_case = [arr, target, solution]
test_function(test_case)
