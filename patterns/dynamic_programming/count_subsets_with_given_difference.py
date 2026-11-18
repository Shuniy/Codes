def CountSubsetsWithGivenDifferenceRecursion(arr: list[int], difference: int) -> int:
    """
    Calculate the number of subsets in the given array that have a difference equal to the given difference.

    Parameters:
    - arr (list[int]): The input array of integers.
    - difference (int): The difference between the sums of two subsets.

    Returns:
    - int: The total number of subsets that have a difference equal to the given difference.
    """
    return CountSubsetsWithGivenDifferenceRecursionHelper(arr, difference, 0, sum(arr), 0, 0)


def CountSubsetsWithGivenDifferenceRecursionHelper(arr: list[int], difference: int, subset1Sum: int, subset2Sum: int, index: int, count: int) -> int:
    """
    Recursively counts the number of subsets in the given array that have a difference equal to the given difference.

    Parameters:
    - arr (list[int]): The input array of integers.
    - difference (int): The difference between the sums of two subsets.
    - subset1Sum (int): The sum of elements in the first subset.
    - subset2Sum (int): The sum of elements in the second subset.
    - index (int): The current index in the array.
    - count (int): The current count of subsets.

    Returns:
    - int: The total count of subsets with a difference equal to the given difference.
    """
    if index >= len(arr):
        if abs(subset1Sum - subset2Sum) == difference:
            count += 1
        return count

    count = CountSubsetsWithGivenDifferenceRecursionHelper(
        arr, difference, subset1Sum + arr[index], subset2Sum - arr[index], index + 1, count)
    count = CountSubsetsWithGivenDifferenceRecursionHelper(
        arr, difference, subset1Sum, subset2Sum, index + 1, count)
    return count


arr: list[int] = [1, 1, 2, 3]
difference: int = 1
print(f"Count of arr: {arr} Subset Difference with given difference: {difference} is: {CountSubsetsWithGivenDifferenceRecursion(arr, difference)}")

arr: list[int] = [5, 2, 6, 4]
difference: int = 3
print(f"Count of arr: {arr} Subset Difference with given difference: {difference} is: {CountSubsetsWithGivenDifferenceRecursion(arr, difference)}")

arr: list[int] = [1, 1, 1, 1]
difference: int = 0
print(f"Count of arr: {arr} Subset Difference with given difference: {difference} is: {CountSubsetsWithGivenDifferenceRecursion(arr, difference)}")

arr: list[int] = [4, 6, 3]
difference: int = 1
print(f"Count of arr: {arr} Subset Difference with given difference: {difference} is: {CountSubsetsWithGivenDifferenceRecursion(arr, difference)}")

arr: list[int] = [3, 1, 1, 2, 1]
difference: int = 0
print(f"Count of arr: {arr} Subset Difference with given difference: {difference} is: {CountSubsetsWithGivenDifferenceRecursion(arr, difference)}")

arr: list[int] = [3, 2, 2, 5, 1]
difference: int = 1
print(f"Count of arr: {arr} Subset Difference with given difference: {difference} is: {CountSubsetsWithGivenDifferenceRecursion(arr, difference)}")


def CountSubsetsWithGivenDifferenceRecursion(arr: list[int], difference: int) -> int:
    """
    A recursive function to calculate the number of subsets in the given array that have a difference equal to the given difference.

    Parameters:
    - arr (list[int]): The input array of integers.
    - difference (int): The difference between the sums of two subsets.

    Returns:
    - int: The total number of subsets that have a difference equal to the given difference.
    """
    # Since, we don't need to maintain the sum of second subset, all we can do is,
    # just find the subset with given sum, because
    # s1-s2 = difference, s2 = totalSum - s1; :: s1 = (difference + totalSum) / 2
    subsetSumToFind: int = (difference + sum(arr)) / 2
    return CountSubsetsWithGivenDifferenceRecursionHelper(arr, subsetSumToFind, 0, 0)


