def search_nearly_sorted_array(arr, target):
    """
    Search for a target value in a nearly sorted array.

    Parameters:
    arr (list): A nearly sorted array to search in.
    target (int): The value to search for in the array.

    Returns:
    int: The index of the target value in the array, or -1 if the target is not found.
    """
    # condition could have been at i, i + 1 and i - 1
    left = 0
    right = len(arr) - 1
    while left >= 0 and right <= len(arr) - 1 and left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        if arr[mid + 1] == target:
            return mid + 1
        if arr[mid - 1] == target:
            return mid - 1
        if arr[mid] > target:
            right = mid - 2
        else:
            left = mid + 2

    return -1


# test cases for above function
arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target1 = 5
assert search_nearly_sorted_array(arr1, target1) == 4

arr2 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target2 = 35
assert search_nearly_sorted_array(arr2, target2) == -1

arr2 = [10, 3, 40, 20, 50, 80, 70]
target2 = 40
assert search_nearly_sorted_array(arr2, target2) == 2

arr2 = [10, 3, 40, 20, 50, 80, 70]
target2 = 80
assert search_nearly_sorted_array(arr2, target2) == 5

arr2 = [10, 3, 40, 20, 50, 80, 70]
target2 = 70
assert search_nearly_sorted_array(arr2, target2) == 6

arr2 = [10, 3, 40, 20, 50, 80, 70]
target2 = 10
assert search_nearly_sorted_array(arr2, target2) == 0
