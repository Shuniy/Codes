import collections
from typing import List, Set

def largest_color_value(colors: str, edges: List[List[int]]) -> int:
    """
    Find the largest color value in a graph using dynamic programming.
    # Failing for Straight paths
    """
    n = len(colors)
    graph = collections.defaultdict(set)
    all_nodes = set()
    for u, v in edges:
        graph[u].add(v)
        all_nodes.add(u)
        all_nodes.add(v)

    # Check for cycles in the entire graph
    visited = set()
    for node in all_nodes:
        if node in visited:
            continue
        if has_cycle(graph, node, visited, set()):
            return -1
    
    memo = collections.defaultdict(int)
    
    def dfs(node: int, color: str) -> int:
        count, mx = 0, 0
        if (node, color) in memo:
            return memo[(node, color)]
        if color == colors[node]:
            count += 1
        for neighbor in graph[node]:
            mx = max(mx, dfs(neighbor, color))
        memo[(node, color)] = mx + count
        return memo[(node, color)]

    result = -1
    for node in range(n):
        result = max(result, dfs(node, colors[node]))
    
    return result

def has_cycle(graph: collections.defaultdict, node: int, visited: Set[int], current_path: Set[int]) -> bool:
    if node in current_path:
        return True
    
    if node in visited:
        return False

    visited.add(node)
    current_path.add(node)

    for neighbour in graph[node]:
        if has_cycle(graph, neighbour, visited, current_path):
            return True

    current_path.remove(node)
    return False

# test cases
print(largest_color_value("abaca", [[0,1],[0,2],[2,3],[3,4]]))  # Expected: 3
print(largest_color_value("aa", [[0,1]]))  # Expected: 1
print(largest_color_value("a", [[0,0]]))  # Expected: -1
print(largest_color_value("abc", [[0,1],[1,2]]))  # Expected: 1
print(largest_color_value("iiiiii", [[0,1],[1,2],[2,3],[3,4],[4,5]]))  # Expected: 6