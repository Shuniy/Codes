class DisjointSet:
    def __init__(self, n: int) -> None:
        self.parent = [i for i in range(n + 1)]
        self.size = [1 for _ in range(n + 1)]
        self.rank = [0 for _ in range(n + 1)]

    def findParent(self, node):
        if node == self.parent[node]:
            return node

        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]

    def unionByRank(self, u, v):
        uparent = self.findParent(u)
        vparent = self.findParent(v)
        if uparent == vparent:
            return
        if self.rank[uparent] < self.rank[vparent]:
            self.parent[uparent] = vparent
        elif self.rank[uparent] > self.rank[vparent]:
            self.parent[vparent] = uparent
        else:
            self.parent[vparent] = uparent
            self.rank[uparent] += 1

    def unionBySize(self, u, v):
        uparent = self.findParent(u)
        vparent = self.findParent(v)
        if uparent == vparent:
            return
        if self.size[uparent] < self.size[vparent]:
            self.parent[uparent] = vparent
            self.size[vparent] += self.size[uparent]
        else:
            self.parent[vparent] = uparent
            self.size[uparent] += self.size[vparent]


disjointSet = DisjointSet(7)
# disjointSet.unionByRank(1, 2)
# disjointSet.unionByRank(2, 3)
# disjointSet.unionByRank(4, 5)
# disjointSet.unionByRank(6, 7)
# disjointSet.unionByRank(5, 6)

disjointSet.unionBySize(1, 2)
disjointSet.unionBySize(2, 3)
disjointSet.unionBySize(4, 5)
disjointSet.unionBySize(6, 7)
disjointSet.unionBySize(5, 6)

if disjointSet.findParent(3) == disjointSet.findParent(7):
    print("Same")
else:
    print("Not Same")

disjointSet.unionByRank(3, 7)
if disjointSet.findParent(3) == disjointSet.findParent(7):
    print("Now Same")
else:
    print("Still Not Same")
