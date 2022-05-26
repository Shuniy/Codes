def validate_bst_helper(tree, min_value, max_value):
    if tree is None:
        return True
    if tree.value < min_value or tree.value >= max_value:
        return False

    left_is_valid = validate_bst_helper(tree.left, min_value, tree.value)
    right_is_valid = validate_bst_helper(tree.right, tree.value, max_value)

    return left_is_valid and right_is_valid

def validate_bst(tree):
    return validate_bst_helper(tree, float('-inf'), float('inf'))