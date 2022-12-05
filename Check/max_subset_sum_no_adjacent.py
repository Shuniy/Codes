# Time : O(n)
# Space : O(n)
def MaxSubsetNoAdjacent(arr):
    if not len(arr):
        return 
    elif len(arr) == 1:
        return arr[0]
    
    n = len(arr)
    dp = [0 for _ in range(n)]
    
    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])

    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + arr[i])

    return dp[-1]

# Time : O(n)
# Space : O(1)
def MaxSubsetNoAdjacent(arr):
    n = len(arr)

    first = arr[0]
    second = max(arr[0], arr[1])

    for i in range(2, n):
        max_sum = max(first, second + arr[i])

        first = second
        second = max_sum

    return second

    