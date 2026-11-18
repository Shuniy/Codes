import collections

def make_connected(n: int, connections: list[list[int]]) -> int:
    if len(connections) < n - 1: 
        return -1

    graph = collections.defaultdict(set)
    for u, v in connections:
        graph[u].add(v)
        graph[v].add(u)

    visited = set()
    def dfs(node: int):
        """
        Performs a depth-first search (DFS) starting from the given node,
        marking all reachable nodes as visited.

        Args:
            node (int): The starting node for the DFS traversal.
        """
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor)

    result = 0
    for i in range(n):
        if i in visited:
            continue
        dfs(i)
        result += 1

    return result

# test cases

n = 4
connections = [[0,1],[0,2],[1,2]]
print(make_connected(n, connections))

n = 6
connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
print(make_connected(n, connections))

n = 6
connections = [[0,1],[0,2],[0,3],[1,2]]
print(make_connected(n, connections))

n = 12
connections = [[1,5],[1,7],[1,2],[1,4],[3,7],[4,7],[3,5],[0,6],[0,1],[0,4],[2,6],[0,3],[0,2]]
print(make_connected(n, connections))