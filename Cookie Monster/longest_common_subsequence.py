# Time : O(nm * min(n, m))
# Space : O(nm * min(n, m))
# min(n, m) for string operations that is concatenation

from typing import Sequence


def longest_common_subsequence(str1, str2):
    lcs = [[[] for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]

    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str2[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + [str[i - 1]]
            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1], key = len)

    return lcs[-1][-1]
            
# Here we are not doing concatenation and only storing letter and indices
# Then we will be backtracking

# Time : O(nm)
# Space : O(nm)
def longest_common_subsequence(str1, str2):
    # lcs = [None if first letter is not being used else we are storing that number, 
    # length of current lcs, 
    # ith index
    # jth index]

    lcs = [[[None, 0, None, None] for x in range(len(str1) + 1)] for y in range(len(str2) + 1)]

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str2[i - 1] == str2[j - 1]:
                lcs[i][j] = [str2[i - 1], lcs[i - 1][j - 1][1] + 1, i - 1, j - 1]
            else:
                if lcs[i - 1][j][1] > lcs[i][j - 1][1]:
                    lcs[i][j] = [None, lcs[i - 1][j][1], i - 1, j]
                else:
                    lcs[i][j] = [None, lcs[i][j - 1][1], i, j - 1]

    return build_sequence(lcs)

def build_sequence(lcs):
    sequence = []

    i = len(lcs) - 1
    j = len(lcs[0]) - 1

    while i != 0 and j != 0:
        current_entry = lcs[i][j]

        if current_entry[0] is not None:
            sequence.append(current_entry[0])

        i = current_entry[2]
        j = current_entry[3]

    return list(reversed(sequence))