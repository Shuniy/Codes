def MinimumWindowSubstring(s: str, t: str) -> str:
    i = 0
    hashmap = {}
    string = ""
    minLen = float("inf")
    for item in t:
        if item in hashmap:
            hashmap[item] += 1
        else:
            hashmap[item] = 1
    
    count = len(hashmap)
    for j in range(len(s)):
        if s[j] in hashmap:
            hashmap[s[j]] -= 1
            if hashmap[s[j]] == 0:
                count -= 1
        if count == 0:
            while count == 0:
                if j - i + 1 < minLen:
                    minLen = min(minLen, j - i + 1)
                    string = s[i: j + 1]
                if s[i] in hashmap:
                    hashmap[s[i]] += 1
                    if hashmap[s[i]] == 1:
                        count += 1
                i += 1
    return string    

s = "ADOBECODEBANC"
t = "ABC"
print(MinimumWindowSubstring(s, t))

s = "a" 
t = "a"
print(MinimumWindowSubstring(s, t))

s = "a"
t = "aa"
print(MinimumWindowSubstring(s, t))
