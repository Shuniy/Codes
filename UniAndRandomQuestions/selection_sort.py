# Time : O(n^2), Space : O(1)
def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

def selection_sort(array):
    current_index = 0
    while current_index < len(array) - 1:
        smallest_index = current_index
        for i in range(current_index + 1, len(array)):
            if array[smallest_index] > array[i]:
                smallest_index = i
        swap(current_index, smallest_index, array)
        current_index += 1
    return array
