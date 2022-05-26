# Time : O(nlogn)
# Space : O(1)
def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


def heap_sort(array):
    build_max_heap(array)

    for end_index in reversed(range(1, len(array))):
        swap(0, end_index, array)

        sift_down(0, end_index - 1, array)

    return array

def build_max_heap(array):
    first_parent_index = (len(array) - 1) // 2
    for current_index in reversed(range(first_parent_index + 1)):
        sift_down(current_index, len(array) - 1, array)

def sift_down(current_index, end_index, heap):
    child_one_index = current_index * 2 + 1
    while child_one_index <= end_index:
        child_two_index = current_index * 2 + 2 if current_index * 2 + 2 <= end_index else -1

        if child_two_index > -1 and heap[child_two_index] > heap[child_one_index]:
            index_to_swap = child_two_index
        else:
            index_to_swap = child_one_index

        if heap[index_to_swap] > heap[current_index]:
            swap(current_index, index_to_swap, heap)
            current_index = index_to_swap
            child_one_index = current_index * 2 + 1
        else:
            return

