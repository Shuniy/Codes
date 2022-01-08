"""
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
Hints: #44, #7 7 7, #732
"""

# Time : O(nlogn) : Space : O(1) || O(n)
def isUnique(string):
    string = sorted(string)
    for i in range(1, len(string)):
        if string[i] == string[i - 1]:
            return False
    return True

# Time: O(n) : Space : O(n)
def isUnique(string):
    hashmap = dict()

    for item in string:
        if item in hashmap:
            return False
        else:
            hashmap[item] = 1

    return True

# Time : O(n) : Space : O(1)
# So, in this approach, what we do is, we maintain a bitwise
# So, what happens is we set the bit of that character to 1,
# So, whenever a new item comes it set a different bit to 1
# but when a same character come, it will try to set the already set bit
# that where we take the `and` of the bits and it will return a greater value than 0
# because , bit is already set to 1 and 1 & 1 is 1, so and will return some value
def isUnique(string):
    # we create a checker which is actually a bitwise
    checker = 0

    for item in string:
        # we get the ascii of the item
        item = ord(item)
        # then we check the `and` of ascii value with checker
        if (checker & (1 << item)) > 0:
            return False
        # we store the or of the current checker and the item
        checker |= 1 << item

    return True

print(isUnique('#73'))
