"""
This problem is tackler as the construction of a output list, issue form a single transverse of the elements. By using, several pointers, it is possible on a single transverse to properly order the provided array.

Time and Space complexity
In this case the time complexity is precisely, O(n). Analyzing the space complexity, due to the non usage of auxiliary tables (only a few pointers), it is of order O(1) (excluding the input space).

Dutch National Flag Problem
Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.
"""
def sort_012(input_list):
    i = 0
    i_null = 0
    i_two = len(input_list) - 1

    while i <= i_two:
        if input_list[i] == 0:
            input_list[i] = input_list[i_null]
            input_list[i_null] = 0
            i_null += 1
            i += 1

        elif input_list[i] == 2:
            temp_val = input_list[i_two]
            input_list[i_two] = 2
            input_list[i] = temp_val
            i_two -= 1
        else:
            i += 1
    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

print('Normal Cases:')
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2,
               2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
print('\n')

# Edge cases
print('Edge Cases:')
test_function([0, 1, 1, 0, 1])
test_function([0, 0, 0])
test_function([])
