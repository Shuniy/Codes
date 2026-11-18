def RodCuttingRecursive(lenghts: list[int], prices: list[int], rodLength: int) -> int:
    """
    Recursively calculates the maximum price that can be obtained by cutting a rod of length `rodLength` into smaller rods using the given lengths and prices.

    Parameters:
        - lenghts (list[int]): A list of integers representing the lengths of the available rods.
        - prices (list[int]): A list of integers representing the prices of the available rods.
        - rodLength (int): The length of the rod to be cut.

    Returns:
        - int: The maximum price that can be obtained by cutting the rod.
    """
    return RodCuttingRecursiveHelper(lenghts, prices, rodLength, 0, 0)


def RodCuttingRecursiveHelper(lenghts: list[int], prices: list[int], rodLength: int, index, maxPrice) -> int:
    """
    Recursively calculates the maximum price that can be obtained by cutting a rod of length `rodLength` into smaller rods using the given lengths and prices.

    Parameters:
        - lenghts (list[int]): A list of integers representing the lengths of the available rods.
        - prices (list[int]): A list of integers representing the prices of the available rods.
        - rodLength (int): The length of the rod to be cut.
        - index (int): The current index in the `lenghts` and `prices` lists.
        - maxPrice (int): The maximum price obtained so far.

    Returns:
        - int: The maximum price that can be obtained by cutting the rod.
    """
    if index >= len(lenghts) or rodLength <= 0:
        return maxPrice

    output1 = float("-inf")
    output2 = float("-inf")
    if lenghts[index] <= rodLength:
        output1 = RodCuttingRecursiveHelper(
            lenghts, prices, rodLength - lenghts[index], index, maxPrice + prices[index])
    output2 = RodCuttingRecursiveHelper(
        lenghts, prices, rodLength, index + 1, maxPrice)
    return max(output1, output2)


lenghts: list[int] = [i for i in range(1, 9)]
prices: list[int] = [1, 5, 8, 9, 10, 17, 17, 20]
rodLength: int = 8
print(
    f"Max price we get from rod length {rodLength} with Prices: {prices} is: {RodCuttingRecursive(lenghts, prices, rodLength)}")


def RodCuttingDP(lenghts: list[int], prices: list[int], rodLength: int) -> int:
    """
    Generate the maximum profit from cutting a rod of a given length using dynamic programming.

    Parameters:
    - lenghts: a list of integers representing the possible lengths of rod pieces available for cutting
    - prices: a list of integers representing the prices of each rod piece corresponding to lengths in 'lenghts'
    - rodLength: an integer representing the total length of the initial rod

    Returns:
    - An integer representing the maximum profit achievable by cutting the rod
    """
    dp: list[list[int]] = [
        [0 for _ in range(rodLength + 1)] for _ in range(len(lenghts) + 1)]
    for i in range(1, len(lenghts) + 1):
        for j in range(rodLength + 1):
            if lenghts[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], prices[i - 1] +
                               dp[i][j - lenghts[i - 1]])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[len(lenghts)][rodLength]


lenghts: list[int] = [i for i in range(1, 9)]
prices: list[int] = [1, 5, 8, 9, 10, 17, 17, 20]
rodLength: int = 8
print(
    f"Max price we get from rod length {rodLength} with Prices: {prices} is: {RodCuttingDP(lenghts, prices, rodLength)}")
