def LCSRecursive(x: str, y: str) -> int:
    return LCSRecursiveHelper(x, y, len(x), len(y))

def LCSRecursiveHelper(x: str, y: str, m: int, n: int) -> int:
    if m <= 0 or n <= 0:
        return 0
    
    if x[m - 1] == y[n - 1]:
        return 1 + LCSRecursiveHelper(x, y, m - 1, n - 1)
    else:
        return max(LCSRecursiveHelper(x, y, m, n - 1), LCSRecursiveHelper(x, y, m - 1, n))

x: str = "abcdgh"
y: str = "abedfhr"
print(f"Length of Longest Common Subsequence in string {x} and {y} is: {LCSRecursive(x, y)}")


def LCSMemo(x: str, y: str) -> int:
    memo: list[list[int]] = [[-1 for _ in range(len(y) + 1)] for _ in range(len(x) + 1)]
    return LCSMemoHelper(x, y, len(x), len(y), memo)


def LCSMemoHelper(x: str, y: str, m: int, n: int, memo: list[list[int]]) -> int:
    if m <= 0 or n <= 0:
        return 0

    if memo[m][n] != -1:
        return memo[m][n]

    if x[m - 1] == y[n - 1]:
        memo[m][n] = 1 + LCSMemoHelper(x, y, m - 1, n - 1, memo)
    else:
        memo[m][n] = max(LCSMemoHelper(x, y, m, n - 1, memo),
                         LCSMemoHelper(x, y, m - 1, n, memo))
    return memo[m][n]

x: str = "abcdgh"
y: str = "abedfhr"
print(
    f"Length of Longest Common Subsequence in string {x} and {y} is: {LCSMemo(x, y)}")


def LCSDP(x: str, y: str) -> int:
    m: int = len(x)
    n: int = len(y)
    if m <= 0 or n <= 0:
        return 0

    dp: list[list[int]] = [
        [0 for _ in range(len(y) + 1)] for _ in range(len(x) + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

def PrintLCS(x: str, y: str) -> str:
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
    while i != 0 or j != 0:
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

x: str = "abcdgh"
y: str = "abedfhr"
print(
    f"Length of Longest Common Subsequence in string {x} and {y} is: {LCSDP(x, y)}")

print(f"Longest Common Subsequence is: {PrintLCS(x, y)}")