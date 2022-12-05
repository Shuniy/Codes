# Upper Bound : O(n^2 * n!) time // Space : O(n * n!)

# Roughly : O(n * n!) time // O(n * n!) Space
def get_permutations(array):
    permutations = []

    permutations_helper(array, [], permutations)

    return permutations

def permutations_helper(array, current_permutations, permutations):
    if not len(array) and len(current_permutations):
        permutations.append(current_permutations)

    else:
        for i in range(len(array)):
            new_array = array[:i] + array[i + 1:] #O(n)
            new_permutation = current_permutations + [array[i]]  # O(n)
            permutations_helper(new_array, new_permutation, permutations)


# Time : O(n * n!)
# Space : O(n * n!)

# Total calls = n * n! + n! * n
def get_permutations(array):
    permutations = []

    permutations_helper(0, array, permutations)

    return permutations

def permutations_helper(i, array, permutations):
    if i == len(array) - 1:
        permutations.append(array[i:])
    else:
        for j in range(i, len(array)):
            array[i], array[j] = array[j], array[i]
            permutations_helper(i + 1, array, permutations)
            array[i], array[j] = array[j], array[i]
