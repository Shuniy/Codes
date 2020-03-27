"""
Case Specific Sorting of Strings¶
Problem statement
Given a string consisting of uppercase and lowercase ASCII characters, write a function, case_sort, that sorts uppercase and lowercase letters separately, such that if the $i$th place in the original string had an uppercase character then it should not have a lowercase character after being sorted and vice versa.

For example:
Input: fedRTSersUXJ
Output: deeJRSfrsTUX
"""
def mergesort(items):
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged

def case_sort(string):
    lower_case_char = []
    upper_case_char = []

    for char in string:
        if ord(char) < 91:
            upper_case_char.append(char)
        else:
            lower_case_char.append(char)
    lower_case_char = mergesort(lower_case_char)
    upper_case_char = mergesort(upper_case_char)

    result = ''

    for char in string:
        if ord(char) < 91:
            result += upper_case_char.pop(0)
        else:
            result += lower_case_char.pop(0)

    return result

def test_function(test_case):
    test_string = test_case[0]
    solution = test_case[1]

    if case_sort(test_string) == solution:
        print("Pass")
    else:
        print("False")


test_string = 'fedRTSersUXJ'
solution = "deeJRSfrsTUX"
test_case = [test_string, solution]
test_function(test_case)

test_string = "defRTSersUXI"
solution = "deeIRSfrsTUX"
test_case = [test_string, solution]
test_function(test_case)
