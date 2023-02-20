
def LongestSubstringWithoutReapeatingCharacters(string: str) -> int:
    i = 0
    maxLen = float("-inf")
    hashmap = {}
    for j in range(len(string)):
        if string[j] in hashmap:
            hashmap[string[j]] += 1
        else:
            hashmap[string[j]] = 1
        if len(hashmap) == j - i + 1:
            maxLen = max(maxLen, j - i + 1)
        elif len(hashmap) < j - i + 1:
            while len(hashmap) < j - i + 1:
                if string[i] in hashmap:
                    hashmap[string[i]] -= 1
                    if hashmap[string[i]] == 0:
                        del hashmap[string[i]]
                i += 1
        else:
            continue
    return maxLen

string =  "abcabcbb"
print(LongestSubstringWithoutReapeatingCharacters(string))

string =  "bbbbbbbbb"
print(LongestSubstringWithoutReapeatingCharacters(string))

string = "pwwkew"
print(LongestSubstringWithoutReapeatingCharacters(string))
