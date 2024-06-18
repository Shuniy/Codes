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
            new_array = array[:i] + array[i + 1:]  # O(n)
            new_permutation = current_permutations + [array[i]]  # O(n)
            permutations_helper(new_array, new_permutation, permutations)


arr = [1, 2, 3]
print(get_permutations(arr))
