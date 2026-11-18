def max_element_bitonic_array(arr):
    if len(arr) <= 1:
        return arr[0]

    left = 0
    right = len(arr) - 1
    while left < right:
        mid = left + (right - left) // 2
        if mid > 0 and mid < len(arr) - 1 and arr[mid - 1] < arr[mid] > arr[mid] + 1:
            return mid
        if arr[mid] > arr[mid + 1]:
            right = mid - 1
        else:
            left = mid + 1
    return left


# test cases for above function
arr = [1, 2, 3, 1]
print(max_element_bitonic_array(arr))

arr = [1, 2, 3, 3, 5, 6, 4, 3, 2]
print(max_element_bitonic_array(arr))

arr = [1]
print(max_element_bitonic_array(arr))

arr = [1, 2]
print(max_element_bitonic_array(arr))
