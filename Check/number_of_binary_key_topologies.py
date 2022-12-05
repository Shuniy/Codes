# Number of Binary Tree Topologies
# Mathemcatical  = n * (2n)! / (n! * (n + 1)!) // Catalan Number
# Space : O(n) // about n calls

# Finding time complexity form code is to hard but it is as mathematical

# Too many recursive calls and redundant recursive calls
# Use memoization

# Time : O(n^2)
# Space : O(n)

# Can be done iteratively and recursively like we use memoization in fibonacci series

# Naive
# Time : O(n * (2n)! / (n! * (n + 1)!)) // Not exactly but around
# Space : O(n)
def number_of_binary_trees_topologies(n):
    if n == 0:
        return 1

    number_of_trees = 0
    for left_tree_size in range(n):
        right_tree_size = n - 1 - left_tree_size
        number_of_left_trees = number_of_binary_trees_topologies(left_tree_size)
        number_of_right_trees = number_of_binary_trees_topologies(right_tree_size)

        number_of_trees += number_of_left_trees * number_of_right_trees

    return number_of_trees

# Memoization
# Time : O(n^2)
# Space :O(n) // includes recursive and cache
def number_of_binary_trees_topologies_memo(n, cache = {0:1}):
    if n in cache:
        return cache[n]
    
    number_of_trees = 0
    for left_tree_size in range(n):
        right_tree_size = n - 1 - left_tree_size
        number_of_left_trees = number_of_binary_trees_topologies_memo(
            left_tree_size, cache)
        number_of_right_trees = number_of_binary_trees_topologies_memo(
            right_tree_size, cache)

        number_of_trees += number_of_left_trees * number_of_right_trees
    cache[n] = number_of_trees
    return number_of_trees


# Iterative
# Space : O(n) // includes cache only
# Time : O(n^2)

def number_of_binary_trees_topologies(n):
    cache = [1]
    for i in range(1, len(n)):
        number_of_trees = 0
        for left in range(i):
            right = i - 1 - left
            number_of_left_trees = cache[left]
            number_of_right_trees = cache[right]
            number_of_trees = number_of_left_trees * number_of_right_trees
        cache.append(number_of_trees)

    return cache[n]