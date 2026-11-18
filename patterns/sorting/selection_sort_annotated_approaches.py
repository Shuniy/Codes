"""
Time Complexity: O(n^2) as there are two nested loops.

Auxiliary Space: O(1)
The good thing about selection sort is it never makes more than O(n) swaps and 
can be useful when memory write is a costly operation.

Stability : The default implementation is not stable. However it can be made stable. Please see stable selection sort for details.

In Place : Yes, it does not require extra space.
"""


import random


def selectionSortRecursive(arr, i=0):
    if len(arr) == 1:
        return

    mini = i
    for j in range(i + 1, len(arr)):
        if (arr[j] < arr[mini]):
            mini = j
    arr[i], arr[mini] = arr[mini], arr[i]
    if i + 1 < len(arr):
        selectionSortRecursive(arr, i + 1)
    else:
        return


def selectionSort(arr):
    for i in range(len(arr)):
        # Find the minimum value index
        mini = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[mini]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]


def selectionsort(arr):

    for i in range(len(arr)):
        mini = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[mini]:
                mini = j

        arr[i], arr[mini] = arr[mini], arr[i]


arr = list()
size = int(input("Enter size of the array : "))
arr = list()

for i in range(size):
    c = random.randrange(0, size)
    arr.append(c)

# print("Entered array is : ")
# print(arr)

# selectionsort(arr)
selectionSort(arr)
# selectionSortRecursive(arr)

print("Sorted array is : ")
print(arr)
