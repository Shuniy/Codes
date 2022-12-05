"""
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palin­
drome. A palindrome is a word or  phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

EXAMPLE
Input:  Tact  Coa
Output:  True  (permutations:  "taco  cat",  "atco  eta",  etc.)
Hints: #106, #121, #134, #136

"""

# Check if string is Palindrome
# Time : O(n) : Space : O(1)
def palindromePermutation(string):
    if not string:
        return True

    string = string.strip().replace(' ', '')

    i, j = 0, len(string) - 1
    while i < j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    return True

# However, we have to check if string can be palindrome or note
# For that we have to confirm one thing that almost all the characters
# should occur even number of times
# and the unique character should only occur once if odd

# Time : O(n) : Space : O(n)
def palindromePermutation(string):
    hashmap = dict()
    for item in string:
        if item == " ":
            continue
        if item not in hashmap:
            hashmap[item] = 1
            continue

        if hashmap[item] == 0 :
            hashmap[item] += 1
        elif hashmap[item] == 1:
            hashmap[item] -= 1

    return not list(hashmap.values()).count(1) > 1

print(palindromePermutation("taco  cat"))
print(palindromePermutation("tacdaso  cdaat"))
print(palindromePermutation("atco  eta"))
print(palindromePermutation("atco  cta"))
print(palindromePermutation("atco  etaa"))
