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



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print ("Diameter of given binary tree is %d" % (diameter(root)))
