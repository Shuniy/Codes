
def sortArrayRecursion(arr):
    if len(arr) == 1:
        return arr
    
    firstElemenet = [arr[0]]
    restSortedArray = sortArrayRecursion(arr[1:])
    newArray = firstElemenet + restSortedArray
    
    for i in range(1, len(newArray)):
        if newArray[i - 1] > newArray[i]:
            newArray[i - 1], newArray[i] = newArray[i], newArray[i - 1]
        
    return newArray

arr = [111,9,8,7,6,56,34,5,6,7,8,9,4,3,2,19,57,8,12,96,6,0,8,9,45,2,21,44,36,9,5,5,34,46,69,67,635,241,223,4243,6568,1,0,76,543,21,76,43,54,2,3,52,5,234,35,43,7,68,7,95,3,54324,23,4,64,84,75,5,4,3,3,2,1,0,11]

print(sortArrayRecursion(arr))

def sortAnArray(arr):
    n = len(arr)
    return sortAnArrayHelper(arr, n)

def sortAnArrayHelper(arr, n):
    if n <= 1:
        return arr
    lastElement = arr.pop()
    sortedRestArray = sortAnArrayHelper(arr, n - 1)
    return insertNum(sortedRestArray, lastElement)

def insertNum(arr, num):
    if len(arr) == 0:
        arr.append(num)
        return arr
    
    if arr[-1] <= num:
        arr.append(num)
        return arr
    
    lastElement = arr.pop()
    arr = insertNum(arr, num)
    arr.append(lastElement)
    return arr

print("Sorted Array", sortAnArray(arr))