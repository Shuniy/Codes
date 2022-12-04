# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #DFS
        if root is None:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left, right)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #BFS
        if root is None:
            return 0

        result = 0
        queue = collections.deque([])
        queue.append(root)

        while queue:
            result += 1
            nextLevel = []
            for ptr in queue:
                if ptr.left:
                    nextLevel.append(ptr.left)

                if ptr.right:
                    nextLevel.append(ptr.right)

            queue = nextLevel

        return result
