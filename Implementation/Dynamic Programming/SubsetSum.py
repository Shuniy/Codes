# Recursion
def subsetSumRecursion(arr: list[int], targetSum: int) -> bool:
    return subsetSumRecursionHelper(arr, targetSum, 0)

def subsetSumRecursionHelper(arr: list[int], targetSum: int, index: int) -> bool:
    if index >= len(arr):
        return False
        
    if targetSum == 0:
        return True
    
    if arr[index] <= targetSum:
        output1 = subsetSumRecursionHelper(arr, targetSum - arr[index], index + 1)
        output2 = subsetSumRecursionHelper(arr, targetSum, index + 1)
    else:
        return subsetSumRecursionHelper(arr, targetSum, index + 1)
    
    return output1 or output2

arr: list[int] = [1,2,3,7,8,10]
targetSum: int = 11
print(f"Target Sum with array {arr} with target {targetSum} is possible: {subsetSumRecursion(arr[:], targetSum)}")

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
    memo: list[list[bool]] = [[False for _ in range(targetSum + 1)] for _ in range(len(arr) + 1)]
    for i in range(len(arr) + 1):
        memo[i][0] = True
    return subsetSumRecursionMemoHelper(arr, targetSum, 0, memo)


def subsetSumRecursionMemoHelper(arr: list[int], targetSum: int, index: int, memo: list[list[bool]]) -> bool:
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
        memo[index][targetSum] = subsetSumRecursionMemoHelper(arr, targetSum, index + 1, memo)
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
    return dp[len(arr) - 1][targetSum]


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
