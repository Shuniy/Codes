import collections
from typing import List, Tuple, Dict, Set, Optional

def topological_sort(edges: List[Tuple[int, int]]) -> List[int]:
    """
    Perform topological sort on a directed graph using DFS.
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
    all_nodes = set()
    for u, v in edges:
        graph[u].add(v)
        all_nodes.add(u)
        all_nodes.add(v)
    
    visited: Set[int] = set()
    current_path: Set[int] = set()
    stack: List[int] = []
    has_cycle = False

    def dfs(node: int) -> None:
        nonlocal has_cycle
        if has_cycle:
            return
            
        if node in current_path:
            has_cycle = True
            return
            
        if node in visited:
            return
            
        visited.add(node)
        current_path.add(node)
        
        for neighbor in graph[node]:
            dfs(neighbor)
            if has_cycle:
                return
                
        current_path.remove(node)
        stack.append(node)

    for node in all_nodes:
        if node not in visited:
            dfs(node)
            if has_cycle:
                return []

    return stack[::-1]

# test cases
print(topological_sort([(1, 2), (2, 3), (3, 4), (1, 3)]))  # [1,2,3,4] - DAG with multiple paths
print(topological_sort([(0, 1), (1, 2), (2, 3), (3, 4)]))  # [0,1,2,3,4] - simple DAG
print(topological_sort([(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]))  # [] - cycle
print(topological_sort([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)]))  # [] - longer cycle
print(topological_sort([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 0)]))  # [] - cycle
print(topological_sort([(1, 2), (2, 3), (3, 4), (4, 5)]))  # [1,2,3,4,5] - DAG not starting from 0
print(topological_sort([(1, 2), (2, 3), (3, 4), (4, 5), (5, 3)]))  # [] - cycle with branch
print(topological_sort([]))  # [] - empty graph
print(topological_sort([(1, 2), (3, 4), (4, 3)]))  # [] - disconnected components with cycle
print(topological_sort([(1, 2), (2, 3), (3, 4), (1, 3)]))  # [1,2,3,4] - DAG with multiple paths
