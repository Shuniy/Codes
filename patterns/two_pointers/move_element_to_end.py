# Time : O(n)
# Space : O(1)
def MoveElementToEnd(arr, target):
    n = len(arr)
    if target not in arr:
        return []
    if n <= 1:
        return arr

    i = 0
    j = n - 1

    while i < j:
        if arr[i] != target:
            i += 1
        if arr[j] == target:
            j -= 1
        if arr[i] == target:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    return arr

arr = [2,4,1,2,5,2,7,1,8,2,2,4,9,1,8,2,1,2]
print(MoveElementToEnd(arr, 2))