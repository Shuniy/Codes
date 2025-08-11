# Recursion
def subsetSumRecursion(arr: list[int], targetSum: int) -> bool:
    """
    Check if there exists a subset of the given array that sums up to the target sum.

    Args:
        arr (list[int]): The input array of integers.
        targetSum (int): The target sum to be checked.

    Returns:
        bool: True if there exists a subset that sums up to the target sum, False otherwise.
    """
    return subsetSumRecursionHelper(arr, targetSum, 0)


def subsetSumRecursionHelper(arr: list[int], targetSum: int, index: int) -> bool:
    """
    Recursively checks if there exists a subset of the given array that sums up to the target sum.

    Args:
        arr (list[int]): The input array of integers.
        targetSum (int): The target sum to be checked.
        index (int): The current index in the array.

    Returns:
        bool: True if there exists a subset that sums up to the target sum, False otherwise.
    """
    if index >= len(arr):
        return False

    if targetSum == 0:
        return True

    if arr[index] <= targetSum:
        output1 = subsetSumRecursionHelper(
            arr, targetSum - arr[index], index + 1)
        output2 = subsetSumRecursionHelper(arr, targetSum, index + 1)
    else:
        return subsetSumRecursionHelper(arr, targetSum, index + 1)

    return output1 or output2


arr: list[int] = [1, 2, 3, 7, 8, 10]
targetSum: int = 11
print(
    f"Target Sum with array {arr} with target {targetSum} is possible: {subsetSumRecursion(arr[:], targetSum)}")

arr: list[int] = [3, 34, 4, 12, 5, 2]
targetSum: int = 9
print(
    f"Target Sum with array {arr} with target {targetSum} is possible: {subsetSumRecursion(arr[:], targetSum)}")

arr: list[int] = [3, 34, 4, 12, 5, 2]
targetSum: int = 30
print(
    f"Target Sum with array {arr} with target {targetSum} is possible: {subsetSumRecursion(arr[:], targetSum)}")

# Memoization


def subsetSumRecursionMemo(arr: list[int], targetSum: int) -> bool:
    """
    Calculates whether it is possible to obtain a sum of `targetSum` from a subset of the given array `arr` using recursion and memoization.

    Parameters:
        arr (list[int]): The input array of integers.
        targetSum (int): The target sum to be checked.

    Returns:
        bool: True if it is possible to obtain a sum of `targetSum` from a subset of `arr`, False otherwise.
    """
    memo: list[list[bool]] = [[False for _ in range(
        targetSum + 1)] for _ in range(len(arr) + 1)]
    for i in range(len(arr) + 1):
        memo[i][0] = True
    return subsetSumRecursionMemoHelper(arr, targetSum, 0, memo)


def subsetSumRecursionMemoHelper(arr: list[int], targetSum: int, index: int, memo: list[list[bool]]) -> bool:
    """
    Recursively checks if there exists a subset of the given array that sums up to the target sum using memoization.

    Args:
        arr (list[int]): The input array of integers.
        targetSum (int): The target sum to be checked.
        index (int): The current index in the array.
        memo (list[list[bool]]): The memoization table.

    Returns:
        bool: True if there exists a subset that sums up to the target sum, False otherwise.
    """
    if index >= len(arr):
        return False

    if targetSum == 0:
        memo[index][targetSum] = True
        return True

    if memo[index][targetSum]:
        return memo[index][targetSum]

    if arr[index] <= targetSum:
        output1 = subsetSumRecursionMemoHelper(
            arr, targetSum - arr[index], index + 1, memo)
        output2 = subsetSumRecursionMemoHelper(arr, targetSum, index + 1, memo)
    else:
        memo[index][targetSum] = subsetSumRecursionMemoHelper(
            arr, targetSum, index + 1, memo)
        return memo[index][targetSum]

    memo[index][targetSum] = output1 or output2
    return memo[index][targetSum]


arr: list[int] = [1, 2, 3, 7, 8, 10]
targetSum: int = 11
print(
    f"Target Sum with array {arr} with target {targetSum} is possible: {subsetSumRecursionMemo(arr[:], targetSum)}")

arr: list[int] = [3, 34, 4, 12, 5, 2]
targetSum: int = 9
print(
    f"Target Sum with array {arr} with target {targetSum} is possible: {subsetSumRecursionMemo(arr[:], targetSum)}")

arr: list[int] = [3, 34, 4, 12, 5, 2]
targetSum: int = 30
print(
    f"Target Sum with array {arr} with target {targetSum} is possible: {subsetSumRecursionMemo(arr[:], targetSum)}")


# Bottom UP Approach
def subsetSumRecursionTopDown(arr: list[int], targetSum: int) -> bool:
    """
    Calculates whether it is possible to obtain a sum of `targetSum` from a subset of the given array `arr` using top-down dynamic programming.

    Parameters:
        arr (list[int]): The input array of integers.
        targetSum (int): The target sum to be checked.

    Returns:
        bool: True if it is possible to obtain a sum of `targetSum` from a subset of `arr`, False otherwise.
    """
    dp: list[list[bool]] = [[False for _ in range(
        targetSum + 1)] for _ in range(len(arr) + 1)]
    for i in range(len(arr) + 1):
        for j in range(targetSum + 1):
            if j == 0:
                dp[i][0] = True
            else:
                dp[i][j] = False

    for i in range(1, len(arr) + 1):
        for j in range(1, targetSum + 1):
            if arr[i - 1] <= targetSum:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[len(arr)][targetSum]


arr: list[int] = [1, 2, 3, 7, 8, 10]
targetSum: int = 11
print(
    f"Target Sum with array {arr} with target {targetSum} is possible: {subsetSumRecursionTopDown(arr[:], targetSum)}")

arr: list[int] = [3, 34, 4, 12, 5, 2]
targetSum: int = 9
print(
    f"Target Sum with array {arr} with target {targetSum} is possible: {subsetSumRecursionTopDown(arr[:], targetSum)}")

arr: list[int] = [3, 34, 4, 12, 5, 2]
targetSum: int = 30
print(
    f"Target Sum with array {arr} with target {targetSum} is possible: {subsetSumRecursionTopDown(arr[:], targetSum)}")
