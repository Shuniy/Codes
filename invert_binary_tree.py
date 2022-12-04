# Time : O(n)
# Space : O(d)
def invert_binary_tree(tree):
    if tree is not None:
        tree.left, tree.right = tree.right, tree.left
        invert_binary_tree(tree.left)
        invert_binary_tree(tree.right)
    return tree

# Time : O(n)
# Space : O(n)
def invert_binary_tree_bfs(tree):
    queue = [tree]

    while len(queue):
        current = queue.pop(0)
        if current is None:
            continue
        tree.left, tree.right = tree.right, tree.left

        queue.append(current.left)
        queue.append(current.right)

