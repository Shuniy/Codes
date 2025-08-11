def ceil_element_sorted_array(arr, target):
    left = 0
    right = len(arr) - 1
    candidate = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] > target:
            candidate = mid
            right = mid - 1
        else:
            left = mid + 1
    return arr[candidate] if candidate != -1 else None


# test cases for above function
arr = [1, 2, 3, 4, 5, 6, 8, 9, 10]
target = 7
print(ceil_element_sorted_array(arr, target))
