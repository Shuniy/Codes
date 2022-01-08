# Time : O(n * m)
# Space : O(n * m)

def levenshteinDistance(str1, str2):
    if len(str1) <= 0:
        return
    
    if type(str1) is not str or type(str2) is not str:
        str1 = str(str1)
        str2 = str(str2)

    edits = [x for x in range(len(str) + 1) for y in range(len(str2) + 1)]

    for i in range(1, len(str2) + 1):
        edits[i][0] = edits[i - 1][0] + 1

    for i in range(1, len(str2) + 1):
        for j in range(1, len(str1) + 1):
            if str2[i - 1] == str[j - 1]:
               edits[i][j] = edits[i - 1][j - 1]
            else:
                edits[i][j] = 1 + min(edits[i - 1][j - 1], edits[i][j - 1], edits[i - 1][j])

    return edits[-1][-1]

# Time : O(n * m)
# Space : O(min(n, m))
def levenshteinDistance(str1, str2):
    small = str1 if len(str1) < len(str2) else str2

    big = str1 if len(str1) >= len(str2) else str2

    evenEdits = [x for x in range(len(small) + 1)]

    oddEdits = [None for x in range(len(small) + 1)]

    for i in range(1, len(big) + 1):
        if i % 2 == 1:
            currentEdits = oddEdits
            previousEdits = evenEdits
        else:
            currentEdits = evenEdits
            previousEdits = oddEdits
        currentEdits[0] = i

        for j in range(1, len(small) + 1):
            if big[i - 1] == small[j - 1]:
                currentEdits[j] = previousEdits[j - 1]
            else:
                currentEdits[j] = 1 + min(previousEdits[j - 1], previousEdits[j], currentEdits[j - 1])
    return evenEdits[-1] if len(big) % 2 == 0 else oddEdits[-1]
