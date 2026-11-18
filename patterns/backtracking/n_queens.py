def n_queens(n: int):
    result = []
    board = [["."]*n for _ in range(n)]
    n_queens_helper(n, 0, board, result)
    return result

def can_place(n: int, row: int, col: int, board: list[list]):
    # check if can be added in this col
    for i in range(row - 1, -1, -1):
        if board[i][col] == "Q":
            return False
        
    # upper left
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # upper right
    i = row - 1
    j = col + 1
    while i >= 0 and j < n:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1
    return True



def n_queens_helper(n: int, row: int, board: list[list], result: list):
    if row == n:
        result.append(["".join(row) for row in board])
        return

    for col in range(n):
        if can_place(n, row, col, board):
            board[row][col] = "Q"
            n_queens_helper(n, row + 1, board, result)
            board[row][col] = "."

# test cases
print(n_queens(4))
print(n_queens(1))
print(n_queens(8))
print(n_queens(2))
print(n_queens(3))
print(n_queens(5))
