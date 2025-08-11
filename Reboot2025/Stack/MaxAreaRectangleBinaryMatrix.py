def NSR(arr):
    """
    Given an array `arr`, this function calculates the Next Smaller to Right (NSR) for each element in the array. It returns a list containing the indices of the next smaller element to the right for each element in the input array.
    """
    if not arr:
        return arr

    result = []
    stack = []

    for i, item in enumerate(reversed(arr)):
        if not stack:
            stack.append((item, len(arr) - i - 1))
            result.append(-1)
            continue

        while stack and stack[-1][0] >= item:
            stack.pop()

        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1][1])

        stack.append((item, len(arr) - i - 1))

    return list(reversed(result))


def NSL(arr):
    """
    Given an array 'arr', this function returns a list of the same length as 'arr', where each element at index 'i' represents the index of the Next Smaller Element (NSL) to the left of 'arr[i]'. If there is no smaller element to the left of 'arr[i]', the value at index 'i' will be -1.
    """
    if not arr:
        return arr

    result = []
    stack = []

    for i, item in enumerate(arr):
        if not stack:
            result.append(-1)
            stack.append((item, i))
            continue

        while stack and stack[-1][0] >= item:
            stack.pop()

        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1][1])

        stack.append((item, i))

    return result


def max_area_historgram(arr):
    """
    Calculate the maximum area of a histogram given an array of heights.

    Parameters:
    - arr: a list of integers representing the heights of the histogram bars

    Returns:
    - maxArea: an integer representing the maximum area of the histogram
    """
    if not arr:
        return arr

    left = NSL(arr)
    right = NSR(arr)

    maxArea = float("-inf")
    for i in range(len(arr)):
        start = 0 if left[i] == -1 else left[i] + 1
        end = len(arr) - 1 if right[i] == -1 else right[i] - 1
        maxArea = max(maxArea, arr[i] * (end - start + 1))

    return maxArea


def max_area_rectangle_binary_matrixHelper(matrix: list[list[int]]) -> int:
    if len(matrix) <= 1:
        pass
    else:
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = matrix[i][j] + \
                    matrix[i - 1][j] if matrix[i][j] else 0

    maxArea = float("-inf")
    for row in matrix:
        maxArea = max(maxArea, max_area_historgram(row))

    return maxArea


def copyMatrix(M):
    """Return a copy of matrix M."""
    mcopy = []
    for i in range(len(M)):
        # Append copy of sublist.
        mcopy.append(M[i].copy())  # Could also use M[i][:]
    return mcopy


def max_area_rectangle_binary_matrix(matrix: list[list[int]]) -> int:
    if not matrix:
        return matrix

    vertical = max_area_rectangle_binary_matrixHelper(copyMatrix(matrix))
    horizontal = max_area_rectangle_binary_matrixHelper(
        getTranspose(copyMatrix(matrix)))

    return max(vertical, horizontal)


def getTranspose(matrix):
    """
    Compute the transpose of the given matrix.

    Args:
        matrix: A 2D list representing the input matrix.

    Returns:
        A 2D list representing the transpose of the input matrix.
    """
    m, n = len(matrix), len(matrix[0])
    ans = [[None] * m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            ans[j][i] = matrix[i][j]
    return ans


matrix = [[0, 1, 1, 0],
          [1, 1, 1, 1],
          [1, 1, 1, 1],
          [1, 1, 0, 0]]

print(max_area_rectangle_binary_matrix(matrix))
