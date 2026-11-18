listSubarrays = []

def subarrays(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(i, n):
            print(arr[i: j + 1])
            listSubarrays.append(arr[i:j + 1])

    return

def subarraysRecursionHelper(arr, start, end):
    if end == len(arr):
        return
    elif start > end:
        subarraysRecursionHelper(arr, 0, end + 1)
    else:
        listSubarrays.append(arr[start : end+1])    
        subarraysRecursionHelper(arr, start + 1, end)

def subarraysRecursion(arr):
    subarraysRecursionHelper(arr, 0, 0)

arr = [1,2,3,4,5]
subarrays(arr)
print(listSubarrays)
listSubarrays = []
subarraysRecursion(arr)
print(listSubarrays)
