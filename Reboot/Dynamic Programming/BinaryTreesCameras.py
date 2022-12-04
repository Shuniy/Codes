# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        hasCamera = False
        isMonitored = False
        # Current root node neither has camera nor it is monitored
        return self.helper(root, hasCamera, isMonitored)

    # Case1: if node has camera-> Then we will add camera at node, return 1 + minimum number of cameras
    # required from left subtree + minimum number of cameras required for right subtree

    # Case2: node doesnt have camera, but is monitored by some child, then we will only
    # need minimum number of cameras required in left subtree + minimum number of cameras
    # required for right subtree

    # Case3: node doesn't have camera, and children also doesnt have camera, which means
    # node is not monitored either, So, We will add camera at node and return 1 + minimum
    # number of cameras required in left subtree with minimum number of cameras required in
    # right subtree

    # POINTS TO REMEMBER:-
    # Function will always return minimum number of cameras required for tree, starting from
    # provided node, inititally, we dont know it has camera or not and is monitored or not
    # so we will pass hasCamera and isMonitored as False for every single node, unless,
    # for the case, in which we are adding camera to the node, in that case,
    # left and right node will automatically be monitored, so isMonitored will be true
    # but still, we hasCamera for left and right is False, as left and right can have camera or cannot, it depends
    # Other independent cases, which doesnt depend on whether the node has camera or not or monitored or not are
    # First, we will add the camera at Node
    # Second, we will add camera either at left or right child of the node, as one is enough
    # We are not adding at both because, we are adding camera at our will, going from root node to end nodes or leaf nodes which are null
    # and considering all the possible cases
    # In, the end, we need minimum, of all the three cases

    # Hypothesis -> Will always return the minimum Cameras required
    def helper(self, root, hasCamera, isMonitored) -> int:
        # if no node, then no camera needed
        if root is None:
            return 0
        # ************************** BASE CASES *************************************************
        # now, if node has camera, then we need that camera
        # so we return that camera with minimum cameras in left and right subtree
        # and we will not add camera to the immediate left and right node
        # as they will be monitored by node itself
        if hasCamera:
            # CASE - 1
            return 1 + self.helper(root=root.left, hasCamera=False, isMonitored=True) + self.helper(root=root.right, hasCamera=False, isMonitored=True)

        # no camera is present at node, which means node is monitored somehow
        if isMonitored:
            # This case is tricky, as if node is monitored, then, either we can have cameras
            # at both left or right or only at one of them,
            # in any case we have to find the minimum at both left or right, as our function,
            # returns the minimum number of cameras from the subtree starting from the node
            # CASE - 2
            # No camera at node, but child have camera, so we need cameras from left and right
            childWithCam = self.helper(root.left, hasCamera=False, isMonitored=False) + \
                self.helper(root.right, hasCamera=False, isMonitored=False)
            childWithNoCam = 1 + self.helper(root.left, hasCamera=False, isMonitored=True) + self.helper(
                root.right, hasCamera=False, isMonitored=True)
            # Now, we dont, need both cases, only the case which has minimum cameras
            return min(childWithCam, childWithNoCam)

        # ************************************* INDUCTION ****************************************
        # Now, all the cases, when adding camera at out will
        # Try, adding camera at node or root
        rootHasCam = 1 + self.helper(root.left, hasCamera=False, isMonitored=True) + \
            self.helper(root.right, hasCamera=False, isMonitored=True)
        # No camera at root or node
        # Now, we have two cases, either add camera to left or right node
        # First, adding camera to left node
        leftHasCam = float("inf")
        if root.left is not None:
            leftHasCam = self.helper(root.left, hasCamera=True, isMonitored=False) + \
                self.helper(root.right, hasCamera=False, isMonitored=False)
        # Second, Now adding camera to right node, not left
        rightHasCam = float("inf")
        if root.right is not None:
            rightHasCam = self.helper(root.left, hasCamera=False, isMonitored=False) + \
                self.helper(root.right, hasCamera=True, isMonitored=False)
        # Now, we want minimum of all the cases
        return min(rootHasCam, leftHasCam, rightHasCam)

