def CountSubsetsWithGivenSumRecursive(arr: list[int], targetSum: int) -> int:
    """
    Recursive function to count the number of subsets in the given array that sum up to the target sum.

    Args:
        arr (list[int]): The input array of integers.
        targetSum (int): The target sum to be achieved.

    Returns:
        int: The total number of subsets that sum up to the target sum.
    """
    return CountSubsetsWithGivenSumRecursiveHelper(arr, targetSum, 0, 0)


def CountSubsetsWithGivenSumRecursiveHelper(arr: list[int], targetSum: int, index: int, count: int) -> int:
    """
    Recursively counts the number of subsets in a given array that have a sum equal to the target sum.

    Args:
        arr (list[int]): The input array of integers.
        targetSum (int): The target sum for the subsets.
        index (int): The current index in the array.
        count (int): The current count of subsets.

    Returns:
        int: The total count of subsets with a sum equal to the target sum.
    """
    if index >= len(arr):
        if targetSum == 0:
            count += 1
        return count

    if targetSum == 0:
        count += 1
        return count

    if arr[index] <= targetSum:
        count = CountSubsetsWithGivenSumRecursiveHelper(
            arr, targetSum - arr[index], index + 1, count)
        count = CountSubsetsWithGivenSumRecursiveHelper(
            arr, targetSum, index + 1, count)
    else:
        count = CountSubsetsWithGivenSumRecursiveHelper(
            arr, targetSum, index + 1, count)
    return count


arr: list[int] = [3, 3, 3, 3]
targetSum: int = 6
print(
    f"Number of subsets with {targetSum} in arr {arr} are: {CountSubsetsWithGivenSumRecursive(arr, targetSum)}")


arr: list[int] = [2, 3, 5, 6, 8, 10]
targetSum: int = 10
print(
    f"Number of subsets with {targetSum} in arr {arr} are: {CountSubsetsWithGivenSumRecursive(arr, targetSum)}")

arr: list[int] = [1, 2, 3, 4, 5]
targetSum: int = 7
print(
    f"Number of subsets with {targetSum} in arr {arr} are: {CountSubsetsWithGivenSumRecursive(arr, targetSum)}")

arr: list[int] = [3, 2, 3]
targetSum: int = 5
print(
    f"Number of subsets with {targetSum} in arr {arr} are: {CountSubsetsWithGivenSumRecursive(arr, targetSum)}")

# Memoization


def CountSubsetsWithGivenSumTopDown(arr: list[int], targetSum: int) -> int:
    """
    CountSubsetsWithGivenSumTopDown calculates the total number of subsets in the given array 'arr' that sum up to the target sum 'targetSum' using a top-down dynamic programming approach.

    Args:
        arr (list[int]): The input array of integers.
        targetSum (int): The target sum to be achieved.

    Returns:
        int: The total number of subsets that sum up to the target sum.
    """
    dp: list[list[int]] = [
        [0 for _ in range(targetSum + 1)] for _ in range(len(arr) + 1)]
    dp[0][0] = 1

    for i in range(1, len(arr) + 1):
        for j in range(0, targetSum + 1):
            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - arr[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[len(arr)][targetSum]


arr: list[int] = [3, 3, 3, 3]
targetSum: int = 6
print(
    f"Number of subsets with {targetSum} in arr {arr} are: {CountSubsetsWithGivenSumTopDown(arr, targetSum)}")

arr: list[int] = [2, 3, 5, 6, 8, 10]
targetSum: int = 10
print(
    f"Number of subsets with {targetSum} in arr {arr} are: {CountSubsetsWithGivenSumTopDown(arr, targetSum)}")

arr: list[int] = [1, 2, 3, 4, 5]
targetSum: int = 7
print(
    f"Number of subsets with {targetSum} in arr {arr} are: {CountSubsetsWithGivenSumTopDown(arr, targetSum)}")

arr: list[int] = [3, 2, 3]
targetSum: int = 5
print(
    f"Number of subsets with {targetSum} in arr {arr} are: {CountSubsetsWithGivenSumTopDown(arr, targetSum)}")
