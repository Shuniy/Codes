import numpy as np

"""
TAKE REFERENCE OF DFS HERE !!!

In-order Traversal
In this traversal method, the left subtree is visited first, then the root and later the right sub-tree. 
We should always remember that every node may represent a subtree itself.
If a binary tree is traversed in-order, the output will produce sorted key values in an ascending order.
Algorithm
Until all nodes are traversed −
Step 1 − Recursively traverse left subtree.
Step 2 − Visit root node.
Step 3 − Recursively traverse right subtree.


In this traversal method, the root node is visited first, then the left subtree and finally the right subtree.
We start from A, and following pre-order traversal, we first visit A itself and then move to its left subtree B. B is also traversed pre-order. The process goes on until all the nodes are visited. The output of pre-order traversal of this tree will be −

A → B → D → E → C → F → G
Algorithm
Until all nodes are traversed −
Step 1 − Visit root node.
Step 2 − Recursively traverse left subtree.
Step 3 − Recursively traverse right subtree.


Post-order Traversal
In this traversal method, the root node is visited last, hence the name. First we traverse the left subtree, then the right subtree and finally the root node.
We start from A, and following Post-order traversal, we first visit the left subtree B. B is also traversed post-order. The process goes on until all the nodes are visited. The output of post-order traversal of this tree will be −

D → E → B → F → G → C → A

Algorithm
Until all nodes are traversed −
Step 1 − Recursively traverse left subtree.
Step 2 − Recursively traverse right subtree.
Step 3 − Visit root node.

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


Tree = Tree("apple")
Tree.getRoot().setLeftChild(node("banana"))
Tree.getRoot().setRightChild(node("cherry"))
Tree.getRoot().getLeftChild().setLeftChild(node("dates"))

visitOrder = list()
stack = np.Stack()
node = Tree.getRoot()
stack.push(node)
print(f"""visit_order {visitOrder} stack : {stack}""")

if node.hasLeftChild():
    node = node.getLeftChild()
    stack.push(node)
print(f"""visit_order {visitOrder} stack : {stack}""")

# Pre-order traversal using loop
# If confused check the cpp implementation you have done recursively
# that is easy to understand


def preOrder(Tree):
    visitOrder = list()
    stack = np.Stack()
    node = Tree.getRoot()
    stack.push(node)
    node = stack.top()
    visitOrder.append(node.getValue())
    count = 0
    loop_limit = 7
    while(node and count < loop_limit):
        print(f"""
        loop count : {count}
        current node : {node}
        stack : {stack}
        """)
        count += 1
        if node.hasLeftChild():
            node = node.getLeftChild()
            stack.push(node)
            node = stack.pop()
            visitOrder.append(node.getValue())
        else:
            stack.pop()
            if not stack.is_empty():
                node = stack.top()
            else:
                node = None
    return visitOrder


node = Tree.getRoot()


def printInorder(node):
    if node:
        printInorder(node.getLeftChild())
        print(node.getValue())
        printInorder(node.getRightChild())


def printPreorder(node):
    if node:
        print(node.getValue())
        printInorder(node.getLeftChild())
        printInorder(node.getRightChild())


def printPostorder(node):
    if node:
        printInorder(node.getLeftChild())
        printInorder(node.getRightChild())
        print(node.getValue())
