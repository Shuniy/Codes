import collections
from typing import List, Set, Tuple, Dict

def longest_cycle(edges: List[List[int]]) -> int:
    """
    Given a directed graph represented by edges, find the length of the longest cycle.
    
    Args:
        edges: List of directed edges where each edge is [u, v] representing u -> v
        
    Returns:
        int: Length of the longest cycle, or 0 if no cycle exists
    """
    if not edges:
        return 0
        
    # Build the directed graph and collect all nodes
    graph: Dict[int, List[int]] = collections.defaultdict(set)
    all_nodes = set()
    for u, v in edges:
        graph[u].add(v)
        all_nodes.add(u)
        all_nodes.add(v)
    
    result = 0
    visited = set()
    
    for node in all_nodes:
        if node not in visited:
            cycle_found, cycle_length = find_cycle_length(graph, node, visited, set(), [], {})
            if cycle_found:
                result = max(result, cycle_length)
    
    return result

def find_cycle_length(graph: Dict[int, List[int]], node: int, visited: Set[int], current_path: Set[int], path_order: list[int], memo: dict) -> Tuple[bool, int]:
    """
    Helper function to find the length of a cycle starting from the given node.
    
    Args:
        graph: Adjacency list representation of the graph
        node: Current node being visited
        visited: Set of nodes that have been completely processed
        current_path: Set of nodes in the current DFS path
        
    Returns:
        Tuple containing:
        - bool: True if a cycle is found, False otherwise
        - int: Length of the cycle if found, 0 otherwise
    """
    if node in memo:
        return memo[node]

    if node in current_path:
        return (True, len(current_path) - path_order.index(node))

    if node in visited:
        return (False, len(current_path))

    visited.add(node)
    current_path.add(node)
    path_order.append(node)
    
    for neighbor in graph[node]:
        result = find_cycle_length(graph, neighbor, visited, current_path, path_order, memo)
        memo[node] = result
        if result[0]:
            return result
    current_path.remove(node)
    path_order.remove(node)
    memo[node] = (False, len(current_path))
    return memo[node]

# test cases
print(longest_cycle([[1, 2], [2, 3], [3, 4], [4, 1]]))  # 4 - simple cycle
print(longest_cycle([[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]]))  # 5 - longer cycle
print(longest_cycle([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 1]]))  # 6 - even longer cycle
print(longest_cycle([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 1]]))  # 10 - longest cycle
print(longest_cycle([[1, 2], [2, 3], [3, 1], [4, 5], [5, 6], [6, 4]]))  # 3 - multiple cycles, should return length of longest
print(longest_cycle([[1, 2], [2, 3], [3, 4], [4, 2]]))  # 3 - cycle with entry point
print(longest_cycle([[1, 2], [2, 3], [3, 4], [4, 5]]))  # 0 - no cycle
print(longest_cycle([[1, 2], [2, 3], [3, 4], [4, 5], [5, 3]]))  # 3 - cycle with branch
print(longest_cycle([]))  # 0 - empty graph
print(longest_cycle([[1, 2], [3, 4], [4, 3]]))  # 2 - disconnected components with cycle
