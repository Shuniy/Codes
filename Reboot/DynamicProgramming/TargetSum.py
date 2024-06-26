def targetSumRecursion(arr: list[int], target: int) -> int:
    """
    Recursively calculates the number of target sums in the given array that sum up to the target value.

    Args:
        arr (list[int]): The input array of integers.
        target (int): The target sum to be achieved.

    Returns:
        int: The number of target sums in the array that sum up to the target value.
    """
    return targetSumRecursionHelper(arr, target, 0, 0)


def targetSumRecursionHelper(arr: list[int], target: int, index: int, count) -> int:
    """
    A recursive function that counts the number of ways to obtain a target sum from the given array.

    Parameters:
    - arr (list[int]): The input array of integers.
    - target (int): The target sum to achieve.
    - index (int): The current index in the array.
    - count: The current count of ways to reach the target sum.

    Returns:
    - int: The total count of ways to obtain the target sum.
    """
    if index >= len(arr):
        if target == 0:
            count += 1
        return count

    count = targetSumRecursionHelper(
        arr, target - arr[index], index + 1, count)
    count = targetSumRecursionHelper(
        arr, target + arr[index], index + 1, count)
    return count


arr: list[int] = [1, 1, 1, 1, 1]
target: int = 3
print(
    f"target sums of {target} in array: {arr} are: {targetSumRecursion(arr, target)}")

arr: list[int] = [1]
target: int = 1
print(
    f"target sums of {target} in array: {arr} are: {targetSumRecursion(arr, target)}")

# Problem is same as the CountSubsetsWithGivenDifference:-
# Suppose, if we can make a subset with all plus signs + subset with all minus sign
# taking minus sign will give us subset1(all plus) + (-)(subset2)(all minus taken common)
# and this sum or difference is what we want in target, basically we have to find places,
# where targetSum of (targetSum - sum(arr)) / 2, making it a count subset sum problem


def targetSumDP(arr: list[int], target: int) -> int:
    """
    Calculates the number of target sums in the given array that sum up to the target value using dynamic programming.

    Parameters:
        arr (list[int]): The input array of integers.
        target (int): The target sum to be achieved.

    Returns:
        int: The number of target sums in the array that sum up to the target value.
    """
    targetSumToFind: int = (target + sum(arr)) // 2
    dp: list[list[int]] = [
        [0 for _ in range(targetSumToFind + 1)] for _ in range(len(arr) + 1)]
    dp[0][0] = 1
    for i in range(1, len(arr) + 1):
        for j in range(targetSumToFind + 1):
            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - arr[i - 1]] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[len(arr)][targetSumToFind]


def targetSumDPSpace(arr: list[int], target: int) -> int:
    targetSumToFind: int = (target + sum(arr)) // 2
    dp: list[int] = [0 for _ in range(targetSumToFind + 1)]
    dp[0] = 1
    for i in range(1, len(arr) + 1):
        ans = dp.copy()
        for j in range(targetSumToFind + 1):
            if arr[i - 1] <= j:
                ans[j] = dp[j - arr[i - 1]] + dp[j]
            else:
                ans[j] = dp[j]
        dp = ans.copy()
    return dp[targetSumToFind]


arr: list[int] = [1, 1, 1, 1, 1]
target: int = 3
print(
    f"target sums of {target} in array: {arr} are: {targetSumDP(arr, target)}")

arr: list[int] = [1]
target: int = 1
print(
    f"target sums of {target} in array: {arr} are: {targetSumDP(arr, target)}")

arr: list[int] = [1, 1, 1, 1, 1]
target: int = 3
print(
    f"target sums of {target} in array: {arr} are: {targetSumDPSpace(arr, target)}")

arr: list[int] = [1]
target: int = 1
print(
    f"target sums of {target} in array: {arr} are: {targetSumDPSpace(arr, target)}")
