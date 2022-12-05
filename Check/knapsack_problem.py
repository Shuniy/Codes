# Time : O(nc)
# Space : (nc) // n is the number of items and c is capacity

def knapsack_problem(items, capacity):
    knapsack_dp = [[0 for i in range(capacity + 1)] for y in range(len(items) + 1)]

    for i in range(1, len(items) + 1):
        current_weight = items[i - 1][1]
        current_value = items[i - 1][0]

        for j in range(capacity + 1):
            if current_weight > j:
                knapsack_dp[i][j] = knapsack_dp[i - 1][j]

            else:
                knapsack_dp[i][j] = max(knapsack_dp[i - 1][j], knapsack_dp[i - 1][j - current_weight] + current_value)

    return [knapsack_dp[-1][-1], get_knapsack_items(knapsack_dp, items)]

def get_knapsack_items(knapsack_dp, items):
    sequence = []

    i = len(knapsack_dp) - 1
    j = len(knapsack_dp[0]) - 1

    while i > 0:
        if knapsack_dp[i][j] == knapsack_dp[i - 1][j]:
            i -= 1
        else:
            sequence.append(i - 1) # Or you can append the value or item
            j -= items[i - 1][1]
            i -= 1
        if j == 0:
            break

    return list(reversed(sequence))

