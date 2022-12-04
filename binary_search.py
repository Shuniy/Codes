# Time : O(log(n)), Space : O(1)
def binary_search_helper(array, left, right, target):
    if right < 1:
        print("Invalid")
        return
    if right == 1:
        print("Found at index : ", left)
        return
    if left > right:
        return

    middle = (left + right - 1) // 2
    if array[middle] == target:
        print("Found at Index : ", middle)
        return
    elif array[middle] < target:
        binary_search_helper(array, middle + 1, right, target)
    else:
        binary_search_helper(array, left, middle - 1, target)


def binary_search(array, target):
    binary_search_helper(array, 0, len(array), target)

def binary_search_iterative(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = (left + right) // 2
        if target == array[middle]:
            return middle
        elif target < array[middle]:
            right = middle - 1
        else:
            left = middle + 1