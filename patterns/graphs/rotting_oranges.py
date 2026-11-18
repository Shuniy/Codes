import collections

def orangesRotting(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    result = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    rotten = collections.deque([])
    fresh = 0
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                fresh += 1
            elif grid[i][j] == 2:
                rotten.append((i, j))

    while rotten and fresh:
        result += 1
        for _ in range(len(rotten)):
            x, y = rotten.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx >= m or ny >= n:
                    continue
                if grid[nx][ny] != 1:
                    continue
                grid[nx][ny] = 2
                rotten.append((nx, ny))
                fresh -= 1

    return -1 if fresh else result

# test cases

grid = [[2,1,1],[1,1,0],[0,1,1]]
print(orangesRotting(grid))

grid = [[2,1,1],[0,1,1],[1,0,1]]
print(orangesRotting(grid))

grid = [[0,2]]
print(orangesRotting(grid))

grid = [[0]]
print(orangesRotting(grid))

grid = [[2,2]]
print(orangesRotting(grid))
