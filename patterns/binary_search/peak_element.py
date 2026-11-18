def peak_element(arr):
    """
    Find and return the index of a peak element in a given array using binary search.

    Args:
    - arr: An array of integers

    Returns:
    - The index of a peak element in the array
    """
    if len(arr) <= 1:
        return arr[0]

    left = 0
    right = len(arr) - 1
    while left < right:
        mid = left + (right - left) // 2
        if mid > 0 and mid < len(arr) - 1 and arr[mid - 1] < arr[mid] > arr[mid + 1]:
            return mid
        if arr[mid] > arr[mid + 1]:
            right = mid - 1
        else:
            left = mid + 1
    return left


# test cases for above function
arr = [1, 2, 3, 1]
print(peak_element(arr))

arr = [1, 2, 1, 3, 5, 6, 4]
print(peak_element(arr))

arr = [1]
print(peak_element(arr))

arr = [1, 2]
print(peak_element(arr))
