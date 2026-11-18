# Easy way to do is make BST and do traversal, but don't do that

# Time : O(n^2)
# Space : O(n^2)
def same_bst(bst1, bst2):
    if len(bst1) != len(bst2) or bst1[0] != bst2[0] or sorted(bst1) != sorted(bst2):
        return False

    if len(bst1) == 0 and len(bst2) == 0:
        return True

    left_one = get_smaller(bst1)
    left_two = get_smaller(bst2)
    right_one = get_bigger_or_equal(bst1)
    right_two = get_bigger_or_equal(bst2)

    return same_bst(left_one, left_two) and same_bst(right_one, right_two)

def get_smaller(array):
    smaller = []

    for i in range(1, len(array)):
        if array[i] < array[0]:
            smaller.append(array[i])
    return smaller


def get_bigger_or_equal(array):
    bigger = []

    for i in range(1, len(array)):
        if array[i] >= array[0]:
            bigger.append(array[i])
    return bigger


# Optimal Space Complexity
# Time : O(n^2)
# Space : O(d) //d is the depth of binary search tree

def same_bst_optimal(bst1, bst2):
    if len(bst1) != len(bst2) or sorted(bst1) != sorted(bst2):
        return False

    if len(bst1) == 0 and len(bst2) == 0:
        return True

    return are_same_bsts(bst1, bst2, 0, 0, float('-inf'), float('inf'))

def are_same_bsts(bst1, bst2, root_index1, root_index2, min_val, max_val):
    if root_index1 == -1 or root_index2 == -1:
        return root_index1 == root_index2

    if bst1[root_index1] != bst2[root_index2]:
        return False

    left_root_index_one = get_index_of_first_smaller(bst1, root_index1, min_val)
    left_root_index_two = get_index_of_first_smaller(bst2, root_index2, min_val)
    right_root_index_one = get_index_of_first_bigger_equal(bst1, root_index1, max_val)
    right_root_index_two = get_index_of_first_bigger_equal(bst2, root_index2, max_val)

    current_value = bst1[root_index1]

    left_are_same = are_same_bsts(bst1, bst2, left_root_index_one, left_root_index_two, min_val, current_value)
    right_are_same = are_same_bsts(bst1, bst2, right_root_index_one, right_root_index_two, current_value, max_val)

    return left_are_same and right_are_same

    
def get_index_of_first_smaller(array, starting_index, min_val):
    for i in range(starting_index + 1, len(array)):
        if array[i] < array[starting_index] and array > min_val:
            return i
    return -1


def get_index_of_first_bigger_equal(array, starting_index, max_val):
    for i in range(starting_index + 1, len(array)):
        if array[i] >= array[starting_index] and array < max_val:
            return i
    return -1
