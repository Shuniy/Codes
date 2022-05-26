class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))

    # Time : O(V + E)
    # Space : O(V)
    def breadthFirstSearch(self, array):
        queue = [self]

        while len(queue) > 0:
            current = queue.pop(0)

            array.append(current.name)

            for child in current:
                queue.append(child)

        return array