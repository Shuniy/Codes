def MatrixChainMultiplication(arr: list[int]) -> int | float:
    """
    Calculates the minimum cost of matrix chain multiplication for a given list of matrices.

    Parameters:
        arr (list[int]): A list of integers representing the dimensions of the matrices.

    Returns:
        int | float: The minimum cost of matrix chain multiplication.

    """
    return MatrixChainMultiplicationHelper(arr, 1, len(arr) - 1, )


def MatrixChainMultiplicationHelper(arr: list[int], i: int, j: int) -> int | float:
    """
    Calculates the minimum cost of matrix chain multiplication for a given subarray of matrices.

    Parameters:
        arr (list[int]): A list of integers representing the dimensions of the matrices.
        i (int): The starting index of the subarray.
        j (int): The ending index of the subarray.

    Returns:
        int | float: The minimum cost of matrix chain multiplication for the subarray.
    """
    if i >= j:
        return 0

    min_cost = float('inf')
    for k in range(i, j):
        cost = arr[i - 1] * arr[k] * arr[j] + MatrixChainMultiplicationHelper(
            arr, i, k) + MatrixChainMultiplicationHelper(arr, k + 1, j)
        min_cost = min(min_cost, cost)
    return min_cost


X = [10, 30, 5, 60]
print("minimum cost of matrix chain multiplication is",
      MatrixChainMultiplication(X))


X = [40, 20, 30, 10, 30]
print("minimum cost of matrix chain multiplication is",
      MatrixChainMultiplication(X))

X = [1, 2, 3, 4, 3]
print("minimum cost of matrix chain multiplication is",
      MatrixChainMultiplication(X))

X = [10, 20, 30]
print("minimum cost of matrix chain multiplication is",
      MatrixChainMultiplication(X))
