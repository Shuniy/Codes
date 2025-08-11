def spiralPrint(arr):
    startRow = 0
    startCol = 0
    endRow = len(arr) - 1
    endCol = len(arr[0]) - 1
    
    while startRow <= endRow and startCol <= endCol:
        for col in range(startCol, endCol + 1):
            print(arr[startRow][col], end=" ")
        
        startRow += 1
        for i in range(startRow, endRow + 1):
            print(arr[i][endCol], end=" ")
        
        endCol -= 1
        for j in range(endCol, startCol - 1, -1):
            print(arr[endRow][j], end=" ")
            
        endRow -= 1
        for i in range(endRow, startRow - 1, -1):
            print(arr[i][startCol], end=" ")
            
        startCol += 1
        
arr = [[1,2,3,4],[5,6,7,8], [9,10,11, 12], [13,14,15,16]]
spiralPrint(arr)