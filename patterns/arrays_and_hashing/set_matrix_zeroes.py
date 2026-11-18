"""
Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
"""

def set_matrix_zero_new_arrays(matrix, m, n):
    row = [0 for _ in range(m)]
    col = [0 for _ in range(n)]

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                row[i] = 0
                col[j] = 0

    for i in range(m):
        for j in range(n):
            if row[i] == 0:
                matrix[i][j] = 0
            elif col[j] == 0:
                matrix[i][j] = 0
            else:
                pass

    return matrix

def set_matrix_zero_constant(matrix, m, n):
    flag = False
    row = False
    column = False
    if matrix[0][0] == 0:
        flag = True
        row = False
        column = False

    for i in range(1, m):
        if matrix[i][0] == 0:
            column = True
            break

    for i in range(1, n):
        if matrix[0][i] == 0:
            row = True
            break

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0

    for i in range(1, m):
        for j in range(1, n):
            if not matrix[i][0] or not matrix[0][j]:
                matrix[i][j] = 0

    if flag:
        for i in range(1, m):
            matrix[i][0] = 0
        for i in range(n):
            matrix[0][i] = 0

    else:
        if column:
            for i in range(m):
                matrix[i][0] = 0
        if row:
            for i in range(n):
                matrix[0][i] = 0

