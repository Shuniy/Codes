import collections

def bellman_ford(connections: list[list[int]], n: int, start_node: int):
    distances = collections.defaultdict(lambda: float('inf'))
    distances[start_node] = 0
    for iteration in range(n):
        for edge in connections:
            u, v, distance = edge
            new_distance = distances[u] + distance
            if new_distance >= distances[v]:
                continue
            if iteration == n - 1:
                return collections.defaultdict(lambda: float('inf'))
            distances[v] = new_distance

    return distances

# test cases
connections = [[0,1,1],[0,2,5],[1,2,3],[2,3,1]]
n = 4
start_node = 0
print(bellman_ford(connections, n, start_node))

connections = [[0,1,1],[2,3,1]]
n = 4
start_node = 0
print(bellman_ford(connections, n, start_node))

connections = [[0,1,1],[1,2,1]]
n = 3
start_node = 0
print(bellman_ford(connections, n, start_node))

connections = [[1, 3, 2], [4, 3, -1], [2, 4, 1], [1, 2, 1], [0, 1, 5]]
n = 5
start_node = 0
print(bellman_ford(connections, n, start_node))