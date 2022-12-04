class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        self.result = []
        self.board = [["." for _ in range(n)] for _ in range(n)]
        self.nQueenHelper(n, 0)
        return self.result

    def isValidPosition(self, row: int, col: int, n: int) -> bool:
        for i in range(row - 1, -1, -1):
            if self.board[i][col] == "Q":
                return False
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if self.board[i][j] == "Q":
                return False
            i -= 1
            j -= 1
        i = row - 1
        j = col + 1
        while i >= 0 and j < n:
            if self.board[i][j] == "Q":
                return False
            i -= 1
            j += 1
        return True

    def nQueenHelper(self, n: int, row: int) -> None:
        if row == n:
            result = []
            for row in self.board:
                result.append("".join(row))
            self.result.append(result)
            return
        for col in range(n):
            if self.isValidPosition(row, col, n):
                self.board[row][col] = "Q"
                self.nQueenHelper(n, row + 1)
                self.board[row][col] = "."
        return
