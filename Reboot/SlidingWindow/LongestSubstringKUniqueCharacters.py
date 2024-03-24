def LongestSubstringkUniqueCharacters(string: str, k: int):
    """
    Calculate the length of the longest substring with at most k unique characters.

    Parameters:
    string (str): The input string
    k (int): The maximum number of unique characters allowed in the substring

    Returns:
    int: The length of the longest substring with at most k unique characters
    """
    i = 0
    max_len = float("-inf")
    hashmap = {}
    for j, item in enumerate(string):
        if item in hashmap:
            hashmap[item] += 1
        else:
            hashmap[item] = 1

        if len(hashmap) < k:
            continue
        if len(hashmap) == k:
            max_len = max(max_len, j - i + 1)
        else:
            while len(hashmap) > k:
                if string[i] in hashmap:
                    hashmap[string[i]] -= 1
                    if hashmap[string[i]] == 0:
                        del hashmap[string[i]]
                i += 1
            if len(hashmap) == k:
                max_len = max(max_len, j - i + 1)
    return max_len


S = "aabacbebebe"
K = 3

print(LongestSubstringkUniqueCharacters(S, K))
