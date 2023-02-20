
def LongestSubstringkUniqueCharacters(string: str, k: int) -> int:
    i = 0
    maxLen = float("-inf")
    hashmap = {}
    for j in range(len(string)):
        if string[j] in hashmap:
           hashmap[string[j]] += 1
        else:
            hashmap[string[j]] = 1
        if len(hashmap) < k:
            continue
        elif len(hashmap) == k:
            maxLen = max(maxLen, j - i + 1)
        else:
            while len(hashmap) > k:
                if string[i] in hashmap:
                    hashmap[string[i]] -= 1
                    if hashmap[string[i]] <= 0:
                        del hashmap[string[i]]
                i += 1
        print(i, j)
    return maxLen
        

s = "aabacbebebe"
k = 3

print(LongestSubstringkUniqueCharacters(s, k))
