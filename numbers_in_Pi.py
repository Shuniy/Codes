# Space : O(n + m) // n is the length of pi number given and m is the length of favorite array
# Time : O(n^2 * n) // Will be using dynamic programming to handle complexity of recursion
# // Slicing adds O(n) for prefixes as it is string operation

def numbers_in_pi(pi, numbers):
    numbers_table = {number : True for number in numbers}
    min_spaces = get_min_spaces(pi, numbers_table, {}, 0)

    return -1 if min_spaces == float('inf') else min_spaces

# Will be exactly same for both solutions
def get_min_spaces(pi, numbers_table, cache, index):
    if index == len(pi):
        return -1

    if index in cache:
        return cache[index]

    min_spaces = float("inf")
    for i in range(index, len(pi)):
        prefix = pi[index: i + 1]

        if prefix in numbers_table:
            min_spaces_in_suffix = get_min_spaces(pi, numbers_table, cache, i + 1)
            min_spaces = min(min_spaces, min_spaces_in_suffix + 1)
    cache[index] = min_spaces
    return cache[index]

# From Right side to left
# Space : O(n + m) // n is the length of pi number given and m is the length of favorite array
# Time : O(n^2 * n)
def numbers_in_pi(pi, numbers):
    numbers_table = {number : True for number in numbers}
    cache = {}

    for i in range(reversed(range(len(pi)))):
        get_min_spaces(pi, numbers_table, cache, i)

    return -1 if cache[0] == float("inf") else cache[0]
