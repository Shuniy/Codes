def EqualSumPartitionRecursive(arr: list[int]) -> bool:
    arrSum: int = sum(arr)
    if arrSum % 2 == 0:
        return EqualSumPartitionRecursiveHelper(arr, 0, arrSum // 2)
    else:
        return False

def EqualSumPartitionRecursiveHelper(arr, index, targetSum) -> bool:
    if index >= len(arr):
        if targetSum == 0:
            return True
        return False
    
    if targetSum == 0:
        return True
    
    if arr[index] <= targetSum:
        output1 = EqualSumPartitionRecursiveHelper(arr, index + 1, targetSum - arr[index])
        output2 = EqualSumPartitionRecursiveHelper(arr, index + 1, targetSum)
    else:
        return EqualSumPartitionRecursiveHelper(arr, index + 1, targetSum)
    
    return output1 or output2

arr: list[int] = [1, 5, 11, 5]
print(f"The array {arr} can be partitioned equally: {EqualSumPartitionRecursive(arr)}")

arr: list[int] = [1, 5, 3]
print(
    f"The array {arr} can be partitioned equally: {EqualSumPartitionRecursive(arr)}")

# Memoization


def EqualSumPartitionMemo(arr: list[int]) -> bool:
    arrSum: int = sum(arr)
    if arrSum % 2 == 0:
        memo: list[list[False]] = [[False for _ in range((arrSum // 2) + 1)] for _ in range(len(arr) + 1)]
        return EqualSumPartitionMemoHelper(arr, 0, arrSum // 2, memo)
    else:
        return False


def EqualSumPartitionMemoHelper(arr, index, targetSum, memo) -> bool:
    if index >= len(arr):
        return False

    if targetSum == 0:
        memo[index][targetSum] = True
        return True
    
    if memo[index][targetSum]:
        return memo[index][targetSum]

    if arr[index] <= targetSum:
        output1 = EqualSumPartitionMemoHelper(
            arr, index + 1, targetSum - arr[index], memo)
        output2 = EqualSumPartitionMemoHelper(arr, index + 1, targetSum, memo)
    else:
        memo[index][targetSum] = EqualSumPartitionMemoHelper(arr, index + 1, targetSum, memo)
        return memo[index][targetSum]

    memo[index][targetSum] = output1 or output2
    return memo[index][targetSum]


arr: list[int] = [1, 5, 11, 5]
print(
    f"The array {arr} can be partitioned equally: {EqualSumPartitionMemo(arr)}")

arr: list[int] = [1, 5, 3]
print(
    f"The array {arr} can be partitioned equally: {EqualSumPartitionMemo(arr)}")

# Bottom UP Approach

def EqualSumPartitionTopDown(arr: list[int]) -> bool:
    arrSum: int = sum(arr)
    if arrSum % 2 == 0:
        dp: list[list[False]] = [[False for _ in range(
            (arrSum // 2) + 1)] for _ in range(len(arr) + 1)]
        for i in range(len(arr) + 1):
            dp[i][0] = True
            
        for i in range(1, len(arr) + 1):
            for j in range(1, (arrSum // 2) + 1):
                if arr[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[len(arr) - 1][arrSum // 2]
    else:
        return False
    
arr: list[int] = [1, 5, 11, 5]
print(
    f"The array {arr} can be partitioned equally: {EqualSumPartitionTopDown(arr)}")

arr: list[int] = [1, 5, 3]
print(
    f"The array {arr} can be partitioned equally: {EqualSumPartitionTopDown(arr)}")
