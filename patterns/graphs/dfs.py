def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        print(str(vertex) + " ", end="")
        for neighbour in graph[vertex]:
            if neighbour in visited:
                continue
            stack.append(neighbour)
            visited.add(vertex)


if __name__ == '__main__':
    graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

    dfs(graph, '0')
