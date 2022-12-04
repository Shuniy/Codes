# Find amximum number of ways or total number of ways to make total Sum from given coins
def CoinChange1REcursion(coins: list[int], totalSum: int) -> int:
    return CoinChange1RecursionHelper(coins, totalSum, 0)


def CoinChange1RecursionHelper(coins: list[int], totalSum: int, index: int) -> int:
    if index >= len(coins):
        return 0
    if totalSum <= 0:
        return 1
    if coins[index] <= totalSum:
        output1 = CoinChange1RecursionHelper(
            coins, totalSum - coins[index], index)
        output2 = CoinChange1RecursionHelper(coins, totalSum, index + 1)
    else:
        return CoinChange1RecursionHelper(coins, totalSum, index + 1)

    return output1 + output2


coins: list[int] = [1, 2, 3]
totalSum: int = 4
print(
    f"Max Number of ways for coins {coins} to make sum of {totalSum} are: {CoinChange1REcursion(coins, totalSum)}")


def CoinChange1DP(coins: list[int], totalSum: int) -> int:
    if totalSum <= 0:
        return 1
    dp: list[list[int]] = [
        [0 for _ in range(totalSum + 1)] for _ in range(len(coins) + 1)]
    for i in range(len(coins) + 1):
        dp[i][0] = 1

    for i in range(1, len(coins) + 1):
        for j in range(totalSum + 1):
            if coins[i - 1] <= j:
                dp[i][j] = dp[i][j - coins[i - 1]] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[len(coins)][totalSum]


coins: list[int] = [1, 2, 3]
totalSum: int = 4
print(
    f"Max Number of ways for coins {coins} to make sum of {totalSum} are: {CoinChange1DP(coins, totalSum)}")