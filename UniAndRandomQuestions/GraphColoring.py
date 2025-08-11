class GraphColoring:
    def __init__(self) -> None:
        self.v = 4

    def isSafeToColor(self, v, graphMatrix, color, c):
        for i in range(self.v):
            if graphMatrix[v][i] == 1 and c == color[i]:
                return False
        return True

    def graphColorUtil(self, graphMatrix, m, color, v):
        if v == self.v:
            return True

        for i in range(1, m + 1):
            if self.isSafeToColor(v, graphMatrix, color, i):
                color[v] = i
                if self.graphColorUtil(graphMatrix, m, color, v + 1):
                    return True
                color[v] = 0

        return False

    def printColoringSolution(self, color):
        print("Color schema for vertices are: ")
        for i in range(self.v):
            print(color[i])

    def graphColoring(self, graphMatrix, m):
        color = [0]*(self.v)
        if not self.graphColorUtil(graphMatrix, m, color, 0):
            print("Color schema not possible")
            return False

        self.printColoringSolution(color)
        return True
