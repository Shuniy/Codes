def find_element_sorted_rotated_array(arr, target):
    """
    Function to search for a target element in a sorted and rotated array.

    Args:
        arr (list): A sorted and rotated array of integers.
        target (int): The target element to search for.

    Returns:
        int: The index of the target element in the array, or -1 if it is not found.
    """
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        if arr[left] <= arr[mid]:
            # section 1
            if arr[left] <= target <= arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # section 2
            if arr[mid] <= target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


# test cases for above function
arr = [4, 5, 6, 7, 0, 1, 2]
target = 0
assert (find_element_sorted_rotated_array(arr, target) == 4)
arr = [4, 5, 6, 7, 0, 1, 2]
target = 4
assert (find_element_sorted_rotated_array(arr, target) == 0)
arr = [4, 5, 6, 7, 0, 1, 2]
target = 2
assert (find_element_sorted_rotated_array(arr, target) == 6)
arr = [4, 5, 6, 7, 0, 1, 2]
target = 5
assert (find_element_sorted_rotated_array(arr, target) == 1)
arr = [4, 5, 6, 7, 0, 1, 2]
target = 1
assert (find_element_sorted_rotated_array(arr, target) == 5)
arr = [4, 5, 6, 7, 0, 1, 2]
target = 6
assert (find_element_sorted_rotated_array(arr, target) == 2)
arr = [4, 5, 6, 7, 0, 1, 2]
target = 7
assert (find_element_sorted_rotated_array(arr, target) == 3)
