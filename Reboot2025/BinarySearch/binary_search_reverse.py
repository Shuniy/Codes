def binary_search_reverse(arr, target):
    """
    Perform a binary search on the given array to find the target element.
    
    Parameters:
    arr (list): The input sorted list to be searched.
    target (int): The element to be searched in the list.
    
    Returns:
    int: The index of the target element if found, otherwise -1.
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

def test_binary_search_reverse():
    """
    Test the binary_search_reverse function with various input cases.
    """
    assert binary_search_reverse([9, 7, 5, 3, 1], 3) == 3
    assert binary_search_reverse([9, 7, 5, 3, 1], 9) == 0
    assert binary_search_reverse([9, 7, 5, 3, 1], 2) == -1
    assert binary_search_reverse([], 5) == -1
    
test_binary_search_reverse()