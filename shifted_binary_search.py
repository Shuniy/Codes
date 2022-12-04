# Time : O(logn)
# Space : O(logn)

def shifted_binary_search(array, target):
    return shifted_binary_search_helper(array, target, 0, len(array) - 1)

def shifted_binary_search_helper(array, target, left, right):
    if left > right:
        return -1

    middle = (left + right) // 2

    potential_match = array[middle]
    left_num = array[left]
    right_num = array[right]

    if target == potential_match:
        return middle

    elif left_num <= potential_match:
        if target < potential_match and target >= left_num:
            return shifted_binary_search_helper(array, target, left, middle - 1)
        else:
            return shifted_binary_search_helper(array, target, middle + 1, right)
    else:
        if target > potential_match and target <= right_num:
            return shifted_binary_search_helper(array, target, middle + 1, right)
        else:
            return shifted_binary_search_helper(array, target, left, middle - 1)

# Time : O(logn)
# Space : O(1)


def shifted_binary_search(array, target):
    return shifted_binary_search_helper(array, target, 0, len(array) - 1)


def shifted_binary_search_helper(array, target, left, right):
    while left <= right:

        middle = (left + right) // 2
        potential_match = array[middle]
        left_num = array[left]
        right_num = array[right]

        if target == potential_match:
            return middle

        elif left_num <= potential_match:
            if target < potential_match and target >= left_num:
                right = middle - 1
            else:
                left = middle + 1
        else:
            if target > potential_match and target <= right_num:
                left = middle - 1
            else:
                right = middle - 1

    return -1
