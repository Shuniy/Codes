class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None
        self.height: int = 1


class AVLTree:
    def __init__(self) -> None:
        self.root: TreeNode | None = None

    def getRoot(self):
        return self.root

    def _insert(self, node: TreeNode | None, value):
        # Step 1 - Perform the normal BST
        if not node:
            node = TreeNode(value)
            return node
        elif value < node.value:
            node.left = self._insert(node.left, value)
        else:
            node.right = self._insert(node.right, value)
        # Step 2 - Update the height of the parent or ancestor node
        node.height = 1 + max(self.getHeight(node.left),
                              self.getHeight(node.right))

        # Step 3 - Get the balance factor
        balance = self.getBalance(node)

        # Step 4 - if node is unbalanced, need to handle the 4 cases
        # LL, RR, LR, RL
        # If balance  is 0 and 1 its fine
        # if balance is less -1, right skewed
        # if balance is greater 1, left skewed

        # LL, means tree is completely left skewed
        if node.left and balance > 1 and value < node.left.value:
            return self.rightRotate(node)

        # RR, means tree is completely right skewed
        if node.right and balance < -1 and value > node.right.value:
            return self.leftRotate(node)

        # LR, means tree has left node and element will be added to right
        if node.left and balance > 1 and value > node.left.value:
            # first rotate parent to left and then ancestor to right
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)

        # RL, means tree has right node and element will be added to left
        if node.right and balance < -1 and value < node.right.value:
            # first rotate parent to right and then ancestor to left
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        return node

    def insert(self, value):
        node = self.getRoot()
        if not node:
            self.root = TreeNode(value)
            return
        self.root = self._insert(node, value)
        return

    def _delete(self, node: TreeNode | None, value):
        # Perform standard bst delete
        if not node:
            return node
        if node.left and value < node.value:
            node.left = self._delete(node.left, value)
        elif node.right and value > node.value:
            node.right = self._delete(node.right, value)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            temp = self._getMin(node.right)
            node.value = temp
            node.right = self._delete(node.right, temp)

        if not node:
            return node

        # Step 2 - Update the height
        node.height = 1 + max(self.getHeight(node.right),
                              self.getHeight(node.left))

        # Step 3 - Get balance factor
        balance = self.getBalance(node)

        # Step 4 - Now balance
        # LL
        if node.left and balance > 1 and self.getBalance(node.left) >= 0:
            return self.rightRotate(node)

        # RR
        if node.right and balance < -1 and self.getBalance(node.right) <= 0:
            return self.leftRotate(node)

        # LR
        if node.left and balance > 1 and self.getBalance(node.left) < 0:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)

        # RL
        if node.right and balance < -1 and self.getBalance(node.right) > 0:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)

        return node

    def _getMin(self, node: TreeNode | None):
        if not node:
            return None

        if not node.left:
            return node.value

        return self._getMin(node.left)

    def getMin(self) -> TreeNode | None:
        return self._getMin(self.getRoot())

    def delete(self, value):
        node = self.getRoot()
        if not node:
            return node
        self.root = self._delete(node, value)
        return value

    def leftRotate(self, node: TreeNode):
        if not node:
            return node
        y = node.right
        if not y:
            return node
        # If we are left rotating, that means incoming elemet will be adding at
        # y.right
        T2 = y.left
        # Now rotating
        node.right = T2
        y.left = node
        node.height = 1 + max(self.getHeight(node.left),
                              self.getHeight(node.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def rightRotate(self, node: TreeNode):
        if not node:
            return node
        y = node.left
        if not y:
            return node
        # If we are left rotating, that means incoming element will be added to
        # y.left
        T2 = y.right
        # Now rotating
        node.left = T2
        y.right = node
        node.height = 1 + max(self.getHeight(node.left),
                              self.getHeight(node.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def getHeight(self, node: TreeNode | None):
        if not node:
            return 0

        return node.height

    def _preorder(self, node, result):
        if not node:
            return
        result.append(node.value)
        self._preorder(node.left, result)
        self._preorder(node.right, result)

    def preorder(self):
        result = []
        self._preorder(self.getRoot(), result)
        return result

    def _postorder(self, node, result):
        if not node:
            return

        self._postorder(node.left, result)
        self._postorder(node.right, result)
        result.append(node.value)

    def postorder(self):
        result = []
        self._postorder(self.getRoot(), result)
        return result

    def _inorder(self, node, result):
        if not node:
            return
        self._inorder(node.left, result)
        result.append(node.value)
        self._inorder(node.right, result)

    def inorder(self):
        result = []
        self._inorder(self.getRoot(), result)
        return result

    def getBalance(self, node: TreeNode | None):
        if not node:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)


avlTree = AVLTree()
avlTree.insert(10)
avlTree.insert(20)
avlTree.insert(30)
avlTree.insert(40)
avlTree.insert(50)
avlTree.insert(25)
print("Inorder: ", avlTree.inorder())
print("Preorder: ", avlTree.preorder())
print("Postorder: ", avlTree.postorder())
avlTree.delete(10)
avlTree.delete(25)
print("Inorder: ", avlTree.inorder())
print("Preorder: ", avlTree.preorder())
print("Postorder: ", avlTree.postorder())
