# Naive or Unoptimized:
# Time : O(n^2 * k)
# Space : O(n * k) can be optimized to O(n) and k = 2

# Optimized
# Time : O(n * k)
# Space : O(n) and k = 2

# Time : O(n * k)
# Space : O(n * k)
def max_profit_with_transactions(prices, k):
    if not len(prices):
        return 0

    profits = [[0 for d in prices] for _ in range(k + 1)]

    for t in range(1, k + 1):
        max_thus_far = float('-inf')
        for d in range(1, len(prices)):
            max_thus_far = max(max_thus_far, profits[t - 1][d - 1] - prices[d - 1])
            profits[t][d] = max(profits[t][d - 1], max_thus_far + prices[d])

    
    return profits[-1][-1]

# Time : O(n * k)
# Space : O(n)

def max_profit_with_transactions(prices, k):
    if not len(prices):
        return 0

    even_profits = [0 for d in prices]
    odd_profits = [0 for d in prices]

    for t in range(1, k + 1):
        max_thus_far = float("-inf")

        if t % 2 == 1:
            current_profits = odd_profits
            previous_profits = even_profits
        else:
            current_profits = even_profits
            previous_profits = odd_profits

        for d in range(1, len(prices)):
            max_thus_far = max(max_thus_far, previous_profits[d - 1] - prices[d - 1])
            current_profits[d] = max(current_profits[d - 1], max_thus_far + prices[d])

    return even_profits[-1] if k % 2 == 0 else odd_profits[-1]