"""
Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other.
Hints: #7, #84, #722, #737
"""

# Time : O(nlogn) : Space : O(1)
# Check if different lengths and check if whitespaces are significant
def checkPermutation(string1, string2):
    if len(string1) != len(string2):
        return False

    return sorted(string1) == sorted(string2)

# Time : O(n) : Space : O(n)
def checkPermutation(string1, string2):
    if len(string1) != len(string2):
        return False

    hashmap = dict()

    for item in string1:
        if item in hashmap:
            hashmap[item] += 1
        else:
            hashmap[item] = 1

    for item in string2:
        if item in hashmap:
            hashmap[item] -= 1
            if hashmap[item] < 0:
                return False
        else:
            return False

    return True

print(checkPermutation('dog', 'god'))
print(checkPermutation('dog', 'gode'))
print(checkPermutation('dog    ', 'gode'))
print(checkPermutation('dog    ', 'gode           '))
