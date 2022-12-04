def sortArray(arr):
    if len(arr) <= 1:
        return arr
    lastElement = arr[-1]
    restElementSorted = sortArray(arr[0:len(arr) - 1])
    return findCorrectPosition(restElementSorted, lastElement)

def findCorrectPosition(arr, element):
    if len(arr) <= 0:
        return [element]
    if arr[-1] <= element:
        return arr + [element]
    else:
        return findCorrectPosition(arr[0: len(arr) - 1], element) + [arr[-1]]

arr = [1,0,3,4,9,8,7,6,2,1,-1]
print("Sorted Array, ", sortArray(arr))