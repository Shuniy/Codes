from collections import deque
"""
Implemented using queue
"""

class node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def setLeftChild(self, node):
        self.left = node

    def setRightChild(self, node):
        self.right = node

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def hasLeftChild(self):
        return self.left != None

    def hasRightChild(self):
        return self.right != None

    def _repr_(self):
        return f"Node ({self.getValue()})"

    def _str_(self):
        return f"Node ({self.getValue()})"


class Tree(object):
    def __init__(self, value):
        self.root = node(value)

    def getRoot(self):
        return self.root
# PRINT TREE
    def _repr_(self):
        level = 0
        q = Queue()
        visitOrder = list()
        node = self.getRoot()
        q.enq((node, level))
        while len(q) > 0:
            node, level = q.deq()
            if node == None:
                visitOrder.append(("<empty", level))
                continue
            visitOrder.append((node, level))
            if node.hasLeftChild():
                q.enq((node.getLeftChild(), level + 1))
            else:
                q.enq((None, level + 1))
        s= "Tree \n"
        previous_level = -1
        for i in range(len(visitOrder)):
            node, level = visitOrder[i]
            if level == previous_level:
                s += " | " + str(node)
            else:
                previous_level = level
        return s

Tree = Tree("apple")
Tree.getRoot().setLeftChild(node("banana"))
Tree.getRoot().setRightChild(node("cherry"))
Tree.getRoot().getLeftChild().setLeftChild(node("dates"))

#Just for reference
q = deque()
q.appendleft('apple')
q.appendleft('banana')
print(q)

# Making my own class for queue and dequeue

class Queue():
    def __init__(self):
        self.q = deque()
    def enq(self, value):
        self.q.appendleft(value)
    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None
    def _len_(self):
        return len(self.q)
    def _repr_(self):
        if len(self.q) > 0:
            s = "< enqueue here >\n ________________________\n"
            s += "\n______________________\n".join([str(item) for item in self.q])
            s += "\n_______________________\n <dequeue here >"
            return s
        else:
            return "<queue is empty>"

visitOrder = list()
q = Queue()

node = Tree.getRoot()
q.enq(node)
print(q)
node = q.deq()
visitOrder.append(node)
if node.hasLeftChild():
    q.enq(node.getLeftChild())
if node.hasRightChild():
    q.enq(node.getRightChild())

print(f"""visit order : {visitOrder}""")
print(q)
node = q.deq()
visitOrder.append(node)
# Above is the thing use for loop for above or recursion

def bfs(tree):
    q = Queue()
    visitOrder = list()
    node = Tree.getRoot()
    q.enq(node)
    while len(q) > 0:
        node = q.deq()
        visitOrder.append(node)
        if node.hasLeftChild():
            q.enq(node.getLeftChild())
        if node.hasRightChild():
            q.enq(node.getRightChild())
    return visitOrder
