# Time : O(n^2)
# Space : O(n)

def max_sum_increasing_subsequence(array):
    sequences = [None for _ in array]
    sums = array
    max_sum_index = 0

    for i in range(len(array)):
        current_num = array[i]

        for j in range(0, i):
            other_num = array[j]
            if other_num < current_num and sums[j] + current_num >= sums[i]: # Strictly Increasing because of (subsequence)
                sums[i] = sums[j] + current_num
                sequences[i] = j
        if sums[i] >= sums[max_sum_index]:
            max_sum_index = i

    return (sums[max_sum_index], build_sequence(array, sequences, max_sum_index))

def build_sequence(array, sequences, current_index):
    sequence = []

    while current_index is not None:
        sequence.append(array[current_index])
        current_index = sequences[current_index]

    return list(reversed(sequence))
