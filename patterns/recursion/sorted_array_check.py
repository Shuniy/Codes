def sortedArrayCheck(arr):
    if len(arr) <= 1:
        return True
    
    return arr[0] <= arr[1] and sortedArrayCheck(arr[1:])

arr = [1,2,3,4,5,0,5,6,7]
print(sortedArrayCheck(arr[:]))
arr = [1,2,3,4,5,5,6,7]
print(sortedArrayCheck(arr[:]))