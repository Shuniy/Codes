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


def PrintLCS(x: str, y: str) -> str:
    """
    Given two strings `x` and `y`, this function returns the Longest Common Subsequence (LCS) between them.

    Parameters:
        x (str): The first string.
        y (str): The second string.

    Returns:
        str: The LCS of `x` and `y`.
    """
    m: int = len(x)
    n: int = len(y)
    if m <= 0 or n <= 0:
        return ""

    dp: list[list[int]] = [
        [0 for _ in range(len(y) + 1)] for _ in range(len(x) + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i: int = m
    j: int = n
    result: str = ""
    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            result = x[i - 1] + result
            i -= 1
            j -= 1
        else:
            if dp[i - 1][j] >= dp[i][j - 1]:
                i -= 1
            else:
                j -= 1
    return result


X = "bbbab"
print("Longest Palindromic Subsequence is of size: ",
      LongestPalindromicSubsequence(X))
print(PrintLCS(X, X[::-1]))

X = "agbcba"
print("Longest Palindromic Subsequence is of size: ",
      LongestPalindromicSubsequence(X))
print(PrintLCS(X, X[::-1]))

X = "geeksforgeeks"
print("Longest Palindromic Subsequence is of size: ",
      LongestPalindromicSubsequence(X))
print(PrintLCS(X, X[::-1]))
