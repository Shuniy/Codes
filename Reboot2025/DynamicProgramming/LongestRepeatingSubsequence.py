def LongestRepeatingSubsequence(s):
    """
    Calculates the length of the longest repeating subsequence in a given string.

    Parameters:
        s (str): The input string.

    Returns:
        int: The length of the longest repeating subsequence.

    This function uses dynamic programming to calculate the length of the longest repeating subsequence in a given string. It creates a 2D array `dp` to store the lengths of the longest common subsequences between different substrings of the input string. The outer loop iterates over the characters of the string, and the inner loop iterates over the characters of the string. If the current characters are the same and they are not the same substring, the length of the longest common subsequence is incremented by 1. Otherwise, the length of the longest common subsequence is the maximum of the lengths of the longest common subsequences without the current characters. Finally, the function returns the length of the longest common subsequence for the entire string.
    """
    dp = [[0 for _ in range(len(s) + 1)] for _ in range(len(s) + 1)]

    for i in range(1, len(dp)):
        for j in range(1, len(dp)):
            if s[i - 1] == s[j - 1] and i != j:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]


X = "abcdeabd"
print("Length of longest repeating subsequence is: ",
      LongestRepeatingSubsequence(X))
