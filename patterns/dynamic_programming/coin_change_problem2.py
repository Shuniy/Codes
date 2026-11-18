# Find the minimum number of coins needed to create the amount
def CoinChange2Recursion(coins: list[int], totalSum: int) -> int:
    """
    A recursive function to find the minimum number of coins needed to create a given total sum from the given coins.

    Args:
        coins (list[int]): The list of coin denominations available.
        totalSum (int): The total sum to be achieved.

    Returns:
        int: The minimum number of coins needed to create the total sum using the given coins.
    """
    return CoinChange2RecursionHelper(coins, totalSum, 0)


def CoinChange2RecursionHelper(coins: list[int], totalSum: int, index: int) -> int:
    """
    A recursive function to find the minimum number of coins needed to create a given total sum from the given coins.

    Args:
        coins (list[int]): The list of coin denominations available.
        totalSum (int): The total sum to be achieved.
        index (int): The current index in the coins list.

    Returns:
        int: The minimum number of coins needed to create the total sum using the given coins.
    """
    if index >= len(coins):
        return float("inf")
    if totalSum <= 0:
        # Completed, no more coin needed
        return 0
    if coins[index] <= totalSum:
        output1 = 1 + CoinChange2RecursionHelper(
            coins, totalSum - coins[index], index)
        output2 = CoinChange2RecursionHelper(coins, totalSum, index + 1)
    else:
        return CoinChange2RecursionHelper(coins, totalSum, index + 1)

    return min(output1, output2)


coins: list[int] = [1, 2, 5]
totalSum: int = 11
print(
    f"Max Number of ways for coins {coins} to make sum of {totalSum} are: {CoinChange2Recursion(coins, totalSum)}")

coins: list[int] = [2]
totalSum: int = 3
print(
    f"Max Number of ways for coins {coins} to make sum of {totalSum} are: {CoinChange2Recursion(coins, totalSum)}")

coins: list[int] = [2]
totalSum: int = 0
print(
    f"Max Number of ways for coins {coins} to make sum of {totalSum} are: {CoinChange2Recursion(coins, totalSum)}")


def CoinChange2DP(coins: list[int], totalSum: int) -> int:
    """
    A dynamic programming function to find the minimum number of coins needed to create a given total sum from the given coins.

    Args:
        coins (list[int]): The list of coin denominations available.
        totalSum (int): The total sum to be achieved.

    Returns:
        int: The minimum number of coins needed to create the total sum using the given coins.
    """
    if totalSum <= 0:
        return 0
    dp: list[list[float]] = [
        [float("inf") for _ in range(totalSum + 1)] for _ in range(len(coins) + 1)]
    for i in range(len(coins) + 1):
        dp[i][0] = 0

    for i in range(1, len(coins) + 1):
        for j in range(totalSum + 1):
            if coins[i - 1] <= j:
                dp[i][j] = min(1 + dp[i][j - coins[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[len(coins)][totalSum]


coins: list[int] = [1, 2, 5]
totalSum: int = 11
print(
    f"Max Number of ways for coins {coins} to make sum of {totalSum} are: {CoinChange2DP(coins, totalSum)}")

coins: list[int] = [2]
totalSum: int = 3
print(
    f"Max Number of ways for coins {coins} to make sum of {totalSum} are: {CoinChange2DP(coins, totalSum)}")

coins: list[int] = [2]
totalSum: int = 0
print(
    f"Max Number of ways for coins {coins} to make sum of {totalSum} are: {CoinChange2DP(coins, totalSum)}")
