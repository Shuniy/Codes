def binary_search(arr, target):
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
            right = mid - 1
        else:
            left = mid + 1
    return -1

# generate test cases for binary search
def test_binary_search():
    """
    This function is a test for the binary_search function. It prints the result of binary_search and asserts the expected results of binary_search with different inputs.
    """
    assert binary_search([1, 3, 5, 7, 9], 3) == 1
    assert binary_search([1, 3, 5, 7, 9], 9) == 4
    assert binary_search([1, 3, 5, 7, 9], 2) == -1
    assert binary_search([], 5) == -1
    
test_binary_search()
