def first_last_occurence_array(arr, target):
    """
    Find the first and last occurrence of the target in the array.

    Args:
    arr (list): The input array.
    target: The target value to find in the array.

    Returns:
    tuple: A tuple containing the first and last occurrence indices of the target in the array.
    """
    left = 0
    right = len(arr) - 1
    first = -1
    last = -1
    # calculate first occurence
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            first = mid
            right = mid - 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            last = mid
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return (first, last)


# test cases for above function
arr = [1, 2, 3, 4, 5, 6, 7, 7,7,7,7,7, 8, 9, 10]
target = 7
print(first_last_occurence_array(arr, target))