# Memoization
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        hasCamera = False
        isMonitored = False
        return self.helper(root, hasCamera, isMonitored)

    # Hypothesis -> Will always return the minimum Cameras required
    def helper(self, root, hasCamera, isMonitored) -> int:
        # if no node, then no camera needed
        if root is None:
            return 0
        # ************************** BASE CASES *************************************************
        if hasCamera:
            # CASE - 1
            return 1 + self.helper(root=root.left, hasCamera=False, isMonitored=True) + self.helper(root=root.right, hasCamera=False, isMonitored=True)
        # no camera is present at node, which means node is monitored somehow
        if isMonitored:
            # CASE - 2
            # No camera at node, but child have camera, so we need cameras from left and right
            childWithCam = self.helper(root.left, hasCamera=False, isMonitored=False) + \
                self.helper(root.right, hasCamera=False, isMonitored=False)
            childWithNoCam = 1 + self.helper(root.left, hasCamera=False, isMonitored=True) + self.helper(
                root.right, hasCamera=False, isMonitored=True)
            # REMEMBER, THIS IS NOT THE FINAL ANSWER, IT IS JUST A BASE CASE
            return min(childWithCam, childWithNoCam)

        # REMEMBER, THIS IS TRICKY,
        # DONT ADD, THIS BASE CASE FOR MEMOIZATION, BEFORE OTHER POSSIBLE BASE CASES
        # BECAUSE, THEY HAVE THEIR OWN RECURSIVE CALLS AND THEIR OWN OPERATIONS TO PERFORM
        if root.val != 0:
            return root.val
        # ************************************* INDUCTION ****************************************
        # Now, all the cases, when adding camera at out will
        # Try, adding camera at node or root
        rootHasCam = 1 + self.helper(root.left, hasCamera=False, isMonitored=True) + \
            self.helper(root.right, hasCamera=False, isMonitored=True)
        # Now, we have two cases, either add camera to left or right node
        leftHasCam = float("inf")
        if root.left is not None:
            leftHasCam = self.helper(root.left, hasCamera=True, isMonitored=False) + \
                self.helper(root.right, hasCamera=False, isMonitored=False)
        rightHasCam = float("inf")
        if root.right is not None:
            rightHasCam = self.helper(root.left, hasCamera=False, isMonitored=False) + \
                self.helper(root.right, hasCamera=True, isMonitored=False)
        # Now, we want minimum of all the cases
        # REMEMBER: - THIS MINIMUM IS THE FINAL ANSWER REQUIRED, SO MEMOIZE THIS
        root.val = min(rootHasCam, leftHasCam, rightHasCam)
        return root.val


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def solve(node):
            # Keep track, of all the cases
            # CASE-1 = ans[0] means, all nodes below i,e subtrees of left and right are monitored, not the current node
            # CASE-2 = ans[1] means, all, the nodes below are monitored and current node is monitored,
            # but current node doesnt have the camera
            # CASE-3 = ans[2] means, all, the nodes below are monitored and current node is monitored,
            # because current node has the camera

            # BASE CASE
            # if node is null, that means
            # CASE-1: Not possible as current is null and there will be no left and right also
            # CASE-2: Not possible as current and left and right doesnt exist
            # Case-3: Adding camera to watch current node which is null, So, we can place the camera at null
            # but what is the use of adding camera at null, so we will ignore this case, and to ignore this
            # we will add "infinity" here, as later min will automaticlly ignore this case
            if node is None:
                return 0, 0, float('inf')
            # Now, getting case results for left and right
            L = solve(node.left)
            R = solve(node.right)
            # Now, To get minimum, we will add up cases
            # CASE-1: Means all nodes left and right are monitored but not the node
            # So, to cover this case, the child node left and right must me in CASE-2
            # So, we will take the values of CASE-2 from LEFT AND RIGHT
            dp0 = L[1] + R[1]
            # To cover CASE-2 without placing a camera here, the children of this node must be in CASE-1 or
            # CASE-3, and at least one of those children must be in CASE-3.
            dp1 = min(L[2] + min(R[1:]), R[2] + min(L[1:]))
            # To cover the CASE-3 when placing a camera here, the children can be in any CASE.
            dp2 = 1 + min(L) + min(R)
            return dp0, dp1, dp2
            # Now, Solve for Every Node, but ignore the case in which current node is not monitored
        return min(solve(root)[1:])


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.minimumCameras = 0
        # Again, Distinguish with cases
        # 1 = node is not monitored
        # 2 = node is monitored, but no camera
        # 3 = has camera

        def dfs(root):
            # Null node, is always not monitored, so consider it monitored
            # no need of adding camera there at null
            if root is None:
                return 2
            # Get Status of left and right
            getLeft = dfs(root.left)
            getRight = dfs(root.right)
            # If any of the child node is not monitored, we will add camera
            # 1 means node not monitored, below it means left or right is not monitored
            if getLeft == 1 or getRight == 1:
                # we will add the camera to parent or root
                self.minimumCameras += 1
                # Now the camera is added, So return 3 for parent node or root
                return 3
            # if any of the child node is monitored and has camera,
            # the current node is monitored, no need of camera
            # 3 Means node has camera, below it means left or right already has camera
            elif getLeft == 3 or getRight == 3:
                # 2 Means node is monitored, but has no camera
                # returning 2 for root as child has camera, so no need of camera here and parent or root is monitored
                return 2
            else:
                # Else, case means not monitored by any child, means child is not even monitored or have camera
                return 1
        # If root node is not monitored, means child node is also not monitored and has no camera
        # So, we will add camera at root
        if dfs(root) == 1:
            self.minimumCameras += 1
        return self.minimumCameras
