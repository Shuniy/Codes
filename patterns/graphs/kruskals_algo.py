class DSU:
    def __init__(self, vertices: list[str]) -> None:
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, i: str):
        if self.parent[i] == i:
            return i
        
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        rooti = self.find(i)
        rootj = self.find(j)
        ranki = self.rank[rooti]
        rankj = self.rank[rootj]
        
        if rooti != rootj:
            if ranki < rankj:
                self.parent[rooti] = rootj
            elif ranki > rankj:
                self.parent[rootj] = rooti
            else:
                self.parent[rootj] = rooti
                self.rank[rooti] += 1
            return True
        return False


def kruskals_mst(connections: list[tuple], vertices: list[str]):
    sorted_edges = sorted(connections, key=lambda x: x[2])
    dsu = DSU(vertices)
    edges = []
    total_weight = 0
    edges_count = 0
    n = len(vertices)

    for u, v, wt in sorted_edges:
        if dsu.find(u) != dsu.find(v):
            dsu.union(u, v)
            edges.append((u, v, wt))
            total_weight += wt
            edges_count += 1

        if edges_count == n - 1:
            break

    return total_weight, edges


connections = [
    ('a', 'b', 5), ('a', 'c', 13), ('b', 'c', 2),
    ('b', 'e', 17), ('c', 'e', 25), ('b', 'd', 7), ('d', 'e', 8),
    ('c', 'g', 5), ('g', 'f', 9), ('e', 'f', 1),
]

print(kruskals_mst(connections, ['a', 'b', 'c', 'd', 'e', 'f', 'g']))