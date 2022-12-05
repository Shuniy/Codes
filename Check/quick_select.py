# Time : O(n)
# Space : O(1)

def quick_select(array, k):
    position = k - 1
    return quick_select_helper(array, 0, len(array) - 1, position)

def quick_select_helper(array, start_index, end_index, position):
    while True:
        if start_index > end_index:
            raise Exception("Your algorithm sucks as this will not work, check out")

        pivot_index = start_index
        left_index = pivot_index + 1
        right_index = end_index

        while left_index <= right_index:
            if array[left_index] > array[pivot_index] and array[right_index] < array[pivot_index]:
                array[left_index], array[right_index] = array[right_index], array[left_index]

            if array[left_index] <= array[pivot_index]:
                left_index += 1
            if array[right_index] >= array[pivot_index]:
                right_index -= 1

        array[pivot_index], array[right_index] = array[right_index], array[pivot_index]

        if right_index == position:
            return array[right_index]
        elif right_index < position:
            start_index = right_index + 1
        else:
            end_index = right_index - 1
