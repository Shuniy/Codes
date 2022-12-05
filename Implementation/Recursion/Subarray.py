def subarrays(arr):
    output = []
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            output.append(arr[i: j + 1])
            
    return output

print(subarrays([1,2,3,4,5]))

def subarraysRecursion(arr):
    output = []
    subarraysRecursionHelper(arr, 0, 0 ,output)
    return output

def subarraysRecursionHelper(arr, start, end, outputArray):
    if end > len(arr):
        return
    
    if start > end:
        subarraysRecursionHelper(arr, 0, end + 1, outputArray)
        return
    
    outputArray.append(arr[start: end])
    subarraysRecursionHelper(arr, start + 1, end, outputArray)

print(subarraysRecursion([1,2,3,4]))