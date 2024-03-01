import random


class TreeNode(object):
    def __init__(self, value, leftChild=None, rightChild=None, parent=None) -> None:
        self.value = value
        self.leftChild: TreeNode | None = leftChild
        self.rightChild: TreeNode | None = rightChild
        self.parent: TreeNode | None = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.leftChild or self.rightChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def spliceOut(self):
        pass

    def findSuccessor(self):
        pass

    def findMin(self):
        pass

    def replaceNodeData(self):
        pass


class BinaryTree:
    def __init__(self, initialItems: list = []) -> None:
        self.root: TreeNode | None = None
        for item in initialItems:
            self.insert(item)

    def getRoot(self):
        if self.root:
            return self.root
        return None

    def _insert(self, value, currentNode: TreeNode | None) -> TreeNode | None:
        if currentNode is None:
            currentNode = TreeNode(value)
            return currentNode

        if value <= currentNode.value:
            currentNode.leftChild = self._insert(value, currentNode.leftChild)
        elif value > currentNode.value:
            currentNode.rightChild = self._insert(
                value, currentNode.rightChild)
        return currentNode

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
            return

        self.root = self._insert(value, self.getRoot())

    def _delete(self, value, currentNode: TreeNode | None) -> TreeNode | None:
        if currentNode is None:
            return currentNode

        if value < currentNode.value:
            currentNode.leftChild = self._delete(value, currentNode.leftChild)
        elif value > currentNode.value:
            currentNode.rightChild = self._delete(
                value, currentNode.rightChild)
        else:
            if currentNode.leftChild is None:
                temp = currentNode.rightChild
                currentNode = None
                return temp
            elif currentNode.rightChild is None:
                temp = currentNode.leftChild
                currentNode = None
                return temp
            temp = self._minValue(currentNode.rightChild)
            currentNode.value = temp
            currentNode.rightChild = self._delete(temp, currentNode.rightChild)

        return currentNode

    def delete(self, value):
        if not self.root:
            return
        self.root = self._delete(value, self.getRoot())
        return value

    def _inorder(self, currentNode: TreeNode | None, result: list):
        if currentNode:
            self._inorder(currentNode.hasLeftChild(), result)
            result.append(currentNode.value)
            self._inorder(currentNode.hasRightChild(), result)

    def inorder(self):
        result = []
        self._inorder(self.getRoot(), result)
        return result

    def _preorder(self, currentNode: TreeNode | None, result: list):
        if currentNode:
            result.append(currentNode.value)
            self._preorder(currentNode.hasLeftChild(), result)
            self._preorder(currentNode.hasRightChild(), result)

    def preorder(self):
        result = []
        self._preorder(self.getRoot(), result)
        return result

    def _postorder(self, currentNode: TreeNode | None, result: list):
        if currentNode:
            self._postorder(currentNode.hasLeftChild(), result)
            self._postorder(currentNode.hasRightChild(), result)
            result.append(currentNode.value)

    def postorder(self):
        result = []
        self._inorder(self.getRoot(), result)
        return result

    def _minValue(self, currentNode: TreeNode | None):
        if currentNode is None:
            return None

        if currentNode.leftChild is None:
            return currentNode.value

        return self._minValue(currentNode.leftChild)

    def minValue(self):
        if not self.root:
            return None

        return self._minValue(self.getRoot())

    def _maxValue(self, currentNode: TreeNode | None):
        if currentNode is None:
            return None

        if currentNode.rightChild is None:
            return currentNode.value

        return self._maxValue(currentNode.rightChild)

    def maxValue(self):
        if not self.root:
            return None

        return self._maxValue(self.getRoot())


size = int(input("Enter the size of the array: "))
array = [random.randint(0, size) for _ in range(size)]
binaryTree = BinaryTree(array)
print("Inorder traversal: ", binaryTree.inorder())
print("Preorder traversal: ", binaryTree.preorder())
print("Postorder traversal: ", binaryTree.postorder())
# Get minimum
print("Minimum Value: ", binaryTree.minValue())
# Get maximum
print("Maximum Value: ", binaryTree.maxValue())
# delete value
print("Deleting value: ", binaryTree.delete(random.choice(array)))
print("Inorder traversal: ", binaryTree.inorder())
# delete value
print("Deleting value: ", binaryTree.delete(random.choice(array)))
print("Inorder traversal: ", binaryTree.inorder())
# delete value
print("Deleting value: ", binaryTree.delete(random.choice(array)))
print("Inorder traversal: ", binaryTree.inorder())
