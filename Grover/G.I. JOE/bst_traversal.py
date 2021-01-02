# Space : O(n) 
# Time : O(n)
def inorder_traversal(tree, array):
    if tree is not None:
        inorder_traversal(tree.left, array)
        array.append(tree.value)
        inorder_traversal(tree.right, array)

    return array


def preorder_traversal(tree, array):
    if tree is not None:
        array.append(tree.value)
        preorder_traversal(tree.left, array)
        preorder_traversal(tree.right, array)

    return array


def postorder_traversal(tree, array):
    if tree is not None:
        postorder_traversal(tree.left, array)
        postorder_traversal(tree.right, array)
        array.append(tree.value)

    return array
