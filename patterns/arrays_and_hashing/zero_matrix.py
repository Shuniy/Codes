"""
Zero Matrix: Write  an  algorithm such  that if an  element in an MxN  matrix is 0,  its entire row and
column are set to 0.
Hints:#17, #74, #702
"""
from copy import deepcopy

# Time : O(n**2) | Space : O(n**2) | O(1) depends on copy
def zeroMatrix(matrix):
    arr = deepcopy(matrix)
    m = len(arr)
    n = len(arr[0])
    zeroLocations = set()

    for i in range(m):
        for j in range(n):
            if arr[i][j] == 0:
                zeroLocations.add((i, j))

    for location in zeroLocations:
        ii, jj = location

        for i in range(m):
            arr[i][jj] = 0

        for j in range(n):
            arr[ii][j] = 0

    print('Location of Zeroes : ', zeroLocations)
    return arr

def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=' ')
        print()

matrix = [[1,2,3,4], [5,6,7,8], [9,0,11,12], [13,14,15,0]]

print('Original Matrix')
printMatrix(matrix)

print('Zero Matrix')
print(printMatrix(zeroMatrix(matrix)))