def CountSubsetsWithGivenDifferenceRecursionHelper(arr: list[int], targetSum: int, index: int, count: int) -> int:
    """
    Recursively counts the number of subsets in a given array that have a sum equal to the target sum.

    Parameters:
    - arr (list[int]): The input array of integers.
    - targetSum (int): The target sum for the subsets.
    - index (int): The current index in the array.
    - count (int): The current count of subsets.

    Returns:
    - int: The total count of subsets with a sum equal to the target sum.
    """
    if index >= len(arr):
        if targetSum == 0:
            count += 1
        return count
    if targetSum == 0:
        count += 1
        return count

    if arr[index] <= targetSum:
        count = CountSubsetsWithGivenDifferenceRecursionHelper(
            arr, targetSum - arr[index], index + 1, count)
    count = CountSubsetsWithGivenDifferenceRecursionHelper(
        arr, targetSum, index + 1, count)
    return count


arr: list[int] = [1, 1, 2, 3]
difference: int = 1
print(f"Count of arr: {arr} Subset Difference with given difference: {difference} is: {CountSubsetsWithGivenDifferenceRecursion(arr, difference)}")

arr: list[int] = [5, 2, 6, 4]
difference: int = 3
print(f"Count of arr: {arr} Subset Difference with given difference: {difference} is: {CountSubsetsWithGivenDifferenceRecursion(arr, difference)}")

arr: list[int] = [1, 1, 1, 1]
difference: int = 0
print(f"Count of arr: {arr} Subset Difference with given difference: {difference} is: {CountSubsetsWithGivenDifferenceRecursion(arr, difference)}")

arr: list[int] = [4, 6, 3]
difference: int = 1
print(f"Count of arr: {arr} Subset Difference with given difference: {difference} is: {CountSubsetsWithGivenDifferenceRecursion(arr, difference)}")

arr: list[int] = [3, 1, 1, 2, 1]
difference: int = 0
print(f"Count of arr: {arr} Subset Difference with given difference: {difference} is: {CountSubsetsWithGivenDifferenceRecursion(arr, difference)}")

arr: list[int] = [3, 2, 2, 5, 1]
difference: int = 1
print(f"Count of arr: {arr} Subset Difference with given difference: {difference} is: {CountSubsetsWithGivenDifferenceRecursion(arr, difference)}")


def CountSubsetsWithGivenDifferenceDP(arr: list[int], difference: int) -> int:
    """
    A dynamic programming function to calculate the number of subsets in the given array that have a difference equal to the given difference.

    Parameters:
    - arr (list[int]): The input array of integers.
    - difference (int): The difference between the sums of two subsets.

    Returns:
    - int: The total count of subsets with a difference equal to the given difference.
    """
    targetSumToFind: int = (difference + sum(arr)) // 2
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


arr: list[int] = [1, 1, 2, 3]
difference: int = 1
print(f"Count of arr: {arr} Subset Difference with given difference: {difference} is: {CountSubsetsWithGivenDifferenceDP(arr, difference)}")

arr: list[int] = [5, 2, 6, 4]
difference: int = 3
print(f"Count of arr: {arr} Subset Difference with given difference: {difference} is: {CountSubsetsWithGivenDifferenceDP(arr, difference)}")

arr: list[int] = [1, 1, 1, 1]
difference: int = 0
print(f"Count of arr: {arr} Subset Difference with given difference: {difference} is: {CountSubsetsWithGivenDifferenceDP(arr, difference)}")

arr: list[int] = [4, 6, 3]
difference: int = 1
print(f"Count of arr: {arr} Subset Difference with given difference: {difference} is: {CountSubsetsWithGivenDifferenceDP(arr, difference)}")

arr: list[int] = [3, 1, 1, 2, 1]
difference: int = 0
print(f"Count of arr: {arr} Subset Difference with given difference: {difference} is: {CountSubsetsWithGivenDifferenceDP(arr, difference)}")

arr: list[int] = [3, 2, 2, 5, 1]
difference: int = 1
print(f"Count of arr: {arr} Subset Difference with given difference: {difference} is: {CountSubsetsWithGivenDifferenceDP(arr, difference)}")
