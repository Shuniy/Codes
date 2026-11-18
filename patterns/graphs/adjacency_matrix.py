class Graph:
    def __init__(self, vertices: int):
        """
        Create a new instance of Graph with the given number of vertices.

        :param int vertices: The number of vertices the graph should have.
        :return: A new instance of Graph
        :rtype: Graph
        """
        self.vertices = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        
    def add_edge(self, v1, v2):
        if v1 == v2:
            return
        self.graph[v1][v2] = 1
        self.graph[v2][v1] = 1

    def remove_edge(self, v1, v2):
        if v1 == v2:
            return
        self.graph[v1][v2] = 0
        self.graph[v2][v1] = 0

    def __len__(self):
        return self.vertices

    def print_matrix(self):
        for row in self.graph:
            for val in row:
                print(val, end=" ")
            print()


def main():
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)

    g.print_matrix()


if __name__ == '__main__':
    main()        