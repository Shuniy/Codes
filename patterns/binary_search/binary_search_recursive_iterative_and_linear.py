import time
import random

def linearSearch(arr, k):
    for i in range(len(arr)):
        if arr[i] == k:
            return i

    return "Not Found!"

def binarySearchIterative(arr, k):
    if not arr:
        return "Invalid Array!" 
    
    start = 0
    end = len(arr)
    
    while start <= end:
        mid = start + (end - start) // 2
        
        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            end = mid - 1
        else:
            start = mid + 1
    
    return "Not Found"


def binarySearchRecursiveHelper(arr, k, start, end):
    if start == end:
        return start
    
    if start > end:
        return "Not Found!"
    
    if arr[start] == k:
        return start
    
    if arr[end - 1] == k:
        return end - 1
    
    mid = start + (end - start) // 2
    
    if arr[mid] == k:
        return mid
    elif arr[mid] > k:
        return binarySearchRecursiveHelper(arr, k, start, mid - 1)
    else:
        return binarySearchRecursiveHelper(arr, k, mid + 1, end)

def binarySearchRecursive(arr, k):
    return binarySearchRecursiveHelper(arr, k, 0, len(arr))


arr = sorted([random.random() * 10 for _ in range(10000000)])
k = random.choice(arr)
print(k)

start = time.time()
print("Index of element in array (Iterative) is : ",
      binarySearchIterative(arr, k))
print("Time taken : ", time.time() - start)

start = time.time()
print("Index of element in array (Recursive) is : ",
      binarySearchRecursive(arr, k))
print("Time taken : ", time.time() - start)

start = time.time()
print("Index of element in array (Linear) is : ",
      linearSearch(arr, k))
print("Time taken : ", time.time() - start)
