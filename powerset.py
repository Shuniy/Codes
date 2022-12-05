
# Iterative
# Time : O(2^n * (n/2))
# Space : O(2^n * (n/2))
def powerset(array):
    # Initializing with empty set
    subsets = [[]]

    for ele in array:
        for i in range(len(subsets)):
            current_subset = subsets[i]
            subsets.append(current_subset + [ele])

    return subsets

# Recursive
# Time : O(2^n * (n/2))
# Space : O(2^n * (n/2))
def powerset(array, index = None):
    if index is None:
        index = len(array) - 1
    elif index < 0:
        return [[]]
    
    ele = array[index]

    subsets = powerset(array, index - 1)

    for i in range(len(subsets)):
        current_subset = subsets[i]
        subsets.append(current_subset + [ele])
    return subsets

