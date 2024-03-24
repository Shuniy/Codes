
def LongestSubstringWithoutReapeatingCharacters(string: str):
    """
    Find the length of the longest substring without repeating characters in the given string.

    Args:
    string (str): The input string

    Returns:
    int: The length of the longest substring without repeating characters
    """
    i = 0
    max_len = float("-inf")
    hashmap = {}
    for j, item in enumerate(string):
        if item in hashmap:
            hashmap[item] += 1
        else:
            hashmap[item] = 1

        if len(hashmap) == j - i + 1:
            max_len = max(max_len, j - i + 1)
        elif len(hashmap) < j - i + 1:
            while len(hashmap) < j - i + 1:
                if string[i] in hashmap:
                    hashmap[string[i]] -= 1
                    if hashmap[string[i]] == 0:
                        del hashmap[string[i]]
                i += 1
            if len(hashmap) == j - i + 1:
                max_len = max(max_len, j - i + 1)
        else:
            continue
    return max_len


S = "abcabcbb"
print(LongestSubstringWithoutReapeatingCharacters(S))

S = "bbbbbbbbb"
print(LongestSubstringWithoutReapeatingCharacters(S))

S = "pwwkew"
print(LongestSubstringWithoutReapeatingCharacters(S))
