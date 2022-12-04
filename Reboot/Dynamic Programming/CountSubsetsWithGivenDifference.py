def CountSubsetsWithGivenDifferenceRecursion(arr: list[int], difference: int) -> int:
    return CountSubsetsWithGivenDifferenceRecursionHelper(arr, difference, 0, sum(arr), 0, 0)

def CountSubsetsWithGivenDifferenceRecursionHelper(arr: list[int], difference: int, subset1Sum: int, subset2Sum: int, index: int, count: int) -> int:
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
    # Since, we don't need to maintain the sum of second subset, all we can do is,
    # just find the subset with given sum, because
    # s1-s2 = difference, s2 = totalSum - s1; :: s1 = (difference + totalSum) / 2
    subsetSumToFind: int = (difference + sum(arr)) / 2
    return CountSubsetsWithGivenDifferenceRecursionHelper(arr, subsetSumToFind, 0, 0)

def CountSubsetsWithGivenDifferenceRecursionHelper(arr: list[int], targetSum: int, index: int, count: int) -> int:
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

arr: list[int] = [5,2,6,4]
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
    targetSumToFind: int = (difference + sum(arr)) // 2
    dp: list[list[int]] = [[0 for _ in range(targetSumToFind + 1)] for _ in range(len(arr) + 1)]
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
