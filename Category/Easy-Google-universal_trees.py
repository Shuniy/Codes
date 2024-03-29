"""
Easy
https://www.dailycodingproblem.com/blog/unival-trees/

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)

def count_universal_trees(root):
    if not root:
        return 0
    elif not root.left and not root.right:
        return 1
    elif not root.left and root.data == root.right.data:
        return 1 + count_universal_trees(root.right)
    elif not root.right and root.data == root.left.data:
        return 1 + count_universal_trees(root.left)

    child_counts = count_universal_trees(root.left) + count_universal_trees(root.right)
    current_node_count = 0
    if root.data == root.right.data and root.data == root.left.data:
        current_node_count = 1

    return current_node_count + child_counts

node_a = Node('0')
node_b = Node('1')
node_c = Node('0')
node_d = Node('1')
node_e = Node('0')
node_f = Node('1')
node_g = Node('1')
node_a.left = node_b
node_a.right = node_c
node_c.left = node_d
node_c.right = node_e
node_d.left = node_f
node_d.right = node_g

assert count_universal_trees(None) == 0
assert count_universal_trees(node_a) == 5
assert count_universal_trees(node_c) == 4
assert count_universal_trees(node_g) == 1
assert count_universal_trees(node_d) == 3
