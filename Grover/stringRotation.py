"""
String Rotation: Assume you have a method isSubstring which checks if one word is a substring
of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").
Hints: #34, #88, # 7 04
"""

def isSubstring(string1, string2):
    # suppose it works in O(string1 + string2)
    pass

def stringRotation(string1, string2):
    # we see that if string2 is rotated then it will always be a substring of
    # 2 * string1
    # string1 = waterbottle string2 = erbottlewat, then string2 must be a substring
    # of waterbottlewaterbottle
    # we just have to check if it is substring of string1 or not

    if not string1:
        return False

    return isSubstring(string1 + string1, string2)


print(stringRotation(string1, string2))
