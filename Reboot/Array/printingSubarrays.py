def subarrays(arr):
    if not arr:
        return []
    
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            print(arr[i:j + 1])

def subarraysRecursiveHelper(arr, start, end):
    if end == len(arr):
        return
    
    if start > end:
        subarraysRecursiveHelper(arr, 0, end + 1)
    else:
        print(arr[start: end + 1])
        subarraysRecursiveHelper(arr, start + 1, end)

def subarraysRecursive(arr):
    subarraysRecursiveHelper(arr, 0, 0)

arr = [10,20,30,40,50,60,70,80,90]
# subarrays(arr)
subarraysRecursive(arr)