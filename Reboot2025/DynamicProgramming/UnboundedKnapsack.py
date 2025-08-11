def UnboundedKnapsackRecursive(values: list[int], weights: list[int], capacity: int) -> int:
    return UnboundedKnapsackRecursiveHelper(values, weights, capacity, 0, 0)


def UnboundedKnapsackRecursiveHelper(values: list[int], weights: list[int], capacity: int, index: int, profit: int) -> int:
    if index >= len(weights) or capacity <= 0:
        return profit
    if weights[index] <= capacity:
        output1 = UnboundedKnapsackRecursiveHelper(
            values, weights, capacity - weights[index], index, profit + values[index])
        output2 = UnboundedKnapsackRecursiveHelper(
            values, weights, capacity, index + 1, profit)
    else:
        return UnboundedKnapsackRecursiveHelper(
            values, weights, capacity, index + 1, profit)
    return max(output1, output2)


values: list[int] = [25, 30, 15]
weights: list[int] = [15, 5, 10]
capacity: int = 100
print(
    f"Maximum profit with values: {values} and weights: {weights} with capacity: {capacity} is: {UnboundedKnapsackRecursive(values, weights, capacity)}")


def UnboundedKnapsackMemo(values: list[int], weights: list[int], capacity: int) -> int:
    memo: list[list[int]] = [
        [-1 for _ in range(capacity + 1)] for _ in range(len(weights) + 1)]
    return UnboundedKnapsackMemoHelper(values, weights, capacity, 0, 0, memo)


def UnboundedKnapsackMemoHelper(values: list[int], weights: list[int], capacity: int, index: int, profit: int, memo) -> int:
    if index >= len(weights) or capacity <= 0:
        return profit
    if memo[index][capacity] != -1:
        return memo[index][capacity]
    if weights[index] <= capacity:
        output1 = UnboundedKnapsackRecursiveHelper(
            values, weights, capacity - weights[index], index, profit + values[index])
        output2 = UnboundedKnapsackRecursiveHelper(
            values, weights, capacity, index + 1, profit)
    else:
        memo[index][capacity] = UnboundedKnapsackRecursiveHelper(
            values, weights, capacity, index + 1, profit, memo)
        return memo[index][capacity]
    memo[index][capacity] = max(output1, output2)
    return memo[index][capacity]


values: list[int] = [25, 30, 15]
weights: list[int] = [15, 5, 10]
capacity: int = 100
print(
    f"Maximum profit with values: {values} and weights: {weights} with capacity: {capacity} is: {UnboundedKnapsackRecursive(values, weights, capacity)}")


def UnboundedKnapsackDP(values: list[int], weights: list[int], capacity: int) -> int:
    dp: list[list[int]] = [
        [0 for _ in range(capacity + 1)] for _ in range(len(weights) + 1)]
    for i in range(1, len(weights) + 1):
        for j in range(capacity + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(values[i - 1] + dp[i]
                               [j - weights[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[len(weights)][capacity]


values: list[int] = [25, 30, 15]
weights: list[int] = [15, 5, 10]
capacity: int = 100
print(
    f"Maximum profit with values: {values} and weights: {weights} with capacity: {capacity} is: {UnboundedKnapsackDP(values, weights, capacity)}")
