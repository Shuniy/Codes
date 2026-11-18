import collections

def bfs(graph, start):
    """
    Performs a breadth-first search on a graph given a starting node.

    Args:
        graph (dict): The graph represented as an adjacency list.
        start (int): The node to start the search from.

    Prints out the nodes in the order they were visited.
    """
    visited = set()
    queue = collections.deque([start])
    while queue:
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        for neighbour in graph[vertex]:
            if neighbour in visited:
                continue
            queue.append(neighbour)
            visited.add(vertex)

if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    print("Following is Breadth First Traversal: ")
    bfs(graph, 0)
