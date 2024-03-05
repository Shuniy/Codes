def floor_element_sorted_array(arr, target):
    """
    Perform binary search on a sorted array to find the largest element less than or equal to the target value.

    Parameters:
    - arr: a sorted array of integers
    - target: the target value to search for

    Returns:
    - The largest element less than or equal to the target value, or None if no such element is found.
    """
    left = 0
    right = len(arr) - 1
    candidate = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] > target:
            right = mid - 1
        else:
            candidate = mid
            left = mid + 1
    return arr[candidate] if candidate != -1 else None


# test cases for above function
arr = [1, 2, 3, 4, 5, 6, 8, 9, 10]
target = 7
print(floor_element_sorted_array(arr, target))
