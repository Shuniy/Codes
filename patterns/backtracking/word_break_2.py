def word_break(s: str, word_dict: list[str]) -> list[str]:
    """
    Finds all possible ways to segment a string into words from a given dictionary.

    Args:
        s (str): The input string to be segmented.
        word_dict (list[str]): A list of words available for segmentation.

    Returns:
        list[str]: A list of all possible segmented paths, each represented as a space-separated string.
    """

    result = []
    word_break_helper(s, set(word_dict), 0, [], result)
    return result

def word_break_helper(s: str, word_dict: set[str], index: int, current: list[str], result: list[str]):
    """
    A recursive helper function for finding all possible ways to segment a string into words from a given dictionary.

    Args:
        s (str): The input string to be segmented.
        word_dict (set[str]): A set of words available for segmentation.
        index (int): The current starting index in the string for segmentation.
        current (list[str]): The current list of words forming a segmented path.
        result (list[str]): The list to store all possible segmented paths.

    Returns:
        None
    """

    if index == len(s):
        result.append(" ".join(current.copy()))
        return
    
    for i in range(index, len(s)):
        if s[index: i + 1] in word_dict:
            current.append(s[index: i + 1])
            word_break_helper(s, word_dict, i + 1, current, result)
            current.pop()


# test cases
print(word_break("catsanddog",  ["cat", "cats", "and", "sand", "dog"]))
print(word_break("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))
print(word_break("catsandog", ["cats","dog","sand","and","cat"]))
