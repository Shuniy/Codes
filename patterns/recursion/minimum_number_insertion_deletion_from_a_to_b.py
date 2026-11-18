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


def MinimumNumberInsertionDeletion(x, y):
    """
    A function to find the minimum number of insertions and deletions required to convert one string to another.

    Args:
        x: The first input string.
        y: The second input string.

    Returns:
        The minimum number of insertions and deletions required to convert one string to another.
    """
    return (len(x) - LongestCommonSubsequence(x, y)) + (len(y) - LongestCommonSubsequence(y, x))


x = "geeksforgeeks"
y = "geeks"
print(
    f"minimum insertion and deletion from a to b is: {LongestCommonSubsequence(x, y)}")
