class AdjNode:
    def __init__(self, value):
        """
        Initialize a new AdjNode with the given value.

        Parameters
        ----------
        value : int
            The value to be stored in this node.

        Attributes
        ----------
        vertex : int
            The value of this node.
        next : AdjNode or None
            The next node in the adjacency list, or None if this is the last
            node in the list.
        """
        self.vertex = value
        self.next = None

class Graph:
    def __init__(self, vertices: int):
        """
        Initialize a new Graph with the given number of vertices.

        Parameters
        ----------
        vertices : int
            The number of vertices in this graph.

        Attributes
        ----------
        vertices : int
            The number of vertices in this graph.
        graph : list of AdjNode or None
            The adjacency list, where each index represents a vertex in the
            graph and the value is the head of a linked list of adjacent nodes.
            If a vertex has no adjacent nodes, the value will be None.
        """
        self.vertices = vertices
        self.graph = [None] * self.vertices

    def add_edge(self, src, dest):
        """
        Add an edge between two vertices in the graph.

        This function will add an edge between the source (src) and destination
        (dest) vertices in the graph. The graph is undirected, so an edge from
        src to dest will also be added from dest to src.

        Parameters
        ----------
        src : int
            The source vertex of the edge.
        dest : int
            The destination vertex of the edge.
        """
        node = AdjNode(dest)
        node.next = self.graph[src]
        self.graph[src] = node

        node = AdjNode(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def print_agraph(self):
        """
        Print the adjacency list representation of the graph.

        This function will print the adjacency list representation of the graph.
        The output will be a series of lines, each representing a vertex in the
        graph. Each line will start with the vertex number, followed by a colon,
        and then a list of adjacent vertices, each separated by an arrow (->).
        If a vertex has no adjacent vertices, the line will simply be a vertex
        number followed by a colon.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        for i in range(self.vertices):
            print("Vertex " + str(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print()



if __name__ == "__main__":
    V = 5

    # Create graph and edges
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)

    graph.print_agraph()