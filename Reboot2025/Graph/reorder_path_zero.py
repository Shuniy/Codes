import collections
def min_reorder(n: int, connections: list[list[int]]) -> int:
    graph = collections.defaultdict(set)
    roads = set()
    for u, v in connections:
        graph[u].add(v)
        graph[v].add(u)
        roads.add((u, v))

    result = 0
    def dfs(node, parent):
        nonlocal result
        if (parent, node) in roads:
            result += 1
        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            dfs(neighbor, node)

    dfs(0, -1)
    return result

# test cases
print(min_reorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]))
print(min_reorder(5, [[1,0],[1,2],[3,2],[3,4]]))
print(min_reorder(3, [[1,0],[2,0]]))
print(min_reorder(4, [[1,0],[2,0],[3,1],[3,2]]))
print(min_reorder(6, [[0,1],[0,2],[3,5],[5,4],[4,3]]))
