
def PickToys(toys: str, k: int) -> int:
    i = 0
    hashmap = {}
    maxToys = float("-inf")
    for j in range(len(toys)):
        if toys[j] in hashmap:
            hashmap[toys[j]] += 1
        else:
            hashmap[toys[j]] = 1

        if len(hashmap) < k:
            continue
        elif len(hashmap) == k:
            maxToys = max(maxToys, j - i + 1)
        else:
            while len(hashmap) > k:
                if toys[i] in hashmap:
                    hashmap[toys[i]] -= 1
                    if hashmap[toys[i]] == 0:
                        del hashmap[toys[i]]
                i += 1        
    return maxToys

toys = 'abaccab'
k = 2
print(PickToys(toys, k))