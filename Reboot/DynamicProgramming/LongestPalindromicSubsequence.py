def LongestPalindromicSubsequence(x: str) -> int:
    """
    A function to find the length of the longest palindromic subsequence in a string.

    Args:
        x (str): The input string.

    Returns:
        int: The length of the longest palindromic subsequence in the string.
    """
    y = x[::-1]
    n = len(x)
    m = len(y)

    # Initialize a 2D array to store the length of the LCS
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Fill in the dp array using dynamic programming
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # The final value in dp will be the length of the LCS
    return dp[-1][-1]


X = "bbbab"
print("Longest Palindromic Subsequence is of size: ",
      LongestPalindromicSubsequence(X))

X = "agbcba"
print("Longest Palindromic Subsequence is of size: ",
      LongestPalindromicSubsequence(X))

X = "geeksforgeeks"
print("Longest Palindromic Subsequence is of size: ",
      LongestPalindromicSubsequence(X))
