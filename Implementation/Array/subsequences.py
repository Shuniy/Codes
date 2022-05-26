# Method 1 - Recursive
import math


def subsequencesHelper(arr, currentIndex, subsequence):
    
    if currentIndex > len(arr):
        return
    elif currentIndex == len(arr):
        if len(subsequence):
            print(subsequence)
    else:
        subsequencesHelper(arr, currentIndex + 1, [arr[currentIndex]] + subsequence)
        subsequencesHelper(arr, currentIndex + 1, subsequence)

def subsequences(arr):
    subsequencesHelper(arr, 0, [])


# Method 2 = Powerset
def subsequencesPowerSet(arr):
    setSize = len(arr)
    powerSetSize = (int)(math.pow(2, setSize))
    
    for counter in range(powerSetSize):
        for shiftIndex in range(setSize):
            if counter & (1 << shiftIndex):
                print(arr[shiftIndex], end="")
                
        print()
        
arr = [1,2,3]
subsequences(arr)
subsequencesPowerSet(arr)