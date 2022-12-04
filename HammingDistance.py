"""
Hamming Distance :
In information theory, the Hamming distance between two strings of equal length is the number of positions at which the corresponding 
symbols are different.
  Calculate the hamming distance of the two strings

   Args:
       str1(string), str2(string): Strings to be used for finding the hamming distance
    Returns:
       int: Hamming Distance
"""


def hammingDistance(str1, str2):
    if len(str1) != len(str2):
        return None
    distance = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1
    return distance


print("Pass" if (10 == hammingDistance('ACTTGACCGGG', 'GATCCGGTACA')) else "Fail")
print("Pass" if (1 == hammingDistance('shove', 'stove')) else "Fail")
print("Pass" if (None == hammingDistance('Slot machines', 'Cash lost in me')) else "Fail")
print("Pass" if (9 == hammingDistance('A gentleman', 'Elegant men')) else "Fail")
print("Pass" if (2 == hammingDistance('0101010100011101', '0101010100010001')) else "Fail")
