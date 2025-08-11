import collections

def snakesAndLadders(board: list[list[int]]) -> int:
    n = len(board)
    graph = collections.defaultdict(set)
    connections = collections.defaultdict(int)
    forward = True
    node = 1
    for i in range(n - 1, -1, -1):
        if forward:
            for j in range(n):
                if board[i][j] != -1:
                    connections[node] = board[i][j]
                node += 1
        else:
            for j in range(n - 1, -1, -1):
                if board[i][j] != -1:
                    connections[node] = board[i][j]
                node += 1
        forward = not forward

    for i in range(1, n * n + 1):
        for dice in range(1, 7):
            next_node = i + dice
            if next_node > n * n:
                continue
            if next_node in connections:
                graph[i].add(connections[next_node])
            else:
                graph[i].add(next_node)

    queue = collections.deque([1])
    visited = set()
    steps = 0
    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            current_node = queue.popleft()
            if current_node == n * n:
                return steps
            if current_node in visited:
                continue
            visited.add(current_node)
            for neighbor in graph[current_node]:
                queue.append(neighbor)
        steps += 1

    return -1

# test cases
board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
print(snakesAndLadders(board))

board = [[-1,-1],[-1,3]]
print(snakesAndLadders(board))

board = [[1,1,-1],[1,1,1],[-1,1,1]]
print(snakesAndLadders(board))