#Creating a binary tree

#Creating nodes using node class
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

#Tree class which has root Node and return the root node
class Tree(object):
    def __init__(self, value):
        self.root = node(value)

    def getRoot(self):
        return self.root
