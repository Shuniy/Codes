# Naive
# Time : O(n^2)
# Space : O(n)
def longest_increasing_subsequence(array):
    sequences = [None for _ in array]
    lengths = [1 for _ in array]
    max_length_index = 0

    for i in range(len(array)):
        current_number = array[i]
        for j in range(0, i):
            other_num = array[j]
            if other_num < current_number and lengths[j] + 1 >= lengths[i]:
                lengths[i] = lengths[j] + 1
                sequences[i] = j
        if lengths[i] >= lengths[max_length_index]:
            max_length_index = i
    return build_sequence(array, sequences, max_length_index)

def build_sequence(array, sequences, current_index):
    sequence = []
    while current_index is not None:
        sequence.append(array[current_index])
        current_index = sequences[current_index]
    return list(reversed(sequence))


# Time : O(nlogn)
# Space : O(n)
def longest_increasing_subsequence(array):
    sequences = [None for _ in array]
    indices = [None for _ in range(len(array) + 1)]
    length = 0

    for i, num in enumerate(array):
        new_length = binary_search(1, length, indices, array, num)
        sequences[i] = indices[new_length - 1]
        indices[new_length] = i
        length = max(length, new_length)
    return build_sequence(array, sequences, indices[length])

def binary_search(start_index, end_index, indices, array, num):
    if start_index > end_index:
        return start_index

    middle_index = (start_index + end_index) // 2
    if array[indices[middle_index]] < num:
            start_index = middle_index + 1
    else:
        end_index = middle_index + 1
    return binary_search(start_index, end_index, indices, array, num)

