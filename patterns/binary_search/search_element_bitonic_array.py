def peak_element(arr):
    """
    This function finds a peak element in an array using binary search. 
    It takes an array as input and returns the index of the peak element.
    """
    n = len(arr)
    if n <= 1:
        return arr[n]

    left = 0
    right = n - 1
    while left < right:
        mid = left + (right - left) // 2
        if mid > 0 and mid < n - 1 and arr[mid - 1] < arr[mid] > arr[mid + 1]:
            return mid
        if arr[mid] > arr[mid + 1]:
            right = mid - 1
        else:
            left = mid + 1
    return left


def binary_search(arr, target):
    """
    Perform a binary search on the input array to find the target value.

    Args:
        arr (list): The input array to be searched.
        target (int): The target value to be found in the array.

    Returns:
        int: The index of the target value in the array, or -1 if the target is not found.
    """
    if not arr:
        return -1
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def reverse_binary_search(arr, target):
    """
    Perform a reverse binary search on the given array to find the target element.

    Args:
        arr (list): The input array to be searched.
        target (int): The target element to be found in the array.

    Returns:
        int: The index of the target element in the array, or -1 if the element is not found.
    """
    if not arr:
        return -1
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def search_element_bitonic_array(arr, target):
    """
    Function to search for an element in a bitonic array.

    Parameters:
    - arr: a list of integers representing the bitonic array
    - target: an integer to search for in the array

    Returns:
    - The index of the element if found, otherwise -1
    """
    if not arr:
        return -1

    peak_index = peak_element(arr)

    if arr[peak_index] == target:
        return peak_index

    if arr[0] <= target:
        return binary_search(arr[:peak_index + 1], target)
    return reverse_binary_search(arr[peak_index + 1:], target)
