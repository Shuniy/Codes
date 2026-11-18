import heapq
import collections

def prims_mst(connections, start):
    graph = collections.defaultdict(set)
    for u, v, distance in connections:
        graph[u].add((v, distance))
        graph[v].add((u, distance))

    if not graph:
        return 0, []
    
    heap = []
    heap.append((0, start, None)) # (weight, node, parent)
    total_weight = 0
    edges = []
    visited = set()

    while heap:
        weight, node, parent = heapq.heappop(heap)
        if node in visited:
            continue

        visited.add(node)
        total_weight += weight

        if parent is not None:
            edges.append((parent, node, weight))
        
        for neighbor, wt in graph[node]:
            if neighbor not in visited:
                heapq.heappush(heap, (wt, neighbor, node))


    return total_weight, edges

connections = [
    ('a', 'b', 5), ('a', 'c', 13), ('b', 'c', 2),
    ('b', 'e', 17), ('c', 'e', 25), ('b', 'd', 7), ('d', 'e', 8),
    ('c', 'g', 5), ('g', 'f', 9), ('e', 'f', 1),
]

print(prims_mst(connections, 'a'))