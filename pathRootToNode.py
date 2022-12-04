
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)


def print_arr(arr):
    if not arr or arr.__len__() == 0:
        return

    counter = arr.__len__() - 1

    while counter >= 1:
        print(str(arr[counter]), end=" -> ")
        counter = counter-1

    print(arr[0])

def is_leaf_node(node):
    if node and not node.left and not node.right:
        return True
    else:
        return False

def print_leaf_to_root_paths(root, arr):
    if not root:
        return

    arr.append(root)

    if is_leaf_node(root):
        print_arr(arr)

    if root.left:
        print_leaf_to_root_paths(root.left, arr)

    if root.right:
        print_leaf_to_root_paths(root.right, arr)
    arr.pop()


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.left = Node(8)
root.right.left.right = Node(9)
print_leaf_to_root_paths(root, [])
