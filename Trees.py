
class BinarySearchTree:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode:
                if currentNode.left is None:
                    currentNode.left = BinarySearchTree(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BinarySearchTree(value)
                    break
                else:
                    currentNode = currentNode.right
        return self

    def contains(self, value):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True
        return False

    def getMinValue(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value

    def delete(self, value, parentNode = None):
        currentNode = self
        while currentNode:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinValue()
                    currentNode.right.remove(currentNode.value, currentNode)
                elif parentNode is None:
                    if currentNode.left is None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right
                    else:
                        currentNode.value = None
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode is not None else currentNode.right
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right

class Node:
    def __init__(self, value) -> None:
        self.value = value 
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, value = None) -> None:
        self.root = Node(value) if value else None

    def insertRecursively(self, parent, node):
        if parent is None:
            return node

        if node.value < parent.value:
            parent.left = self.insertRecursively(parent.left, node)
        else:
            parent.right = self.insertRecursively(parent.right, node)

        return parent

    def insert(self, value):
        newNode = Node(value)
        if self.root is None:
            self.root = newNode
            return

        self.root = self.insertRecursively(self.root, newNode)

    def getMinValueNode(self, parent):
        currentNode = parent
        while currentNode:
            currentNode = currentNode.left

        return currentNode

    def deleteRecursively(self, parent, value):
        if parent is None:
            return None

        if value < parent.value:
            parent.left = self.deleteRecursively(parent.left, value)
        elif value > parent.value:
            parent.right = self.deleteRecursively(parent.right, value)
        else:
            if parent.left is None:
                temp = parent.right
                parent = None
                return temp
            elif parent.right is None:
                temp = parent.left
                parent = None
                return temp

            else:
                temp = self.getMinValueNode(parent.right)
                parent.value = temp.value
                parent.right = self.deleteRecursively(parent.right, temp.value)

        return parent

    def delete(self, value):
        if self.root is None:
            print('Nothing to Delete')
            return

        self.root = self.deleteRecursively(self.root, value)

def inOrderTraversal(root):
    if root:
        inOrderTraversal(root.left)
        print(root.value, end=' ')
        inOrderTraversal(root.right)

def preOrderTraversal(root):
    if root:
        print(root.value, end=' ')
        inOrderTraversal(root.left)
        inOrderTraversal(root.right)

def postOrderTraversal(root):
    if root:
        inOrderTraversal(root.left)
        inOrderTraversal(root.right)
        print(root.value, end=' ')

