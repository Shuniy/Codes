def floyd_warshall(connections: list[list[int]], n: int):
    # k is intermediate
    for k in range(n):
        # i is source
        for i in range(n):
            # j is destination
            for j in range(n):
                if i == j or j == k or i == k:
                    continue
                if connections[i][k] == float("inf") or connections[k][j] == float("inf"):
                    continue
                connections[i][j] = min(connections[i][j], connections[i][k] + connections[k][j])

    return connections

# test cases
connections = [[0,1,1],[0,2,5],[1,2,3],[2,3,1]]
n = 3
print(floyd_warshall(connections, n))

connections = [
    [0, 4, float("inf"), 5, float("inf")],
    [float("inf"), 0, 1, float("inf"), 6],
    [2, float("inf"), 0, 3, float("inf")],
    [float("inf"), float("inf"), 1, 0, 2],
    [1, float("inf"), float("inf"), 4, 0]
]
n = 5
print(floyd_warshall(connections, n))