def index_first_1_infinite_sorted_array(arr):
    """
    A function to find the index of the first occurrence of 1 in an infinite sorted array.
    Params:
        arr: The infinite sorted array
    Returns:
        The index of the first occurrence of 1 in the array, or -1 if 1 is not found.
    """
    # First it is a binary array
    # second it is an infinite array
    # third it is a sorted array
    left = 0
    right = 1
    candidate = -1
    while left <= right:
        while arr[right] < 1:
            left = right
            right = right * 2
        mid = left + (right - left) // 2
        if arr[mid] == 0:
            left = mid + 1
        else:
            candidate = mid
            right = mid - 1
    return candidate


# test cases for above
arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
       1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
assert index_first_1_infinite_sorted_array(arr) == 12
