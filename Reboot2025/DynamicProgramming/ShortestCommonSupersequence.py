def LongestCommonSubsequence(x, y):
    """
    A function to find the length of the longest common subsequence between two strings.

    Args:
        x: The first input string.
        y: The second input string.

    Returns:
        The length of the longest common subsequence between the two strings.
    """
    return (len(x) + len(y) - LongestCommonSubsequenceHelper(x, y, len(x), len(y)))


def LongestCommonSubsequenceHelper(x, y, m, n):
    """
    Calculates the length of the longest common subsequence between two strings.

    Args:
        x (str): The first input string.
        y (str): The second input string.
        m (int): The length of the first string.
        n (int): The length of the second string.

    Returns:
        int: The length of the longest common subsequence between the two strings.

    This function uses dynamic programming to calculate the length of the longest common subsequence between two strings.
    It recursively compares the last characters of the strings and either adds 1 to the result if they are equal,
    or chooses the maximum of the two recursive calls if they are not equal. The base case is when either string
    is empty, in which case the length of the common subsequence is 0.
    """
    if m <= 0 or n <= 0:
        return 0

    if x[m - 1] == y[n - 1]:
        return 1 + LongestCommonSubsequenceHelper(x, y, m - 1, n - 1)
    else:
        return max(LongestCommonSubsequenceHelper(x, y, m - 1, n), LongestCommonSubsequenceHelper(x, y, m, n - 1))


def ShortestCommonSupersequence(x, y):
    """
    A function to find the length of the shortest common supersequence of two strings.
    It uses dynamic programming to populate a 2D array and iterates through the strings to calculate the length.
    """
    dp = [[0 for _ in range(len(y) + 1)] for _ in range(len(x) + 1)]
    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return (len(x) + len(y) - dp[len(x)][len(y)])


def printShortesrCommonSupersequence(x, y):
    """
    Prints the shortest common supersequence of two strings.
    """
    dp = [[0 for _ in range(len(y) + 1)] for _ in range(len(x) + 1)]
    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i = len(x)
    j = len(y)
    result = ""
    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            result += x[i - 1]
            i -= 1
            j -= 1
        elif dp[i - 1][j] < dp[i][j - 1]:
            result += y[j - 1]
            j -= 1
        else:
            result += x[i - 1]
            i -= 1
    return result[::-1]


x = "aggtab"
y = "gxtxayb"
print(
    f"Length of longest common subsequence is: {LongestCommonSubsequence(x, y)}")
print(
    f"Length of Shortest common supersequence is: {ShortestCommonSupersequence(x, y)}")
print(printShortesrCommonSupersequence(x, y))

x = "acbcf"
y = "abcdaf"
print(
    f"Length of longest common subsequence is: {LongestCommonSubsequence(x, y)}")
print(
    f"Length of Shortest common supersequence is: {ShortestCommonSupersequence(x, y)}")
print(printShortesrCommonSupersequence(x, y))
