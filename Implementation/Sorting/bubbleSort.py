# In bubble sort, every iteration, will place the largest element at end
# Time Complexity = O(n^2)
# Space Complexity = O(1)

def bubbleSort(arr):
    if len(arr) <= 1:
        return arr
    
    for i in range(len(arr) - 1):
        swapped = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break
            
    return arr

# Bubble sort can be done by recursion,
# by turning every loop to recursion
# Method 1
# turning ith loop in recursive
def bubbleSortRecursion1Helper(arr, n):
    if n == 1:
        return arr
    
    for j in range(n - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            
    return bubbleSortRecursion1Helper(arr, n - 1)

def bubbleSortRecursion1(arr):
    return bubbleSortRecursion1Helper(arr, len(arr))

# Bubble sort can be done by recursion,
# by turning every loop to recursion
# Method 2
# turning ith loop in recursive
# turning jth loop in recursive
def bubbleSortRecursion2Helper(arr, n, j):
    if n <= 1:
        return arr
    
    if j == n - 1:
        bubbleSortRecursion2Helper(arr, n - 1, 0)
        return arr
    
    if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j +  1], arr[j]
        
    return bubbleSortRecursion2Helper(arr, n, j + 1)


def bubbleSortRecursion2(arr):
    return bubbleSortRecursion2Helper(arr, len(arr), 0)


arr = [1, 6, 32, 111, 85, 16, 765, 89, 33, 2, 54, 57, 54, 222, 24, 32, 6, 57, 45, 234, 34, 5, 346, 242, 31, 21, 6, 5787, 769, 65, 34, 543, 7, 3, 324, 236, 2]
# arr = [1,2,3,4,5,6,7,8,9]
# print(bubbleSort(arr[:]))
# print(bubbleSortRecursion1(arr[:]))
print(bubbleSortRecursion2(arr[:]))
