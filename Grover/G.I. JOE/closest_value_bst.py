# N number of nodes, or d - depth of the d only in space complexity
# Average : O(log(n)), Space : Recursively: O(log(n)) and Worse Space : O(n)
# Space: Iteration : O(1)

# Average : Time : O(log(n)) Space: O(log(n))
# Worst : Time : O(n) Space: O(n)
def find_closest_value_in_bst_helper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value

    if target > tree.value:
        return find_closest_value_in_bst_helper(tree.right, target, closest)

    elif target < tree.value:
        return find_closest_value_in_bst_helper(tree.left, target, closest)

    return closest

# Recursively
def find_closest_value(tree, target):
    return find_closest_value_in_bst_helper(tree, target, float("inf"))

# Average : Time : O(log(n)) Space: O(1)
# Worst : Time : O(n) Space: O(1)
def find_closest_value_iterative(tree, target, closest):
    current_node = tree
    while current_node is not None:
        if abs(target - closest) > abs(target - current_node.value):
            closest = current_node.value
        if target < current_node.value:
            current_node = current_node.left
        elif target > current_node.value:
            current_node = current_node.right
        else:
            break
    return closest
