def RodCuttingRecursive(lenghts: list[int], prices: list[int], rodLength: int) -> int:
    return RodCuttingRecursiveHelper(lenghts, prices, rodLength, 0, 0)


def RodCuttingRecursiveHelper(lenghts: list[int], prices: list[int], rodLength: int, index, maxPrice) -> int:
    if index >= len(lenghts) or rodLength <= 0:
        return maxPrice
    
    output1 = float("-inf")
    output2 = float("-inf")
    if lenghts[index] <= rodLength:
        output1 = RodCuttingRecursiveHelper(lenghts, prices, rodLength - lenghts[index], index, maxPrice + prices[index])
    output2 = RodCuttingRecursiveHelper(lenghts, prices, rodLength, index + 1, maxPrice)
    return max(output1, output2)

lenghts: list[int] = [i for i in range(1, 9)]
prices: list[int] = [1,5,8,9,10,17,17,20]
rodLength: int = 8
print(f"Max price we get from rod length {rodLength} with Prices: {prices} is: {RodCuttingRecursive(lenghts, prices, rodLength)}")


def RodCuttingDP(lenghts: list[int], prices: list[int], rodLength: int) -> int:
    dp: list[list[int]] = [[0 for _ in range(rodLength + 1)] for _ in range(len(lenghts) + 1)]
    for i in range(1, len(lenghts) + 1):
        for j in range(rodLength + 1):
            if lenghts[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], prices[i - 1] + dp[i][j - lenghts[i - 1]])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[len(lenghts)][rodLength]

lenghts: list[int] = [i for i in range(1, 9)]
prices: list[int] = [1, 5, 8, 9, 10, 17, 17, 20]
rodLength: int = 8
print(
    f"Max price we get from rod length {rodLength} with Prices: {prices} is: {RodCuttingDP(lenghts, prices, rodLength)}")
