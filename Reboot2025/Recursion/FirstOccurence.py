# Might take O(n^2)

def firstOccurence(arr, key):
    if not len(arr):
        return -1
        
    if arr[0] == key:
        return 0
    
    firstIndex = firstOccurence(arr[1:], key)
    return 1 + firstIndex if firstIndex != -1 else -1

arr = [1,3,5,7,6,2,11,21,7,8,9]
key = 7
result = firstOccurence(arr, key)
if result != -1:
    print("First Occurence of element found at : ", result)
else:
    print("Element not found !")
arr = [1, 3, 5, 17, 6, 2, 11, 21, 17, 8, 9]
key = 7
result = firstOccurence(arr, key)
if result != -1:
    print("First Occurence of element found at : ", result)
else:
    print("Element not found !")
