# Time : O(n) Space : O(n)

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Recursive
def branchSums(root):
    sums = []
    calculateBranchSums(root, 0, sums)
    return sums

def calculateBranchSums(node, runningSum, sums):
    if node is None:
        return

    new_running_sum = runningSum + node.value
    if node.left is None and node.right is None:
        sums.append(new_running_sum)
        return

    calculateBranchSums(node.left, new_running_sum, sums)
    calculateBranchSums(node.right, new_running_sum, sums)
