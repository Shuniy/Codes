# Avg Time : O(n^2)
# Worst Time : O(n^3)

# Space : O(n^2)
def four_number_sum(array, target_sum):
    all_pairs_sum = {}
    quadruples = []

    for i in range(1, len(array) - 1):
        for j in range(i + 1, len(array)):
            current_sum = array[i] + array[j]

            difference = target_sum - current_sum

            if difference in all_pairs_sum:
                for pair in all_pairs_sum[difference]:
                    quadruples.append([pair] + [array[i], array[j]])
        for k in range(0, i):
            current_sum  = array[i] + array[k]

            if current_sum not in all_pairs_sum:
                all_pairs_sum[current_sum] = [[array[k], array[i]]]
            else:
                all_pairs_sum[current_sum].append([array[k], array[i]])

    return quadruples


