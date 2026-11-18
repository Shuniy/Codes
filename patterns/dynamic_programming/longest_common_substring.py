from re import A


def LongestCommonSubstringRecursive(x: str, y: str) -> int:
    """
    Finds the length of the longest common substring between two given strings using a recursive approach.

    Args:
        x (str): The first string.
        y (str): The second string.

    Returns:
        int: The length of the longest common substring between the two strings.

    """
    return LongestCommonSubstringRecursiveHelper(x, y, len(x), len(y), 0)


def LongestCommonSubstringRecursiveHelper(x: str, y: str, m: int, n: int, maxLength: int) -> int:
    """
    Finds the length of the longest common substring between two given strings using a recursive approach.

    Args:
        x (str): The first string.
        y (str): The second string.
        m (int): The length of the first string.
        n (int): The length of the second string.
        maxLength (int): The maximum length of the common substring found so far.

    Returns:
        int: The length of the longest common substring between the two strings.

    """
    if m <= 0 or n <= 0:
        return maxLength

    if x[m - 1] == y[n - 1]:
        maxLength = LongestCommonSubstringRecursiveHelper(
            x, y, m - 1, n - 1, maxLength + 1)
    else:
        maxLength = max(maxLength, max(LongestCommonSubstringRecursiveHelper(
            x, y, m, n - 1, 0), LongestCommonSubstringRecursiveHelper(x, y, m - 1, n, 0)))

    return maxLength


x: str = "abcdgh"
y: str = "abedfhr"
print(
    f"Length of Longest Common Subsequence in string {x} and {y} is: {LongestCommonSubstringRecursive(x, y)}")


def LongestCommonSubstringMemo(x: str, y: str) -> int:
    """
    Finds the length of the longest common substring between two given strings using memoization.

    Args:
        x (str): The first string.
        y (str): The second string.

    Returns:
        int: The length of the longest common substring between the two strings.

    """
    memo: list[list[int]] = [
        [-1 for _ in range(len(y) + 1)] for _ in range(len(x) + 1)]
    return LongestCommonSubstringMemoHelper(x, y, len(x), len(y), memo, 0)


def LongestCommonSubstringMemoHelper(x: str, y: str, m: int, n: int, memo: list[list[int]], maxLength: int) -> int:
    """
    Calculates the length of the longest common substring between two strings using memoization.

    Args:
        x (str): The first string.
        y (str): The second string.
        m (int): The length of the first string.
        n (int): The length of the second string.
        memo (list[list[int]]): The memoization table.
        maxLength (int): The maximum length of the common substring found so far.

    Returns:
        int: The length of the longest common substring between the two strings.
    """
    if m <= 0 or n <= 0:
        return maxLength

    if memo[m][n] != -1:
        return memo[m][n]

    if x[m - 1] == y[n - 1]:
        memo[m][n] = LongestCommonSubstringMemoHelper(
            x, y, m - 1, n - 1, memo, maxLength + 1)
    else:
        memo[m][n] = max(maxLength, max(LongestCommonSubstringMemoHelper(x, y, m, n - 1, memo, maxLength),
                         LongestCommonSubstringMemoHelper(x, y, m - 1, n, memo, maxLength)))
    return memo[m][n]


x: str = "abcdgh"
y: str = "abedfhr"
print(
    f"Length of Longest Common Subsequence in string {x} and {y} is: {LongestCommonSubstringMemo(x, y)}")


def LongestCommonSubstringDP(x: str, y: str) -> int:
    """
    Finds the length of the longest common substring between two given strings using dynamic programming.

    Args:
        x (str): The first string.
        y (str): The second string.

    Returns:
        int: The length of the longest common substring between the two strings.

    """
    m: int = len(x)
    n: int = len(y)
    if m <= 0 or n <= 0:
        return 0

    dp: list[list[int]] = [
        [0 for _ in range(len(y) + 1)] for _ in range(len(x) + 1)]
    result: int = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                result = max(result, dp[i][j])
            else:
                dp[i][j] = 0

    print(dp)
    i = m
    j = n
    string = ""
    globalResult = ""
    while i > 0 and j > 0:
        print((i, j))
        print(x[i - 1], y[j - 1])
        if x[i - 1] == y[j - 1]:
            string += x[i - 1]
            globalResult = max(string, globalResult, key=len)
            i -= 1
            j -= 1
        else:
            if dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1
            string = ""

    print(globalResult)

    return result


x: str = "abcdgh"
y: str = "abedfhr"
print(
    f"Length of Longest Common Subsequence in string {x} and {y} is: {LongestCommonSubstringDP(x, y)}")


x: str = "babad"
y: str = "dabab"
print(
    f"Length of Longest Common Subsequence in string {x} and {y} is: {LongestCommonSubstringDP(x, y)}")

x: str = "ca"
y: str = "ac"
print(
    f"Length of Longest Common Subsequence in string {x} and {y} is: {LongestCommonSubstringDP(x, y)}")
