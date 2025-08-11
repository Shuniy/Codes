def ZeroOneKnapsackProblem(capacity, weights, values) -> int:
    """
    A function that solves the 0-1 Knapsack problem using a helper function.

    Parameters:
    - capacity: an integer representing the maximum weight the knapsack can hold
    - weights: a list of integers representing the weights of the items
    - values: a list of integers representing the values of the items

    Returns:
    - An integer representing the maximum profit that can be achieved
    """
    # Hypothesis: Will always return max profit
    return ZeroOneKnapsackProblemHelper(0, 0, capacity, weights, values)


def ZeroOneKnapsackProblemHelper(index: int, profit: int, capacity: int, weights: list, values: list[int]) -> int:
    """
    A function to solve the 0/1 Knapsack Problem recursively by exploring all possible combinations.

    Parameters:
    - index: int, the current index of the item being considered
    - profit: int, the current total profit
    - capacity: int, the remaining capacity of the knapsack
    - weights: list, a list of weights of the items
    - values: list[int], a list of values of the items

    Returns:
    - int, the maximum profit that can be achieved
    """
    # Hypothesis: Will always return Max Profit
    # Base Condition: If capacity is zero and index is at end
    if capacity <= 0 or index >= len(weights):
        return profit

    if weights[index] <= capacity:
        # Will return max Profit without adding the item
        profit1 = ZeroOneKnapsackProblemHelper(
            index + 1, profit, capacity, weights, values)
        # Will return max profit by adding the item
        profit2 = ZeroOneKnapsackProblemHelper(
            index + 1, profit + values[index], capacity - weights[index], weights, values)
    else:
        return ZeroOneKnapsackProblemHelper(index + 1, profit, capacity, weights, values)
    # Induction: profit will be max of both the profit
    return max(profit1, profit2)


def ZeroOneKnapsackProblemMemo(capacity, weights, values) -> int:
    """
    Calculate the maximum value that can be obtained by filling a knapsack of a given capacity using the items with given weights and values.

    Parameters:
        capacity (int): The maximum capacity of the knapsack.
        weights (List[int]): The weights of the items.
        values (List[int]): The values of the items.

    Returns:
        int: The maximum value that can be obtained by filling the knapsack.
    """
    memo = [[-1 for _ in range(0, capacity + 1)]
            for _ in range(len(weights) + 1)]
    return ZeroOneKnapsackProblemHelperMemo(0, 0, memo, capacity, weights, values)


def ZeroOneKnapsackProblemHelperMemo(index, profit, memo, capacity, weights, values) -> int:
    """
    Calculates the maximum profit that can be obtained from a knapsack problem using the Zero-One algorithm.

    Args:
        index (int): The current index in the weights list.
        profit (int): The current profit obtained.
        memo (List[List[int]]): The memoization table to store previously calculated values.
        capacity (int): The maximum capacity of the knapsack.
        weights (List[int]): The list of weights for each item.
        values (List[int]): The list of values for each item.

    Returns:
        int: The maximum profit that can be obtained from the knapsack problem.
    """
    if capacity <= 0 or index >= len(weights):
        return profit

    if memo[index][capacity] != -1:
        return memo[index][capacity]

    if weights[index] <= capacity:
        # Will return max Profit without adding the item
        profit1 = ZeroOneKnapsackProblemHelper(
            index + 1, profit, capacity, weights, values)
        # Will return max profit by adding the item
        profit2 = ZeroOneKnapsackProblemHelper(
            index + 1, profit + values[index], capacity - weights[index], weights, values)
    else:
        memo[index][capacity] = ZeroOneKnapsackProblemHelper(
            index + 1, profit, capacity, weights, values)
        return memo[index][capacity]

    memo[index][capacity] = max(profit1, profit2)
    return memo[index][capacity]


# Recursion
capacity = 7
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
print(f"Maximum Profit from items  with {weights} and values {values} Recursion: ", ZeroOneKnapsackProblem(
    capacity, weights[:], values[:]))
capacity = 50
weights = [10, 20, 30]
values = [60, 100, 120]
print(f"Maximum Profit from items  with {weights} and values {values} Recursion: ", ZeroOneKnapsackProblem(
    capacity, weights[:], values[:]))

# Memoization
capacity = 7
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
print(f"Maximum Profit from items  with {weights} and values {values} Recursion: ", ZeroOneKnapsackProblemMemo(
    capacity, weights[:], values[:]))
capacity = 50
weights = [10, 20, 30]
values = [60, 100, 120]
print(f"Maximum Profit from items  with {weights} and values {values} Recursion: ", ZeroOneKnapsackProblemMemo(
    capacity, weights[:], values[:]))

# Bottom UP Approach
# We have to convert the recursive code into the top down approach
# Convert the base condition into matrix initialization
# Convert the recursive code into for loop


def ZeroOneKnapsackProblemBottomUp(capacity, weights, values):
    """
    This function solves the 0/1 knapsack problem using the bottom-up dynamic programming approach.
    It takes three parameters: capacity (integer), weights (list of integers), and values (list of integers).
    It returns the maximum value that can be obtained given the capacity, weights, and values.
    """
    if capacity == 0:
        return 0

    dp = [[-1 for _ in range(capacity + 1)] for _ in range(len(weights) + 1)]
    # Base Condition
    for i in range(len(weights) + 1):
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0

    # Now converting recursive code to For loop
    for i in range(1, len(weights) + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] <= j:
                # include or not
                dp[i][j] = max(values[i - 1] + dp[i - 1]
                               [j - weights[i - 1]], dp[i - 1][j])
            else:
                # skip
                dp[i][j] = dp[i - 1][j]

    return dp[len(weights)][capacity]


capacity = 7
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
print(f"Maximum Profit from items  with {weights} and values {values} Top Down: ", ZeroOneKnapsackProblemBottomUp(
    capacity, weights[:], values[:]))
capacity = 50
weights = [10, 20, 30]
values = [60, 100, 120]
print(f"Maximum Profit from items  with {weights} and values {values} Top Down: ", ZeroOneKnapsackProblemBottomUp(
    capacity, weights[:], values[:]))
