import collections
from typing import List, Set

def largest_color_value_topological_sort(colors: str, edges: List[List[int]]) -> int:
    """
    Find the largest color value in a graph using topological sorting.
    """
    n = len(colors)
    graph = collections.defaultdict(set)
    indegree = [0] * n

    for u, v in edges:
        graph[u].add(v)
        indegree[v] += 1

    # Topological sort using Kahn's algorithm
    queue = collections.deque([i for i in range(n) if indegree[i] == 0])
    topo_order = []
    processed = 0
    result = 0
    count = [[0] * 26 for _ in range(n)]  # Count of each color for each node
    while queue:
        node = queue.popleft()
        topo_order.append(node)
        processed += 1
        count[node][ord(colors[node]) - ord('a')] += 1
        result = max(result, count[node][ord(colors[node]) - ord('a')])
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
            for color_index in range(26):
                count[neighbor][color_index] = max(count[neighbor][color_index], count[node][color_index])

    if len(topo_order) != n:
        return -1  # Cycle detected

    return result

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

print(largest_color_value_topological_sort("abaca", [[0,1],[0,2],[2,3],[3,4]]))  # Expected: 3
print(largest_color_value_topological_sort("aa", [[0,1]]))  # Expected: 1
print(largest_color_value_topological_sort("a", [[0,0]]))  # Expected: -1
print(largest_color_value_topological_sort("abc", [[0,1],[1,2]]))  # Expected: 1
print(largest_color_value_topological_sort("iiiiii", [[0,1],[1,2],[2,3],[3,4],[4,5]]))  # Expected: 6
