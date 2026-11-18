import collections

def sudoku_solver(board: list[list[int]]):
    """
    Solves a Sudoku puzzle given as a 9x9 grid.

    The Sudoku puzzle is given as a 9x9 grid, where empty cells are represented by
    the string ".". The function attempts to solve the puzzle by placing numbers
    from 1 to 9 in the empty cells such that each row, column, and 3x3 sub-grid
    contains each number only once. If a solution exists, the function modifies the
    input grid in-place and returns the solved board. If no solution exists, the
    function returns None.

    Parameters:
        board (list[list[int]]): A 9x9 grid representing the Sudoku puzzle.

    Returns:
        list[list[int]]: The solved Sudoku puzzle as a 9x9 grid. If no solution exists, None is returned.
    """
    rows, cols, triples = collections.defaultdict(set), collections.defaultdict(set), collections.defaultdict(set)
    for r in range(9):
        for c in range(9):
            if board[r][c] != ".":
                if rows.get(r) is None:
                    rows[r] = set()
                if cols.get(c) is None:
                    cols[c] = set()
                if triples.get((r // 3, c // 3)) is None:
                    triples[(r // 3, c // 3)] = set()
                rows[r].add(int(board[r][c]))
                cols[c].add(int(board[r][c]))
                triples[(r // 3, c // 3)].add(int(board[r][c]))

    sudoku_solver_helper(board, 0, 0, rows, cols, triples)
    return board

def sudoku_solver_helper(board: list[list[int]], row: int, col: int, rows: dict, cols: dict, triples: dict):
    """
    A recursive helper function to solve a Sudoku puzzle.

    The function attempts to solve the puzzle by placing numbers from 1 to 9 in the empty cells
    such that each row, column, and 3x3 sub-grid contains each number only once. The function uses
    backtracking to try all possible combinations of numbers.

    Parameters:
        board (list[list[int]]): A 9x9 grid representing the Sudoku puzzle.
        row (int): The current row index in the puzzle.
        col (int): The current column index in the puzzle.
        rows (dict): A dictionary of sets storing the numbers already present in each row.
        cols (dict): A dictionary of sets storing the numbers already present in each column.
        triples (dict): A dictionary of sets storing the numbers already present in each 3x3 sub-grid.

    Returns:
        bool: True if a solution exists, False otherwise.
    """
    if row == len(board):
        return True
    if col == len(board[0]):
        return sudoku_solver_helper(board, row + 1, 0, rows, cols, triples)

    if board[row][col] != ".":
        return sudoku_solver_helper(board, row, col + 1, rows, cols, triples)
    for num in range(1, 10):
        if (row in rows and num in rows[row]) or (col in cols and num in cols[col]) or ((row // 3, col // 3) in triples and num in triples[(row // 3, col // 3)]):
            continue
        board[row][col] = str(num)
        rows[row].add(num)
        cols[col].add(num)
        triples[(row // 3, col // 3)].add(num)
        if sudoku_solver_helper(board, row, col + 1, rows, cols, triples):
            return True
        rows[row].remove(num)
        cols[col].remove(num)
        triples[(row // 3, col // 3)].remove(num)
        board[row][col] = "."
    return False

# test cases
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
print(sudoku_solver(board))

board = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
print(sudoku_solver(board))

board = [
    [".",".","4",".",".",".","6","3","."],
    [".",".",".",".","7",".",".",".","."],
    ["5",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"]
]
print(sudoku_solver(board))

board = [
    [".",".","4",".",".",".","6","3","."],
    [".",".",".",".","7",".",".",".","."],
    ["5",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"]
]
print(sudoku_solver(board))

board = [
    [".",".","4",".",".",".","6","3","."],
    [".",".",".",".","7",".",".",".","."],
    ["5",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"]
]
print(sudoku_solver(board))

board = [
    [".",".","9","7","4","8",".",".","."],
    ["7",".",".",".",".",".",".",".","."],
    [".","2",".","1",".","9",".",".","."],
    [".",".","7",".",".",".","2","4","."],
    [".","6","4",".","1",".","5","9","."],
    [".","9","8",".",".",".","3",".","."],
    [".",".",".","8",".","3",".","2","."],
    [".",".",".",".",".",".",".",".","6"],
    [".",".",".","2","7","5","9",".","."]
]
print(sudoku_solver(board))