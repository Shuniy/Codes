import collections

def cycle_detection(edges: list[list[int]]) -> bool:
    """
    This function takes a list of edges and returns a boolean indicating whether
    there is a cycle in the graph. The graph is represented as a list of edges,
    where each edge is a list containing two nodes. The function uses a BFS
    approach to traverse the graph and detect cycles.

    Parameters
    ----------
    edges : list[list[int]]
        A list of edges in the graph, where each edge is a list containing two nodes.

    Returns
    -------
    bool
        A boolean indicating whether there is a cycle in the graph.
    """
    if not edges:
        return False
        
    # Build the graph
    graph = collections.defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)

    visited = set()
    # Check all nodes in case of disconnected graph
    for node in graph:
        if node not in visited:
            if bfs(graph, node, visited):
                return True
    return False

def bfs(graph: dict, start_node: int, visited: set) -> bool:
    """
    Performs a breadth-first search (BFS) in the given graph, starting from the given node.
    If a cycle is detected, return True; otherwise, return False.

    Args:
        graph (dict): The graph represented as an adjacency list.
        start_node (int): The node to start the search from.
        visited (set): A set of nodes that have already been visited.

    Returns:
        bool: True if a cycle is detected, False otherwise.
    """
    queue = collections.deque([(start_node, -1)])  # (node, parent)
    visited.add(start_node)
    
    while queue:
        node, parent = queue.popleft()
        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            if neighbor in visited:
                return True
            visited.add(neighbor)
            queue.append((neighbor, node))
    return False

def dfs(graph: dict, node: int, parent: int, visited: set) -> bool:
    """
    Performs a depth-first search (DFS) in the given graph, starting from the given node.
    If a cycle is detected, return True; otherwise, return False.

    Args:
        graph (dict): The graph represented as an adjacency list.
        node (int): The node to start the search from.
        parent (int): The parent of the current node.
        visited (set): A set of nodes that have already been visited.

    Returns:
        bool: True if a cycle is detected, False otherwise.
    """
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor == parent:
            continue
        if neighbor in visited:
            return True
        if dfs(graph, neighbor, node, visited):
            return True
    return False

# test cases
print(cycle_detection([[0,1], [1,2], [2,3], [3,4], [4,0]]))  # True - cycle
print(cycle_detection([[0,1], [1,2], [2,3], [3,4]]))  # False - no cycle
print(cycle_detection([[0,1], [1,2], [2,3], [3,4], [0,4]]))  # True - cycle
print(cycle_detection([[0,1], [1,2], [2,3], [3,4], [0,2]]))  # True - cycle
print(cycle_detection([[0,1], [1,2], [2,3], [3,4], [0,3]]))  # True - cycle
print(cycle_detection([[0,1], [1,2], [2,3], [3,4], [0,4], [1,3]]))  # True - multiple cycles
print(cycle_detection([[0,1], [1,2], [2,3], [3,4], [0,2], [1,3]]))  # True - multiple cycles
print(cycle_detection([[0, 1], [0, 2], [1, 2], [2, 3]]))  # True - cycle
print(cycle_detection([[0, 1], [1, 2], [2, 3]]))  # False - no cycle
print(cycle_detection([[1,2],[1,3],[2,3]]))  # True - cycle
print(cycle_detection([[1,2],[2,3],[3,4],[1,4],[1,5]]))  # True - cycle
print(cycle_detection([[1,2],[3,4]]))  # False - disconnected graph, no cycle
print(cycle_detection([[1,2],[2,3],[4,5],[5,6],[6,4]]))  # True - disconnected graph with cycle
