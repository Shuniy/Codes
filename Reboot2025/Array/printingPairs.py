import random

def printingPairs(arr, k):
    hashmap = set()
    
    for item in arr:
        if item in hashmap:
            if k - item in hashmap:
                print(item, k - item)
        else:
            hashmap.add(item)

arr = [random.randint(1, 10) for _ in range(1000)]
k = random.choice(arr) + random.choice(arr)
printingPairs(arr, k)

def printAllPairs(arr):
    if not arr:
        return None
    
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            print(arr[i], arr[j])

arr = [10,20,30,40,50,60,70,80,90]
printAllPairs(arr)