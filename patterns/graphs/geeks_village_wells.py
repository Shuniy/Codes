def chefAndWells(n: int, m: int, c: list[list[str]]) -> list[list[int]]:
    """
    Geek's village is represented by a 2-D matrix of characters of size n*m, where

    H - Represents a house
    W - Represents a well
    . - Represents an open ground
    N - Prohibited area(Not allowed to enter this area)

    Every house in the village needs to take water from a well, as the family members are so busy with their work, so every family wants to take the water from a well in minimum time, which is possible only if they have to cover as less distance as possible. Your task is to determine the minimum distance that a person in the house should travel to take out the water and carry it back to the house.

    A person is allowed to move only in four directions left, right, up, and down. That means if he/she is the cell (i,j), then the possible cells he/she can reach in one move are (i,j-1),(i,j+1),(i-1,j),(i+1,j), and the person is not allowed to move out of the grid.

    Note: For all the cells containing 'N', 'W' and '.' our answer should be 0, and for all the houses where there is no possibility of taking water our answer should be -1.
    """
    import collections
    visited = set()
    result = [[0] * m for _ in range(n)]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    memo = collections.defaultdict(int)

    def dfs(x: int, y: int):
        if x < 0 or y < 0 or x >= n or y >= m or c[x][y] == "N":
            return float("inf")
        
        if (x, y) in memo:
            return memo[(x, y)]
        
        if c[x][y] == "W":
            return 0

        mn = float("inf")
        for dx, dy in directions:
            mn = min(mn, 1 + dfs(x + dx, y + dy))
            memo[(x, y)] = mn

        return memo[(x, y)]


    for i in range(n):
        for j in range(m):
            if c[i][j] == "H":
                val = dfs(i, j)
                result[i][j] = -1 if val == float("inf") else 2 * val
            else:
                result[i][j] = 0

    return result


# test cases
print(chefAndWells(3, 3, [["H", "H", "H"], ["H", "W", "H"], ["H", "H", "H"]]))
print(chefAndWells(5, 5, [["H", "N", "H", "H", "H"], 
                          ["N", "N", "H", "H", "W"],
                          ["W", "H", "H", "H", "H"],
                          ["H", "H", "H", "H", "H"],
                          ["H", "H", "H", "H", "H"]]))