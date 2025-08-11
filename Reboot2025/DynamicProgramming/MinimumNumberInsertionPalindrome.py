def MinimumNumberInsertionPalindrome(s):
    """
    Calculates the minimum number of insertions needed to make a string a palindrome.

    Parameters:
    - s (str): The input string.

    Returns:
    - int: The minimum number of insertions needed to make the string a palindrome.
    """
    if s == s[::-1]:
        return 0
    r = s[::-1]
    dp = [[0 for _ in range(len(s) + 1)] for _ in range(len(s) + 1)]
    for i in range(1, len(dp)):
        for j in range(len(dp)):
            if s[i - 1] == r[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return len(s) - dp[-1][-1]


X = "aebebda"
print("minimum number of insertion needed to make string palindrome: ",
      MinimumNumberInsertionPalindrome(X))
