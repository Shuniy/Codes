import random

# Time Complexity = O(n + b)
# Space Complexity = O(max(array))

def countingSort(arr):
    largest = float("-inf")
    
    for item in arr:
        largest = max(largest, item)
        
    hashmap = [0 for _ in range(largest + 1)]
    
    for item in arr:
        hashmap[item] += 1
        
    arr = []
    for index, item in enumerate(hashmap):
        if item != 0:
            while item:
                arr.append(index)
                item -= 1
                
    return arr

arr = [random.randint(0, 9999) for _ in range(100)]
print(countingSort(arr[:]))