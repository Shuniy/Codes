def SequencePatternMatching(a: str, b: str) -> bool:
    """
    Check if a given string `a` is a subsequence of another string `b`.

    Args:
        a (str): The string to check if it is a subsequence of `b`.
        b (str): The string to check if it contains `a` as a subsequence.

    Returns:
        bool: True if `a` is a subsequence of `b`, False otherwise.

    This function uses dynamic programming to solve the problem. It creates a 2D array `dp` to store the length of the longest common subsequence between `a` and `b`. The outer loop iterates over the characters of `a` and the inner loop iterates over the characters of `b`. If the current characters of `a` and `b` match, the length of the LCS is incremented by 1. Otherwise, the length of the LCS is the maximum of the lengths of the LCS without the current characters of `a` and `b`. Finally, the function checks if the length of `a` is equal to the length of the LCS, indicating that `a` is a subsequence of `b`.
    """
    dp = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return len(a) == dp[-1][-1]


X = "axy"
Y = "adxcpy"
print("is X present in Y: ", SequencePatternMatching(X, Y))

X = "axy"
Y = "adcpy"
print("is X present in Y: ", SequencePatternMatching(X, Y))
