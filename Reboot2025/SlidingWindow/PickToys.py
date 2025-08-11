
def PickToys(toys: str, k: int):
    """
    Counts the maximum number of toys that can be picked from the given string of toys,
    such that no more than k unique toys are picked consecutively.

    Args:
        toys (str): A string of toys, where each character represents a unique toy.
        k (int): The maximum number of unique toys that can be picked consecutively.

    Returns:
        int: The maximum number of toys that can be picked without exceeding the limit of k unique toys.
    """

    i = 0
    hashmap = {}
    max_toys = float("-inf")
    for j, item in enumerate(toys):
        if item in hashmap:
            hashmap[item] += 1
        else:
            hashmap[item] = 1

        if len(hashmap) < k:
            continue
        if len(hashmap) == k:
            max_toys = max(max_toys, j - i + 1)
        else:
            while len(hashmap) > k:
                if toys[i] in hashmap:
                    hashmap[toys[i]] -= 1
                    if hashmap[toys[i]] == 0:
                        del hashmap[toys[i]]
                i += 1
            if len(hashmap) == k:
                max_toys = max(max_toys, j - i + 1)
        return max_toys


TOYS = 'abaccab'
K = 2
print(PickToys(TOYS, K))
