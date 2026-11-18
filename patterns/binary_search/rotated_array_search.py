def rotatedArraySearch(arr, k):
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        mid = start + (end - start) // 2
        
        if arr[mid] == k:
            return mid
        
        if arr[start] <= arr[mid]:
            if k >= arr[start] and k <= arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if k >= arr[mid] and k <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1
    
    return -1

arr = [4,5,6,7,8,9,0,1,2,3]
k = 0
print(rotatedArraySearch(arr, k))