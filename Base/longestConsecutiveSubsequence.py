"""
Problem Statement
Given list of integers that contain numbers in random order, write a program to find the longest possible sub sequence of consecutive numbers in the array. Return this subsequence in sorted order. The solution must take O(n) time

For e.g. given the list 5, 4, 7, 10, 1, 3, 55, 2, the output should be 1, 2, 3, 4, 5

Note- If two arrays are of equal length return the array whose index of smallest element comes first.
"""


def longest_consecutive_subsequence(input_list):
    input_list.sort()
    input_list = [element for element in set(input_list)]
    input_list_subst = []

    for i, value in enumerate(input_list):
        if (i != (len(input_list)-1)):
            if i >= 1:
                if (input_list_subst[i-1] == -1) & (input_list[i] - input_list[i + 1] != -1):
                    input_list_subst.append(-1)

            input_list_subst.append(input_list[i] - input_list[i + 1])

        else:
            pass

    i_stored = 0
    i_stored_max = 0
    i_stored_length = 0
    i_stored_max_length = 0
    unbroken_consecutive = True

    for i, value in enumerate(input_list_subst):
        if value == -1:
            i_stored_length += 1

            if i_stored != 0:
                pass
            else:
                i_stored = i
        else:
            unbroken_consecutive = False

            if i_stored is not 0:
                if i_stored_length > i_stored_max_length:
                    i_stored_max_length = i_stored_length
                    i_stored_max = i_stored

                i_stored = 0
                i_stored_length = 0

    if unbroken_consecutive:
        return input_list
    else:
        return input_list[i_stored_max-1: i_stored_max + i_stored_max_length-1]


def test_function(test_case):
    output = longest_consecutive_subsequence(test_case[0])
    if output == test_case[1]:
        print("Pass")
    else:
        print("Fail")


test_case_1 = [[5, 4, 7, 10, 1, 3, 55, 2], [1, 2, 3, 4, 5]]
test_function(test_case_1)

test_case_2 = [[2, 12, 9, 16, 10, 5, 3, 20,
                25, 11, 1, 8, 6], [8, 9, 10, 11, 12]]
test_function(test_case_2)

test_case_3 = [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
test_function(test_case_3)
