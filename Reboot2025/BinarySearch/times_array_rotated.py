def number_of_times_array_rotated(arr):
    """
    Function to find the number of times an array is rotated.

    Parameters:
    arr (list): The input array.

    Returns:
    int: The number of times the array is rotated.
    """
    left = 0
    right = len(arr) - 1
    min_element_index = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] > arr[mid + 1]:
            min_element_index = mid + 1
            break
        if arr[mid] < arr[mid - 1]:
            min_element_index = mid
            break
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid
    if min_element_index == -1:
        return 0
    return min(len(arr) - min_element_index, min_element_index)


# test cases for above function
arr = [15, 18, 2, 3, 6, 12]
assert number_of_times_array_rotated(arr) == 2
arr = [7, 9, 11, 12, 5]
assert number_of_times_array_rotated(arr) == 1
arr = [7, 9, 11, 12, 15]
assert number_of_times_array_rotated(arr) == 0
