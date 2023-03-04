def MinimumSubsetSumDifference(arr: list[int]) -> int:
    totalSum: int = sum(arr)
    return MinimumSubsetSumDifferenceHelper(arr, 0, 0, totalSum, float("inf"))


def MinimumSubsetSumDifferenceHelper(arr: list[int], index: int, subset1Sum: int, subset2Sum: int, minSum: int) -> int:
    if index >= len(arr):
        minSum = min(abs(subset1Sum - subset2Sum), minSum)
        return minSum

    minSum = min(abs(subset1Sum - subset2Sum), minSum)

    output1 = MinimumSubsetSumDifferenceHelper(
        arr, index + 1, subset1Sum + arr[index], subset2Sum - arr[index], minSum)
    output2 = MinimumSubsetSumDifferenceHelper(
        arr, index + 1, subset1Sum, subset2Sum, minSum)
    minSum = min(output1, output2)
    return minSum


arr: list[int] = [1, 6, 11, 5]
print(
    f"Minimun Subset Difference for array: {arr} is: {MinimumSubsetSumDifference(arr)}")
arr: list[int] = [3, 1, 4, 2, 2, 1]
print(
    f"Minimun Subset Difference for array: {arr} is: {MinimumSubsetSumDifference(arr)}")
arr: list[int] = [3, 1, 4, 2, 2, -1]
print(
    f"Minimun Subset Difference for array: {arr} is: {MinimumSubsetSumDifference(arr)}")
arr: list[int] = [3, 1, 4, 2, 2, 15]
print(
    f"Minimun Subset Difference for array: {arr} is: {MinimumSubsetSumDifference(arr)}")


def MinimumSubsetSumDifferenceDP(arr: list[int]):
    totalSum: int = sum(arr)
    dp: list[list[int]] = [[False for _ in range(
        totalSum + 1)] for _ in range(len(arr) + 1)]

    dp[0][0] = True
    for j in range(totalSum + 1):
        dp[0][j] = False

    for i in range(1, len(arr) + 1):
        for j in range(totalSum + 1):
            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    # Now, dp[i][j] will contains the True or false whether a subset can have that sum possible or not
    # dp[i][j] at 5 of value true will tell that arr[i - 1] position array can give sum of 5
    minSum = float("inf")
    for j in range((totalSum // 2) + 1, -1, -1):
        if arr[len(arr)][j] == True:
            subset1Sum = j
            subset2Sum = totalSum - subset1Sum
            subsetDifference = abs(subset1Sum - subset2Sum)
            minSum = min(subsetDifference, minSum)
            return minSum
    minSum = min(minSum, 0)
    return minSum


arr: list[int] = [1, 6, 11, 5]
print(
    f"Minimun Subset Difference for array: {arr} is: {MinimumSubsetSumDifference(arr)}")
arr: list[int] = [3, 1, 4, 2, 2, 1]
print(
    f"Minimun Subset Difference for array: {arr} is: {MinimumSubsetSumDifference(arr)}")
arr: list[int] = [3, 1, 4, 2, 2, -1]
print(
    f"Minimun Subset Difference for array: {arr} is: {MinimumSubsetSumDifference(arr)}")
arr: list[int] = [3, 1, 4, 2, 2, 15]
print(
    f"Minimun Subset Difference for array: {arr} is: {MinimumSubsetSumDifference(arr)}")
