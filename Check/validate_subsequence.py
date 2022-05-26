
def isSubSequence(string1, string2, m, n):
    if m == 0:
        return True
    if n == 0:
        return False

    if string1[m - 1] == string2[n - 1]:
        return isSubSequence(string1, string2, m - 1, n - 1)

    return isSubSequence(string1, string2, m, n - 1)


string1 = "gksrek"
string2 = "geeksforgeeks"

if isSubSequence(string1, string2, len(string1), len(string2)):
    print("Yes")
else:
    print("No")
