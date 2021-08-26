"""
One Away: There  are  three  types  of  edits  that  can be  performed  on  strings:  insert  a  character,
remove a character, or  replace a character. Given  two strings, write a  function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale,  ple  -> true
pales,  pale  -> true
pale,  bale  -> true
pale,  bake  -> false
Hints:#23, #97, #130
"""

# Conditions to cover
# Base Conditions
# if abs length difference greater than 1
# Other Conditions : if length difference is 1
# If inserted:
# Length difference should be 1 and no character should be replaced
# If deleted:
#  length difference should be 1 and no character should be replaced
# If lengths are equal then :
# No more than one character should be replaced

# time : O(n) : space : O(1)

def oneWay(string1, string2):
    m = len(string1)
    n = len(string2)

    if not m and not n:
        return True

    # checking for lengths, will also check for insertion and deletion
    if abs(m - n) > 1:
        return False

    # It means either insert is called or delete is called
    elif abs(m - n) == 1:
        string1 = set(string1)
        string2 = set(string2)
        if m < n:
            string1, string2 = string2, string1

        if len(string1.difference(string2)) > 1:
            return False
    # If lengths are equal and It means replace is called
    else:
        count = 0
        index = 0
        while index < m:
            if string1[index] != string2[index]:
                count += 1
            if count > 1:
                return False
            index += 1

    return True

print(oneWay('pale', 'ple'))
print(oneWay('pale', 'kle'))
print(oneWay('pales', 'pale'))
print(oneWay('pales', 'pake'))
print(oneWay('pale', 'bale'))
print(oneWay('pale', 'bake'))
