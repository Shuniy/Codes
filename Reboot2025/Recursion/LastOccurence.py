# Moving backward

def lastOccurence(arr, key):
    if arr[-1] == key:
        return len(arr) - 1
    
    result = lastOccurenceHelper(arr, len(arr) - 1, key)
    return result

def lastOccurenceHelper(arr, n, key):
    if not n:
        return -1
        
    if arr[n] == key:
        return n
    
    result = lastOccurenceHelper(arr, n - 1, key)
    return result if result != 1 else -1

# Moving forward

def lastOccurence(arr, key):
    if not len(arr):
        return -1
    
    lastIndex = lastOccurence(arr[1:], key)
    if lastIndex == -1:
        if arr[0] == key:
            return 0
        else:
            return -1
    else:
        return lastIndex + 1



arr = [1, 3, 5, 7, 6, 2, 11, 21, 7, 8, 9]
key = 7
result = lastOccurence(arr, key)
if result != -1:
    print("Last Occurence of element found at : ", result)
else:
    print("Element not found !")
arr = [1, 3, 5, 17, 6, 2, 11, 21, 17, 8, 9]
key = 7
result = lastOccurence(arr, key)
if result != -1:
    print("Last Occurence of element found at : ", result)
else:
    print("Element not found !")
