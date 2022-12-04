# It is unstable
# Time : O(nlogn) , Worst : O(n^2)
# Space : O(logn) // Recursive // Apply on the smallest of the array

def quick_sort(array):
    quick_sort_helper(array, 0, len(array) - 1)
    return array

def quick_sort_helper(array, start_index, end_index):
    if start_index > end_index:
        return

    pivot_index = start_index
    left_index = start_index + 1
    right_index = end_index

    while right_index >= left_index:
        if array[left_index] > array[pivot_index] and array[pivot_index] > array[right_index]:
            swap(left_index, right_index, array)
        if array [left_index] <= array[pivot_index]:
            left_index += 1
        if array[right_index] >= array[pivot_index]:
            right_index -= 1

    swap(pivot_index, right_index, array)
    
    left_subarray_is_smaller = right_index - 1 - start_index < end_index - (right_index + 1)

    if left_subarray_is_smaller:
        quick_sort_helper(array, start_index, right_index - 1)
        quick_sort_helper(array, right_index + 1, end_index)
    else:
        quick_sort_helper(array, right_index + 1, end_index)
        quick_sort_helper(array, start_index, right_index - 1)
        


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
