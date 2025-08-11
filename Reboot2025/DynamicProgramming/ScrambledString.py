def ScrambledString(s1: str, s2: str) -> bool:
    """
    A function to check if one string is a scrambled version of another string.

    Args:
        s1 (str): The first string.
        s2 (str): The second string.

    Returns:
        bool: True if `s1` is a scrambled version of `s2`, False otherwise.
    """
    return ScrambledStringHelper(s1, s2)

def ScrambledStringHelper(s1: str, s2: str) -> bool:
    """
    A function to check if one string is a scrambled version of another string.

    Args:
        s1 (str): The first string.
        s2 (str): The second string.

    Returns:
        bool: True if `s1` is a scrambled version of `s2`, False otherwise.
    """

    if len(s1) != len(s2):
        return False

    if s1 == s2:
        return True
    
    for k in range(1, len(s1)):
        if ScrambledStringHelper(s1[:k], s2[:k]) and ScrambledStringHelper(s1[k:], s2[k:]):
            return True

        if ScrambledStringHelper(s1[:k], s2[len(s2) - k:]) and ScrambledStringHelper(s1[k:], s2[:len(s2) - k]):
            return True

    return False

# test cases
print(ScrambledString("abcde", "caebd"))
print(ScrambledString("great", "rgeat"))
print(ScrambledString("great", "rgeta"))
print(ScrambledString("abc", "bca"))
print(ScrambledString("abc", "bac"))
print(ScrambledString("a", "a"))
print(ScrambledString("abb", "bba"))
print(ScrambledString("abc", "bca"))