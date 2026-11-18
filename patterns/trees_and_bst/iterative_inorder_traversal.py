# Time : O(n)
# Space : O(1)

# Callback is for printing

def iterative_inorder_traversal(tree, callback):
    previous_node = None
    current_node = tree

    while current_node is not None:
        next_node = None
        if previous_node is None or previous_node == current_node.parent:
            if current_node.left is not None:
                next_node = current_node.left

            else:
                callback(current_node)
                next_node = current_node.right if current_node.right is not None else current_node.parent

        elif previous_node == current_node.left:
            callback(current_node)
            next_node = current_node.right if current_node.right is not None else current_node.parent
        # Or else
        elif previous_node == current_node.right:
            next_node = current_node.parent
            
        previous_node = current_node
        current_node = next_node
