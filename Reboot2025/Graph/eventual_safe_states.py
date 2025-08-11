import collections
from typing import List, Set, Tuple

def eventual_safe_states(edges: List[List[int]]) -> List[int]:
    """
    Given a directed graph represented by edges, return a list of all nodes that are eventually safe.
    A node is eventually safe if all possible paths starting at that node lead to a terminal node.
    
    Args:
        edges: List of directed edges where each edge is [u, v] representing u -> v
        
    Returns:
        List of safe nodes in sorted order
    """
    if not edges:
        return []
    
    # Build the directed graph and collect all nodes
    graph = collections.defaultdict(set)
    all_nodes = set()
    for u, v in edges:
        graph[u].add(v)
        all_nodes.add(u)
        all_nodes.add(v)
    
    # Initialize all nodes as unsafe
    safe = all_nodes.copy()
    visited = set()
    
    for node in all_nodes:
        if node not in visited:
            result = is_node_in_cycle(graph, node, visited, set())
            if result[0]:
                safe -= result[1]

    return list(safe)

def is_node_in_cycle(graph: collections.defaultdict, node: int, visited: Set[int], current_path: Set[int]) -> Tuple[bool, Set[int]]:
    """
    Helper function to check if a node is part of a cycle.
    
    Args:
        graph: Adjacency list representation of the graph
        node: Current node being visited
        visited: Set of nodes that have been completely processed
        current_path: Set of nodes in the current DFS path
        
    Returns:
        Tuple containing:
        - bool: True if node is part of a cycle, False otherwise
        - Set[int]: Set of nodes in the current path
    """
    if node in current_path:
        return (True, current_path)
    if node in visited:
        return (False, current_path)
    
    visited.add(node)
    current_path.add(node)
    
    for neighbor in graph[node]:
        is_cycle, cycle_nodes = is_node_in_cycle(graph, neighbor, visited, current_path)
        if is_cycle:
            return (True, cycle_nodes)

    current_path.remove(node)
    return (False, current_path)

# test cases
print(eventual_safe_states([[0,1], [1,2], [2,0]]))  # [] - all nodes in cycle
print(eventual_safe_states([[0,1], [1,2], [2,3]]))  # [0,1,2,3] - no cycles
print(eventual_safe_states([[0,1], [1,2], [2,3], [3,1]]))  # [] - all nodes in cycle
print(eventual_safe_states([[0,1], [1,2], [2,1], [1,3]]))  # [3] - only terminal node is safe
print(eventual_safe_states([[0,1], [2,3], [3,2]]))  # [0,1] - disconnected components with cycle
print(eventual_safe_states([[0,1], [1,2], [2,3], [3,4]]))  # [0,1,2,3,4] - linear path
print(eventual_safe_states([[0,1], [1,2], [2,3], [1,3]]))  # [0,1,2,3] - DAG with multiple paths
print(eventual_safe_states([[0,1], [1,2], [2,3], [3,1], [1,4]]))  # [4] - complex cycle
print(eventual_safe_states([[0,1], [1,2], [2,3], [3,4], [4,2]]))  # [0,1] - cycle with entry point
print(eventual_safe_states([]))  # [] - empty graph
print(eventual_safe_states([[1,2], [2,3], [3,1]]))  # [] - cycle not starting from 0
print(eventual_safe_states([[1,2], [3,4], [4,3]]))  # [1,2] - disconnected components with cycle
print(eventual_safe_states([[1,2], [2,3], [3,4]]))  # [1,2,3,4] - linear path not starting from 0
