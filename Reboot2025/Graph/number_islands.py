import collections

def numIslands(grid: list[list[str]]) -> int:
    m, n = len(grid), len(grid[0])
    visited = set()
    result = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def dfs(x: int, y: int):
        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] != "1" or (x, y) in visited:
            return
        
        visited.add((x, y))
        for dx, dy in directions:
            dfs(x + dx, y + dy)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1" and (i, j) not in visited:
                result += 1
                dfs(i, j)
    return result

# test cases

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(numIslands(grid))