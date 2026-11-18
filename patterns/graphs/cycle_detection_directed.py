import collections

def cycle_detection_directed(edges: list[list[int]]) -> bool:
    """
    Detects if there is a cycle in a directed graph represented by edges.
    
    Args:
        edges: List of directed edges where each edge is [u, v] representing u -> v
        
    Returns:
        bool: True if a cycle exists, False otherwise
    """
    if not edges:
        return False
    
    # Build the directed graph and collect all nodes
    graph = collections.defaultdict(list)
    all_nodes = set()
    for u, v in edges:
        graph[u].append(v)  # Only add edge in one direction for directed graph
        all_nodes.add(u)
        all_nodes.add(v)
    
    visited = set()
    current_path = set()
    
    # Check all nodes in case of disconnected graph
    for node in all_nodes:
        if node not in visited:
            if cycle_detection_directed_dfs(graph, node, visited, current_path):
                return True
    return False
    
def cycle_detection_directed_dfs(graph: dict, node: int, visited: set, current_path: set) -> bool:
    """
    Helper function to perform DFS and detect cycles in a directed graph.
    
    Args:
        graph: Adjacency list representation of the graph
        node: Current node being visited
        visited: Set of nodes that have been completely processed
        current_path: Set of nodes in the current DFS path
        
    Returns:
        bool: True if a cycle is detected, False otherwise
    """
    if node in current_path:
        return True
    if node in visited:
        return False
    
    visited.add(node)
    current_path.add(node)
    
    for neighbor in graph[node]:
        if cycle_detection_directed_dfs(graph, neighbor, visited, current_path):
            return True
    
    current_path.remove(node)
    return False

# test cases
print(cycle_detection_directed([[0,1], [1,2], [2,0]]))  # True - simple cycle
print(cycle_detection_directed([[0,1], [1,2], [2,3]]))  # False - no cycle
print(cycle_detection_directed([[0,1], [1,2], [2,3], [3,1]]))  # True - cycle with branch
print(cycle_detection_directed([[0,1], [1,2], [2,1], [1,3]]))  # True - cycle with outgoing edge
print(cycle_detection_directed([[0,1], [2,3], [3,2]]))  # True - disconnected components with cycle
print(cycle_detection_directed([[0,1], [1,2], [2,3], [3,4]]))  # False - linear path
print(cycle_detection_directed([[0,1], [1,2], [2,3], [1,3]]))  # False - DAG with multiple paths
print(cycle_detection_directed([[0,1], [1,2], [2,3], [3,1], [1,4]]))  # True - complex cycle
print(cycle_detection_directed([[0,1], [1,2], [2,3], [3,4], [4,2]]))  # True - cycle with entry point
print(cycle_detection_directed([]))  # False - empty graph
print(cycle_detection_directed([[1,2], [2,3], [3,1]]))  # True - cycle not starting from 0
print(cycle_detection_directed([[1,2], [3,4], [4,3]]))  # True - disconnected components with cycle
print(cycle_detection_directed([[1,2], [2,3], [3,4]]))  # False - linear path not starting from 0
