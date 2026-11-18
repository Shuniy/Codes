def sortedArraySearch(arr, k):
    if not arr:
        return [None, None]
    
    m = len(arr)
    n = len(arr[0])
    
    if k < arr[0][0] or k > arr[m - 1][n - 1]:
        return [-1, -1]
    
    i = 0
    j = n - 1
    
    while i <= m - 1 and j >= 0:
        if k == arr[i][j]:
            return [i, j]
        
        elif k < arr[i][j]:
            j -= 1
        else:
            i += 1
    
    return [-1, -1]


arr = [[10,20,30,40],[15,25,35,45],[27,29,37,48],[32,33,39,50]]
k = 32
print(sortedArraySearch(arr, k))
