import collections


class Graph(object):
    def __init__(self, size) -> None:
        self.adjacencyList = collections.defaultdict(set)
        self.adjacencyMatrix = [[0 for _ in range(size)]
                                for _ in range(size)]
        self.size = size

    def addEdge(self, v1, v2, undirected: bool, v1tov2: bool | None = None):
        if v1 == v2:
            print("Self Connected: ")
            return

        if not undirected or v1tov2 is None:
            self.adjacencyMatrix[v1][v2] = 1
            self.adjacencyMatrix[v2][v1] = 1
            self.adjacencyList[v1].add(v2)
            self.adjacencyList[v2].add(v1)
        else:
            if v1tov2:
                self.adjacencyMatrix[v1][v2] = 1
                self.adjacencyList[v1].add(v2)
            else:
                self.adjacencyMatrix[v2][v1] = 1
                self.adjacencyList[v2].add(v1)

    def removeEdge(self, v1, v2, removeBoth: bool, v1Tov2: bool | None = None):
        if v1 == v2:
            self.adjacencyMatrix[v1][v2] = 0
            self.adjacencyList[v1].remove(v2)
            return
        if removeBoth or v1Tov2 is None:
            self.adjacencyMatrix[v1][v2] = 0
            self.adjacencyMatrix[v2][v1] = 0
            self.adjacencyList[v2].remove(v1)
            self.adjacencyList[v1].remove(v2)
        else:
            if v1Tov2:
                self.adjacencyMatrix[v1][v2] = 0
                self.adjacencyList[v1].remove(v2)
            else:
                self.adjacencyMatrix[v2][v1] = 0
                self.adjacencyList[v2].remove(v1)

    def __len__(self):
        return self.size

    def convertAdjacencyMatrixToList(self):
        adjList = collections.defaultdict(set)
        for i in range(len(self.adjacencyMatrix)):
            for j in range(len(self.adjacencyMatrix[i])):
                if self.adjacencyMatrix[i][j] != 0:
                    adjList[i].add(j)
        return adjList

    def convertAdjacencyListToMatrix(self):
        adjMatrix = [[0 for _ in range(self.size)]
                     for _ in range(self.size)]
        values = self.adjacencyList.items()
        print(values)
        for item in values:
            v1 = item[0]
            v2 = item[1]
            for node in v2:
                adjMatrix[v1][node] = 1
        return adjMatrix

    # Print the matrix
    def printAdjacencyMatrix(self):
        for row in self.adjacencyMatrix:
            for val in row:
                print(val, end="", sep=" ")
            print()

    # Print the matrix
    def printAdjacencyList(self):
        values = self.adjacencyList.items()
        for item in values:
            print(item[0], item[1], end="", sep=" ")
            print()

    def dfs(self, start, searchNode, visited=None):
        if searchNode > 9:
            return self.dfsStack(start, searchNode)
        if visited is None:
            visited = set()
        visited.add(start)

        if searchNode is None:
            return False

        if start == searchNode:
            return True

        found = False
        for nextNode in self.adjacencyList[start] - visited:
            found = self.dfs(nextNode, searchNode, visited)
            if found:
                break
        return found

    def dfsStack(self, start, searchNode):
        if searchNode is None:
            return False

        if start == searchNode:
            return True

        stack = [start]
        visited = set()
        found = False
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
            if node == searchNode:
                found = True
                break
            for nextNode in self.adjacencyList[node]:
                if nextNode not in visited:
                    stack.append(nextNode)
        return found

    def bfs(self, root, searchNode):
        if searchNode is None:
            return False

        if root == searchNode:
            return True

        visited, queue = set(), collections.deque([root])
        visited.add(root)

        found = False
        while queue:
            # Dequeue a vertex from queue
            vertex = queue.popleft()
            # If not visited, mark it as visited, and
            # enqueue it
            if vertex == searchNode:
                found = True
                break
            for neighbour in self.adjacencyList[vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
        return found


graph = Graph(5)
graph.addEdge(0, 1, True)
graph.addEdge(0, 2, False)
graph.addEdge(1, 2, True)
graph.addEdge(2, 0, False)
graph.addEdge(2, 0, True)
graph.addEdge(0, 4, False)
graph.addEdge(4, 0, True)
graph.printAdjacencyMatrix()
graph.printAdjacencyList()
print("Adjacency List: ", graph.convertAdjacencyMatrixToList())
print("Adjacency Matrix: ", graph.convertAdjacencyListToMatrix())
print("DFS Visited: 0 to 4", graph.dfs(0, 4))
print("DFS Visited: 0 to 3", graph.dfs(0, 3))
print("BFS Visited: 0 to 4", graph.bfs(0, 4))
print("BFS Visited: 0 to 3", graph.bfs(0, 3))
