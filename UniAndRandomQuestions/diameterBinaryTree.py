class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
#Complexity O(n*h)
def height(root):
    if root == None:
        return 0
    lh = height(root.left)
    rh = height(root.right)
    return 1 + max(lh, rh)

def diameter(root):
    if root == None:
        return 0
    option1 = height(root.left) + height(root.right)
    option2 = diameter(root.left)
    option3 = diameter(root.right)
    return max(option1, max(option2, option3))

# Complexity can be improved by getting diameter and heigth of left and right together
# O(n) because every node does constant time
# Or by storing the heigths in an array

def height1(root, ans):
    if (root == None):
        return 0
    leftHeight = height1(root.left, ans)

    rightHeight = height1(root.right, ans)
    ans[0] = max(ans[0], 1 + leftHeight + rightHeight)

    return 1 + max(leftHeight, rightHeight)

def diameter1(root):
    if (root == None):
        return 0
    ans = []
    heightOfTree = height1(root, ans)
    return ans[0]

def diameter2(root):
    if root == None:
        output = [0,0]
        output[0] = 0
        output[1] = 0
        return output
    lo = diameter2(root.left)
    ro = diameter2(root.right)
    height = 1 + max(lo[0], ro[0])
    option1 = lo[0] + ro[0]
    option2 = lo[1]
    option3 = ro[1]
    diameter = max(option1, max(option2, option3))
    output = [0,0]
    output[0] = height
    output[1] = diameter
    return output

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
#print ("Diameter of given binary tree is %d" % (diameter(root)))
#print("Diameter of given binary tree is %d" % (diameter1(root)))
print("Diameter of given binary tree is %d" % (diameter2(root)[1]))
