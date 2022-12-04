"""
The principle employed in this algorithms is based directly in the binary search algorithms, differently, to this implementations, in its structure, it has been decided to be employed a more divide approach, rather than computationally expensive on previous levels to spare some division; e.g. when the lists are of size 2, both values could have been checked (though this would have increased our time complexity).

Time and Space complexity
The time complexity being an algorithm based on binary search is O(log(n)). The number of iterations we perform, i.e. recursive depth, follows the rule of recursive_depth^2 = n. Thus if we isolate the number of iterations in relation to the input space (n), we obtain log(n) = recursive_depth. As for the space complexity, it is independent of the input, requiring solely pointers to different array locations; O(1).
"""

def binary_search_recursive(array : list, target : int, start_index : int, end_index : int) -> int:
    if start_index > end_index:
        return -1

    mid_index = (start_index + end_index) // 2
    mid_element = array[mid_index]

    if mid_element == target:
        return mid_index

    index_left_side = binary_search_recursive(array, target, start_index, mid_index - 1)
    index_right_side = binary_search_recursive(array, target, mid_index + 1, end_index)

    return max(index_left_side, index_right_side)

def rotated_array_search(input_list : list, number : int) -> int:
    return binary_search_recursive(array=input_list, target=number, start_index=0, end_index=len(input_list) - 1)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index

    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

# Normal cases
print('Normal Cases:')
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
print('\n')

# Edge cases
print('Edge Cases:')
test_function([[], -1])
test_function([[1], 0])
