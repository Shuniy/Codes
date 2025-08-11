def MatrixChainMultiplication(p: list[int]) -> int:
    """
    A function to find the minimum number of multiplications required to 
    multiply all the matrixes in a given chain.

    Args:
        p (list[int]): A list of integers representing the dimensions of the 
        matrix chain.

    Returns:
        int: The minimum number of multiplications required to multiply all 
        the matrixes in the chain.
    """
    n = len(p) - 1
    dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
    return MatrixChainMultiplicationHelper(p, 0, n, dp)

def MatrixChainMultiplicationHelper(p: list[int], i: int, j: int, dp: list[list[int]]) -> int:
    """
    A helper function to find the minimum number of multiplications required to 
    multiply all the matrixes in a given chain.

    Args:
        p (list[int]): A list of integers representing the dimensions of the 
        matrix chain.
        i (int): The starting index of the chain.
        j (int): The ending index of the chain.
        dp (list[list[int]]): A 2D list of integers representing the 
        minimum number of multiplications required to multiply all the 
        matrixes in a given chain.

    Returns:
        int: The minimum number of multiplications required to multiply all 
        the matrixes in the chain.
    """
    # I Have only 2 elements in the chain, meaning only 1 matrix
    if i + 1 == j:
        return 0
    
    if dp[i][j] != -1:
        return dp[i][j]

    ans = float('inf')
    for k in range(i + 1, j):
        result = MatrixChainMultiplicationHelper(p, i, k, dp) + \
            MatrixChainMultiplicationHelper(p, k, j, dp) + \
                p[i] * p[k] * p[j]
        ans = min(ans, result)
    dp[i][j] = ans
    return ans


# test cases
print(MatrixChainMultiplication([1, 2, 3, 4, 3]))
print(MatrixChainMultiplication([10, 30, 5, 60]))
print(MatrixChainMultiplication([40, 20, 30, 10, 30]))
print(MatrixChainMultiplication([1, 2, 3, 4, 3]))
print(MatrixChainMultiplication([10, 20, 30]))