import collections
from typing import List, Set

def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    return helper(image, sr, sc, image[sr][sc], color, set())

def helper(image: List[List[int]], x: int, y: int, floodColor: int, color: int, visited: Set) -> List[List[int]]:
    if x < 0 or y < 0 or x >= len(image) or y >= len(image[0]) or image[x][y] != floodColor or (x, y) in visited:
        return image
    
    visited.add((x, y))
    image[x][y] = color
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        image = helper(image, x + dx, y + dy, floodColor, color, visited)
    return image

# test cases
print(floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))
print(floodFill([[0,0,0],[0,0,0]], 0, 0, 2))
print(floodFill([[0,0,0],[0,1,1]], 1, 1, 1))