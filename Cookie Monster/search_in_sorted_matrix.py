# Time : O(n + m)
# Space : O(1)

def search_in_sorted_matrix(matrix, target):
    row = 0
    col = len(matrix[0]) - 1

    while row < len(matrix) and col >= 0:
        if target > matrix[row][col]:
            row += 1
        elif target < matrix[row][col]:
            col -= 1
        else:
            return (row, col)

    return [-1, -1]

