"""
Permutation is all about swapping elements
"""

# Method 1 -> Create hashmap and keep track of every visited element
# Permutation without repetition

def permutationHashmapHelper(arr, onePossible, visited):
    if len(onePossible) == len(arr):
        print(onePossible)
        return
    
    for i in range(len(arr)):
        if visited[i] == True:
            continue
        else:
            visited[i] = True
            onePossible.append(arr[i])
            permutationHashmapHelper(arr, onePossible, visited)
            visited[i] = False
            onePossible.pop()

def permutation1(arr):
    permutationHashmapHelper(arr, [], [False for _ in range(len(arr))])    


# Method 2 -> Swap elements inplace
# Permutation without repetition
def permutationSwapHelper(arr, currentIndex):
    if currentIndex == len(arr):
        print(arr)
        return
        
    for i in range(currentIndex, len(arr)):
        arr[currentIndex], arr[i] = arr[i], arr[currentIndex]
        permutationSwapHelper(arr, currentIndex + 1)
        arr[currentIndex], arr[i] = arr[i], arr[currentIndex]

def permutation2(arr):
    permutationSwapHelper(arr, 0)


# Permutation with repetition
def permutationWithRepetitionHelper(arr, currentIndex, hashmap):
    for i in range(len(arr)):
        hashmap[currentIndex] = arr[i]
        
        if currentIndex == len(arr) - 1:
            print(hashmap)
        else:
            permutationWithRepetitionHelper(arr, currentIndex + 1, hashmap) 

def permutationWithRepetition(arr):
    permutationWithRepetitionHelper(arr, 0, [None for _ in range(len(arr)) ])

arr = [1,2,3]
print("Permutation without repetition : Method 1 Hashmap : ")
permutation1(arr)
print("Permutation without repetition : Method 2 Swap : ")
permutation2(arr)
print("Permutation with Repetition : ")
permutationWithRepetition(arr)