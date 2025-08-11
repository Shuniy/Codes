import collections
import heapq

def dijkstra_shortest_path(connections: list[list[int]], start: int, end: int) -> int:
    graph = collections.defaultdict(set)
    for u, v, distance in connections:
        graph[u].add((v, distance))

    distances = collections.defaultdict(lambda: float('inf'))
    distances[start] = 0
    min_heap = [(0, start)]
    while min_heap:
        distance, node = heapq.heappop(min_heap)
        if node == end:
            return distance
        for neighbor, next_distance in graph[node]:
            new_distance = distance + next_distance
            if new_distance >= distances[neighbor]:
                continue
            distances[neighbor] = new_distance
            heapq.heappush(min_heap, (new_distance, neighbor))

    return -1

# test cases
connections = [[0,1,2],[1,2,4],[2,0,8],[1,3,16]]
start = 0
end = 3
print(dijkstra_shortest_path(connections, start, end))

connections = [[0,1,2],[1,2,4],[2,0,8],[1,3,16]]
start = 0
end = 2
print(dijkstra_shortest_path(connections, start, end))

connections = [[0,1,2],[1,2,4],[2,0,8],[1,3,16]]
start = 0
end = 1
print(dijkstra_shortest_path(connections, start, end))

connections = [[0,1,2],[1,2,4],[2,0,8],[1,3,16]]
start = 0
end = 4
print(dijkstra_shortest_path(connections, start, end))

connections = [[0, 1, 4], [0, 2, 8], [1, 4, 6], [2, 3, 2], [3, 4, 10]] 
start = 0
end = 0
print(dijkstra_shortest_path(connections, start, end))

connections = [[0, 1, 4], [0, 2, 8], [1, 4, 6], [2, 3, 2], [3, 4, 10]] 
start = 0
end = 1
print(dijkstra_shortest_path(connections, start, end))

connections = [[0, 1, 4], [0, 2, 8], [1, 4, 6], [2, 3, 2], [3, 4, 10]] 
start = 0
end = 2
print(dijkstra_shortest_path(connections, start, end))

connections = [[0, 1, 4], [0, 2, 8], [1, 4, 6], [2, 3, 2], [3, 4, 10]] 
start = 0
end = 3
print(dijkstra_shortest_path(connections, start, end))

connections = [[0, 1, 4], [0, 2, 8], [1, 4, 6], [2, 3, 2], [3, 4, 10]] 
start = 0
end = 4
print(dijkstra_shortest_path(connections, start, end))