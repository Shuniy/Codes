# Time : O(n) Space : O(n)

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Recursive

def branchSums(root):
    depths = []
    calculateBranchdepths(root, 0, depths)
    return depths


def calculateBranchdepths(node, current, depths):
    if node is None:
        return

    current = current + 1
    if node.left is None and node.right is None:
        current += 0
        depths.append(current)
        return

    calculateBranchdepths(node.left, current, depths)
    calculateBranchdepths(node.right, current, depths)
