# Recursive
# Time : O(2^(n + m)) // Not exactly but it is a rough idea
# Space : O(n + m)
def interweaving_strings(one, two, three):
    if len(three) != len(one) + len(two):
        return False

    return are_interwoven_recursive(one, two, three, 0, 0)

def are_interwoven_recursive(one, two, three, i, j):
    k = i + j
    if k == len(three): 
        return True

    if i < len(one) and one[i] == three[k]:
        if are_interwoven_recursive(one, two, three, i + 1, j):
            return True

    if j < len(two) and two[j] == three[k]:
        return are_interwoven_recursive(one, two, three, i, j + 1)

    return False

# Caching
# Time : O(nm)
# Space : O(nm + n + m) // (n + m) recursive call stack


def interweaving_strings(one, two, three):
    if len(three) != len(one) + len(two):
        return False

    cache = [[None for j in range(len(two) + 1)] for i in range(len(one) + 1)]
    return are_interwoven(one, two, three, 0, 0, cache)


def are_interwoven(one, two, three, i, j, cache):
    if cache[i][j] is not None:
        return cache[i][j]

    k = i + j
    if k == len(three):
        return True

    if i < len(one) and one[i] == three[k]:
        cache[i][j] = are_interwoven(one, two, three, i + 1, j, cache)
        if cache[i][j]: 
            return True

    if j < len(two) and two[j] == three[k]:
        cache[i][j] = are_interwoven(one, two, three, i, j + 1, cache)
        return cache[i][j]
    
    cache[i][j] = False
    return False
