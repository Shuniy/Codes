# Time : O(n^2) Space: O(1)
# Optimized Bubble Sort
def bubble_sort(array):
    is_sorted = False
    Counter = 0
    while not is_sorted:
        is_sorted = True
        for i in range(len(array) - 1- Counter):
            if array[i] > array[i + 1]:
                swap(i, i + 1, array)
                is_sorted = False
        Counter += 1
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
