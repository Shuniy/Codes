import collections
def find_path_exists(n: int, edges: list[list[int]], source: int, destination: int) -> bool:
    graph = collections.defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)

    # return dfs(graph, source, destination, set())
    return bfs(graph, source, destination)

def dfs(graph, source, destination, visited):
    if source == destination:
        return True

    if source in visited:
        return False

    visited.add(source)
    for neighbour in graph[source]:
        if dfs(graph, neighbour, destination, visited):
            return True
    return False

def bfs(graph, source, destination):
    queue = collections.deque([source])
    visited = set([source])
    while queue:
        vertex = queue.popleft()
        if vertex == destination:
            return True
        for neighbour in graph[vertex]:
            if neighbour in visited:
                continue
            queue.append(neighbour)
            visited.add(neighbour)

    return False

# test cases
print(find_path_exists(3, [[0,1],[1,2],[2,0]], 0, 2))
print(find_path_exists(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5))
print(find_path_exists(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 3, 5))
print(find_path_exists(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 3, 4))
