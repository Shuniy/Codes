import collections
import heapq

def path_minimum_effort(heights: list[list[int]]) -> int :
    """
    You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.
    A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.
    Return the minimum effort required to travel from the top-left cell to the bottom-right cell.
    """
    distances = collections.defaultdict(lambda: float('inf'))
    distances[(0, 0)] = 0
    min_heap = [(0, (0, 0))]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while min_heap:
        distance, node = heapq.heappop(min_heap)
        if node == (len(heights) - 1, len(heights[0]) - 1):
            return distance
        for direction in directions:
            next_node = (node[0] + direction[0], node[1] + direction[1])
            if next_node[0] < 0 or next_node[0] >= len(heights) or next_node[1] < 0 or next_node[1] >= len(heights[0]):
                continue
            next_distance = max(distance, abs(heights[node[0]][node[1]] - heights[next_node[0]][next_node[1]]))
            if next_distance >= distances[next_node]:
                continue
            distances[next_node] = next_distance
            heapq.heappush(min_heap, (next_distance, next_node))
    
    return -1

# test cases
heights = [[1,2,2],[3,8,2],[5,3,5]]
print(path_minimum_effort(heights))

heights = [[1,2,3],[3,8,4],[5,3,5]]
print(path_minimum_effort(heights))

heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
print(path_minimum_effort(heights))