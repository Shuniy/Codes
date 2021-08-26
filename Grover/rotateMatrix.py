"""
Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
bytes, write a method to rotate the image by 90 degrees. Can you do this in place?
Hints: #51, # 100
"""
from copy import deepcopy
# new matrix transpose
# time : O(n**2) : space : O(n**2)
def transpose(matrix, n):
    new = [[0] * n] * n
    for i in range(n):
        for j in range(n):
            new[i][j] = matrix[j][i]

    return new

# Inplace : time : O(n**2) | space : O(1)
def transpose(matrix, n, diagnal):
    if diagnal == 1:
        for i in range(n):
            for j in range(i + 1, n):
                swap(matrix, i, j)
    else:
        for i in range(n):
            for j in range(n - 1 - i):
                matrix[i][j], matrix[n - 1- j][n - i - 1] = matrix[n - j - 1][n - i - 1], matrix[i][j]

    return matrix

def swap(arr, i, j):
    arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

def rotateBy90(matrix, n):
    # Inplace transpose swap
    matrix = transpose(matrix, n, diagnal=1)
    # Now swapping Column
    for i in range(n):
        for j in range(n - 2):
            matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]

    return matrix

def rotateBy180(matrix, n):
    for i in range(n - 2):
        for j in range(n):
            matrix[i][j], matrix[n - i - 1][n - j - 1] = matrix[n - i - 1][n - j - 1], matrix[i][j]

    return matrix

def rotateBy270(matrix, n):
    matrix = transpose(matrix, n, diagnal = 2)
    for i in range(n):
        for j in range(n - 2):
            matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]

    return matrix

def rotateMatrix(matrix, degrees, n):
    arr = deepcopy(matrix)
    if not arr:
        return arr

    if degrees == 360:
        return arr

    if degrees == 90:
        return rotateBy90(arr, n)

    if degrees == 180:
        # or you can rotate matrix 2 times by 90 degrees
        return rotateBy180(arr, n)

    if degrees == 270:
        # either rotate by 90 three times
        # or rotate by 180 and then 90
        # or transpose with other diagnal and swap column
        return rotateBy270(arr, n)

def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=' ')
        print()

matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]

print('Original Matrix')
printMatrix(matrix)

print('rotate by 90 degrees')
printMatrix(rotateMatrix(matrix, 90, 4))
print('rotate by 180 degrees')
printMatrix(rotateMatrix(matrix, 180, 4))
print('rotate by 270 degrees')
printMatrix(rotateMatrix(matrix, 270, 4))
# print('rotate by 360 degrees')
# printMatrix(rotateMatrix(matrix, 360, 4))
