# Find a subarray if sorted make entire array sorted

# Time : O(n)
# Space = O(1)
def subarray_sort(array):
    minimum_out_of_order = float("inf")
    maximum_out_of_order = float("-inf")

    for i in range(len(array)):
        num = array[i]

        if is_out_of_order(i, num, array):
            minimum_out_of_order = min(minimum_out_of_order, num)
            maximum_out_of_order = max(maximum_out_of_order, num)

    if minimum_out_of_order == float("inf"):
        return [-1, -1]

    subarray_left_index = 0
    while minimum_out_of_order >= array[subarray_left_index]:
        subarray_left_index += 1

    subarray_right_index = len(array) - 1
    while maximum_out_of_order <= array[subarray_right_index]:
        subarray_right_index -= 1

    return [subarray_left_index, subarray_right_index]

def is_out_of_order(i, num, array):
    if i == 0:
        return num > array[i + 1]
    if i == len(array) - 1:
        return num < array[i - 1]

    return num > array[i + 1] or num < array[i - 1]