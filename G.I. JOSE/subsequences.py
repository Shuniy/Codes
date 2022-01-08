"""
Method 1 is to include the current element to subsequence or not

Method 2 is to generate power set with set size = n or length of the arr -> Refer power set code
"""
import math
subsequences = []


def subsequencesRecursionHelper(arr, currentIndex, subsequence):
    if currentIndex > len(arr):
        return
    elif currentIndex == len(arr):
        subsequences.append(subsequence)
    else:
        subsequencesRecursionHelper(arr, currentIndex + 1, subsequence)
        subsequencesRecursionHelper(
            arr, currentIndex + 1, [arr[currentIndex]] + subsequence)


def subsequencesRecursion(arr):
    subsequencesRecursionHelper(arr, 0, [])


def powerset(arr):
    set_size = len(arr)
    powerset_size = (int)(math.pow(2, set_size))

    for counter in range(powerset_size):
        temp = []
        for j in range(set_size):
            if counter & (1 << j):
                temp.append(str(arr[j]))
        subsequences.append("".join(temp))


arr = [1, 2, 3]
subsequencesRecursion(arr)
print(subsequences)
subsequences = []
powerset(arr)
print(subsequences)
