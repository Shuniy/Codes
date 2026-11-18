import collections
from typing import List, Set, Dict, Tuple

def topological_sort_kahn(edges: List[Tuple[int, int]]) -> List[int]:
    """
    Perform topological sort on a directed graph using Kahn's algorithm.
    Returns a valid topological ordering if the graph is a DAG, empty list otherwise.
    
    Args:
        edges: List of directed edges where each edge is (u, v) representing u -> v
        
    Returns:
        List[int]: A valid topological ordering if the graph is a DAG, empty list if it contains cycles
    """
    if not edges:
        return []
    
    # Build the directed graph and collect all nodes
    graph: Dict[int, Set[int]] = collections.defaultdict(set)
    in_degree: Dict[int, int] = collections.defaultdict(int)
    all_nodes = set()
    
    for u, v in edges:
        graph[u].add(v)
        in_degree[v] += 1
        all_nodes.add(u)
        all_nodes.add(v)
    
    # Initialize queue with nodes having zero in-degree
    queue = collections.deque([node for node in all_nodes if in_degree[node] == 0])
    visited: Set[int] = set()
    result: List[int] = []
    
    while queue:
        node = queue.popleft()
        visited.add(node)
        result.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check if we visited all nodes (no cycles)
    if len(visited) != len(all_nodes):
        print("Cycle detected")
        return []  # Graph contains cycles
    
    return result

# test cases
print(topological_sort_kahn([(0, 1), (1, 2), (2, 3), (3, 4)]))  # [0, 1, 2, 3, 4] - simple DAG
print(topological_sort_kahn([(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]))  # [] - cycle
print(topological_sort_kahn([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)]))  # [] - longer cycle
print(topological_sort_kahn([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 0)]))  # [] - cycle
print(topological_sort_kahn([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9)]))  # [0,1,2,3,4,5,6,7,8,9] - linear DAG
print(topological_sort_kahn([(1, 2), (2, 3), (3, 4), (4, 5)]))  # [1,2,3,4,5] - DAG not starting from 0
print(topological_sort_kahn([(1, 2), (2, 3), (3, 4), (4, 5), (5, 3)]))  # [] - cycle with branch
print(topological_sort_kahn([]))  # [] - empty graph
print(topological_sort_kahn([(1, 2), (3, 4), (4, 3)]))  # [] - disconnected components with cycle
print(topological_sort_kahn([(1, 2), (2, 3), (3, 4), (1, 3)]))  # [1,2,3,4] - DAG with multiple paths