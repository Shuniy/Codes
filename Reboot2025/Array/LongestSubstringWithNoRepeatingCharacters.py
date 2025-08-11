def lengthOfLongestSubstring(s: str) -> int:
    n = len(s)
    if n <= 1:
        return n

    if len(set(s)) == n:
        return n
    start = 0
    maxLength = 0
    hashmap = {}
    for i in range(n):
        if s[i] in hashmap:
            if hashmap[s[i]] < start:
                maxLength = max(maxLength, i - start + 1)
            else:
                start = hashmap[s[i]] + 1    
        else:
            maxLength = max(maxLength, i - start + 1)
        hashmap[s[i]] = i
        
    return maxLength


string = "abcabcbb"
print(f"Longest Common Substring, {lengthOfLongestSubstring(string)}")
