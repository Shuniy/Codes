def search_2d_matrix(arr, target):
    m = len(arr)
    n = len(arr[0])

    i = 0
    j = n - 1
    while i < m and j >= 0:
        if target == arr[i][j]:
            return True
        if arr[i][-1] < target:
            i += 1
            continue
        j -= 1
    return False


arr = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 16
assert search_2d_matrix(arr, target) == True

arr = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 119
assert search_2d_matrix(arr, target) == False
