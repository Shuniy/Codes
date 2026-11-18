
"""
There are two recursive approach to solve this problem
1. Keep track of the visited element
2. Swap the elements

"""

result = []

# Approach 1 , Keeping track of already included element
def permutationRecursionHelper1(arr, n, hashmap, visited):

    if len(hashmap) == n:
        result.append(hashmap[:])
        return
    
    for i in range(n):
        if(visited[i] == True):
            continue
        
        hashmap.append(arr[i])
        visited[i] = True
        permutationRecursionHelper1(arr, n, hashmap, visited)
        hashmap.pop()
        visited[i] = False

def permutationRecursion1(arr, n):
    permutationRecursionHelper1(arr, n, [], [False for _ in range(n)])

def permutationRecursion2(arr, n):
    permutationRecursionHelper2(arr, n, 0, [])

def permutationRecursionHelper2(arr, n, currentIndex, hashmap):
    
    if currentIndex == n:
        hashmap = arr[:]
        result.append(hashmap)
        return
        
    for i in range(currentIndex, n):
        arr[currentIndex], arr[i] = arr[i], arr[currentIndex]
        permutationRecursionHelper2(arr, n, currentIndex + 1, hashmap)
        arr[currentIndex], arr[i] = arr[i], arr[currentIndex]

arr = [1,2,3]
n = len(arr)
# Approach 1
permutationRecursion1(arr, n)
print(result)
result = []
# Approach 2
permutationRecursion2(arr, n)
print(result)

