"""
Counting Inversions
The number of inversions in a disordered list is the number of pairs of elements that are inverted (out of order) in the list.

Here are some examples:

[0,1] has 0 inversions
[2,1] has 1 inversion (2,1)
[3, 1, 2, 4] has 2 inversions (3, 2), (3, 1)
[7, 5, 3, 1] has 6 inversions (7, 5), (3, 1), (5, 1), (7, 1), (5, 3), (7, 3)
The number of inversions can also be thought of in the following manner.

Given an array arr[0 ... n-1] of n distinct positive integers, for indices i and j, if i < j and arr[i] > arr[j] then the pair (i, j) is called an inversion of arr.


Counting Inversions
The number of inversions in a disordered list is the number of pairs of elements that are inverted (out of order) in the list.

Here are some examples:

[0,1] has 0 inversions
[2,1] has 1 inversion (2,1)
[3, 1, 2, 4] has 2 inversions (3, 2), (3, 1)
[7, 5, 3, 1] has 6 inversions (7, 5), (3, 1), (5, 1), (7, 1), (5, 3), (7, 3)
The number of inversions can also be thought of in the following manner.

Given an array arr[0 ... n-1] of n distinct positive integers, for indices i and j, if i < j and arr[i] > arr[j] then the pair (i, j) is called an inversion of arr.

Problem statement
Write a function, count_inversions, that takes an array (or Python list) as input, and returns a count of the total number of inversions present in the input.

Mergesort provides an efficient way to solve this problem.
"""
def count_inversions(items):
    if len(items) <= 1:
        return items, 0

    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    inversions_left = 0
    inversions_right = 0

    left, inversions_left = count_inversions(left)
    right, inversions_right = count_inversions(right)

    merged, inversions = merge(left, right)

    return merged, inversions_left + inversions_right + inversions

def merge(left, right):
    merged = []
    inversions = 0
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            inversions += 1
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1
    merged += left[left_index:]
    merged += right[right_index:]

    return merged, inversions

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    if count_inversions(arr)[1] == solution:
        print("Pass")
    else:
        print("Fail")


arr = [2, 5, 1, 3, 4]
solution = 3
test_case = [arr, solution]
test_function(test_case)

arr = [54, 99, 49, 22, 37, 18, 22, 90, 86, 33]
solution = 13
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, 4, 2, 3, 11, 22, 99, 108, 389]
solution = 2
test_case = [arr, solution]
test_function(test_case)