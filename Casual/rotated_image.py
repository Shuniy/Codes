"""
Rotate anticlockwise 90 degree

1 way - Take an extra array

2 way - Map each element to its new position
Make sure you access right index

Easier way - inplace Take transpose
"""
# Reverse each row

N = 4

def rotateMatrix(mat):

    for row in range(N):
        start_col = 0
        end_col = N - 1
        while start_col < end_col:
            mat[row][start_col], mat[row][end_col] = mat[row][end_col], mat[row][start_col]
            start_col += 1
            end_col -=1

    for i in range(N):
        for j in range(N):
            if i < j:
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

def displayMatrix(mat):

    for i in range(0, N):

        for j in range(0, N):

            print(mat[i][j], end=' ')
        print("")

mat = [[0 for x in range(N)] for y in range(N)]

mat = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]

'''
# Test case 2
mat = [ [1, 2, 3 ],
        [4, 5, 6 ],
        [7, 8, 9 ] ]

# Test case 3
mat = [ [1, 2 ],
        [4, 5 ] ]
'''

rotateMatrix(mat)
displayMatrix(mat)
