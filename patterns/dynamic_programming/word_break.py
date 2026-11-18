def word_break(s: str, wordDict: list[str]) -> bool:
    """
    Checks if a given non-empty string can be broken into a space-separated sequence of words in the given dictionary.

    Args:
        s (str): The input string.
        wordDict (list[str]): A list of words.

    Returns:
        bool: True if the string can be broken into words in the dictionary, False otherwise.
    """
    return word_break_helper(s, wordDict, 0, {})

def word_break_helper(s: str, wordDict: list[str], index: int, hashmap: dict) -> bool:
    """
    A helper function for word_break.

    Args:
        s (str): The input string.
        wordDict (list[str]): A list of words.
        index (int): The current index in the string.

    Returns:
        bool: True if the string can be broken into words in the dictionary, False otherwise.
    """
    if index == len(s):
        return True
    
    if index in hashmap:
        return hashmap[index]

    for i in range(index, len(s)):
        if s[index: i + 1] in wordDict and word_break_helper(s, wordDict, i + 1, hashmap):
            hashmap[index] = True
            return hashmap[index]

    hashmap[index] = False
    return hashmap[index]

# test cases
print(word_break("leetcode", ["leet", "code"]))
print(word_break("applepenapple", ["apple", "pen"]))
print(word_break("catsanddog", ["cats", "dog", "sand", "and", "cat"]))
print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))
print(word_break("applepenapple", ["apple", "pen", "applepen"]))
print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))
print(word_break("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
