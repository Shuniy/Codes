import collections

def findCheapestPrice(n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
    graph = collections.defaultdict(set)
    for u, v, price in flights:
        graph[u].add((v, price))

    distances = collections.defaultdict(lambda: float('inf'))
    queue = collections.deque([])
    queue.append((src, 0, 0))

    while queue:
        node, cost, stops = queue.popleft()
        if stops > k:
            break
        
        for neighbor in graph[node]:
            new_cost = cost + neighbor[1]
            if new_cost >= distances[neighbor[0]]:
                continue
            distances[neighbor[0]] = new_cost
            queue.append((neighbor[0], new_cost, stops + 1))

    return -1 if distances[dst] == float("inf") else distances[dst]

# test cases
n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1
print(findCheapestPrice(n, flights, src, dst, k))

n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 1
print(findCheapestPrice(n, flights, src, dst, k))

n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 0
print(findCheapestPrice(n, flights, src, dst, k))

n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 2
print(findCheapestPrice(n, flights, src, dst, k))

n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 3
print(findCheapestPrice(n, flights, src, dst, k))

n = 3
flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0
dst = 2
k = 4
print(findCheapestPrice(n, flights, src, dst, k))

