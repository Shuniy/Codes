def LongestCommonSubsequence(x, y):
    return LongestCommonSubsequenceHelper(x, y, len(x), len(y))


def LongestCommonSubsequenceHelper(x, y, m, n):
    if m <= 0 or n <= 0:
        return 0

    if x[m - 1] == y[n - 1]:
        return 1 + LongestCommonSubsequenceHelper(x, y, m - 1, n - 1)
    else:
        return max(LongestCommonSubsequenceHelper(x, y, m - 1, n), LongestCommonSubsequenceHelper(x, y, m, n - 1))


def ShortestCommonSupersequence(x, y):
    dp = [[0 for _ in range(len(y) + 1)] for _ in range(len(x) + 1)]
    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return (len(x) + len(y) - dp[len(x)][len(y)])


x = "aggtab"
y = "gxtxayb"
print(
    f"Length of longest common subsequence is: {LongestCommonSubsequence(x, y)}")
print(
    f"Length of Shortest common supersequence is: {ShortestCommonSupersequence(x, y)}")
