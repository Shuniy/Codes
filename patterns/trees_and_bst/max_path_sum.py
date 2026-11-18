# Time : O(n)
# Space : O(logn) 

def max_path_sum(tree):
    _, max_sum = find_max_sum(tree)
    return max_sum

def find_max_sum(tree):
    if tree is None:
        return (0, 0)

    left_max_sum_as_branch, left_max_path_sum = find_max_sum(tree.left)
    right_max_sum_as_branch, right_max_path_sum = find_max_sum(tree.right)

    max_child_sum_as_branch = max(left_max_sum_as_branch, right_max_sum_as_branch)

    value = tree.value

    max_sum_as_branch = max(max_child_sum_as_branch + value, value)
    max_sum_as_rootnode = max(left_max_sum_as_branch + value + right_max_sum_as_branch, max_sum_as_branch)

    max_path_sum = max(left_max_path_sum, right_max_path_sum, max_sum_as_rootnode)

    return (max_sum_as_branch, max_path_sum)