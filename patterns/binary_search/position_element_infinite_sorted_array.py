def position_element_infinite_sorted_array(arr, target):
    """
    Find the position of a target element in an infinite sorted array.

    Parameters:
        arr (list): The infinite sorted array.
        target: The target element to search for.

    Returns:
        int: The position of the target element in the array, or -1 if it is not found.
    """
    left = 0
    # since infinite sorted array, we don't know, the right bound
    right = 1

    while left < right:
        # there is an extreme case, that right becomes larger than array length,
        # but it is an infinite sorted array so, this case will never happen
        while arr[right] < target:
            left = right
            right = right * 2
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid
        else:
            left = mid + 1

    return -1


# test cases for above function
arr = [1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 7, 7, 8, 9, 10]
target = 7
print(position_element_infinite_sorted_array(arr, target))
# test cases for above function
arr = [1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 7, 7, 8,
       9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
target = 19
print(position_element_infinite_sorted_array(arr, target))

# test cases for above function
arr = [1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 7, 7, 8,
       9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
target = 1
print(position_element_infinite_sorted_array(arr, target))
# test cases for above function
arr = [1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 7, 7, 8,
       9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
target = 18
print(position_element_infinite_sorted_array(arr, target))
# test cases for above function
arr = [1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 7, 7, 8,
       9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
target = 2
print(position_element_infinite_sorted_array(arr, target))
# test cases for above function
arr = [1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 7, 7, 8,
       9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
target = 0
print(position_element_infinite_sorted_array(arr, target))
# test cases for above function
arr = [1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 7, 7, 8,
       9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
target = 13
print(position_element_infinite_sorted_array(arr, target))
