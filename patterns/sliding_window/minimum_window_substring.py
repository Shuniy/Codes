def MinimumWindowSubstring(s: str, t: str):
    """
    Generate the minimum window substring of string s that contains all the characters in string t.

    Parameters:
    s (str): The input string to search within.
    t (str): The target string that should be contained in the minimum window substring.

    Returns:
    str: The minimum window substring of string s that contains all characters in string t.
    """
    i = 0
    hashmap = {}
    string = ""
    min_len = float("inf")
    for item in t:
        if item in hashmap:
            hashmap[item] += 1
        else:
            hashmap[item] = 1

    count = len(hashmap)
    for j, item in enumerate(s):
        if item in hashmap:
            hashmap[item] -= 1
            if hashmap[item] == 0:
                count -= 1
        if count == 0:
            while count == 0:
                if j - i + 1 < min_len:
                    min_len = min(min_len, j - i + 1)
                    string = s[i: j + 1]
                if s[i] in hashmap:
                    hashmap[s[i]] += 1
                    if hashmap[s[i]] == 1:
                        count += 1
                i += 1
    return string


S = "ADOBECODEBANC"
T = "ABC"
print(MinimumWindowSubstring(S, T))

S = "a"
T = "a"
print(MinimumWindowSubstring(S, T))

S = "a"
T = "aa"
print(MinimumWindowSubstring(S, T))
