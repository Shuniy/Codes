# Two ways to merge sort
# Space Complexity differs in ways
# Using new array and inplace sort

# Naive
# Time : O(nlogn)
# Space : O(nlogn)
def merge_sort(array):
    if len(array) == 1:
        return array

    middle_index = len(array) // 2
    left_half = array[:middle_index]
    right_half = array[middle_index:]

    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)
    return merge(sorted_left, sorted_right)

def merge(left, right):
    sorted_array = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    if i < len(left):
        sorted_array += left[i:]
    if j < len(right):
        sorted_array += right[j:]

    return sorted_array

# Optimized
# Time : O(nlogn)
# Space : O(n) // inplace that is only one-extra copy of the array
def merge_sort(array):
    if len(array) <= 1:
        return array

    auxilliary_array = array[:]
    merge_sort_helper(array, 0, len(array) - 1, auxilliary_array)
    return array

def merge_sort_helper(main_array, start_index, end_index, auxilliary_array):
    if start_index == end_index:
        return

    middle_index = (start_index + end_index) // 2
    merge_sort_helper(auxilliary_array, start_index, middle_index, main_array)
    merge_sort_helper(auxilliary_array, middle_index, end_index, main_array)
    do_merge(main_array, start_index, middle_index, end_index, auxilliary_array)


def do_merge(main_array, start_index, middle_index, end_index, auxilliary_array):
    k = start_index
    i = start_index
    j = middle_index + 1

    while i <= middle_index and j <= end_index:
        if auxilliary_array[i] <= auxilliary_array[j]:
            main_array[k] = auxilliary_array[i]
            i += 1
        else:
            main_array[k] = auxilliary_array[j]
            j += 1
        k += 1

    while i <= middle_index:
        main_array[k] = auxilliary_array[i]
        i += 1
        k += 1
    while j <= end_index:
        main_array[k] = auxilliary_array[j]
        j += 1
        k += 1
