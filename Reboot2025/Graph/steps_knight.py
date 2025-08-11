import collections

def steps_by_knight(n: int, start: list, target: list):
    visited = set()
    directions = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
    queue = collections.deque([(start, 0)])
    while queue:
        vertex = queue.popleft()
        if vertex[0] == tuple(target):
            return vertex[1]
        for direction in directions:
            new_x = vertex[0][0] + direction[0]
            new_y = vertex[0][1] + direction[1]
            if new_x < 0 or new_x >= n or new_y < 0 or new_y >= n:
                continue
            if (new_x, new_y) in visited:
                continue
            queue.append(((new_x, new_y), vertex[1] + 1))
            visited.add((new_x, new_y))

    return -1



# test cases
print(steps_by_knight(3, [0, 0], [2, 2]))
print(steps_by_knight(3, [0, 0], [2, 3]))
print(steps_by_knight(3, [0, 0], [1, 2]))
print(steps_by_knight(3, [0, 0], [0, 0]))
print(steps_by_knight(3, [0, 0], [1, 1]))