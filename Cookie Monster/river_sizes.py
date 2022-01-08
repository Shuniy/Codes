def riverSizes(matrix):
    sizes = []
    visited = set()

    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (i, j) in visited:
                continue
            sizes = dfs_traverse(i, j, matrix, sizes, directions, visited)
    return sizes

def dfs_traverse(x, y, matrix, sizes, directions, visited):
    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]) or (x, y) in visited:
        return

    current_river_size = 0

    nodes_to_explore_stack = [(x, y)]

    while len(nodes_to_explore_stack) > 0:
        current_node = nodes_to_explore_stack.pop()
        ix = current_node[0]
        iy = current_node[1]

        if (ix, iy) in visited:
            continue
        
        visited.add((ix, iy))
        if matrix[ix][iy] == 0:
            continue
        current_river_size += 1

        for dx, dy in directions:
            dfs_traverse(ix + dx, iy + dy, matrix, sizes, directions, visited)
        
        sizes.append(current_river_size)

    return sizes
