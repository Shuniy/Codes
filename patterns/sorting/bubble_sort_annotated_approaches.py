"""
Worst and Average Case Time Complexity: O(n*n). Worst case occurs when array is
reverse sorted.

Best Case Time Complexity: O(n). Best case occurs when array is already sorted.

Auxiliary Space: O(1)

Boundary Cases: Bubble sort takes minimum time (Order of n) when elements are 
already sorted.

Sorting In Place: Yes

Stable: Yes

Due to its simplicity, bubble sort is often used to introduce the concept of a 
sorting algorithm.

In computer graphics it is popular for its capability to detect a very small 
error (like swap of just two elements) in almost-sorted arrays and fix it with 
just linear complexity (2n). For example, it is used in a polygon filling 
algorithm, where bounding lines are sorted by their x coordinate at a specific 
scan line (a line parallel to x axis) and with incrementing y their order changes 
(two elements are swapped) only at intersections of two lines
"""
import random


def bubbleSort(arr):
    swapped = False
    for i in range(len(arr)):
        for j in range(1, len(arr) - i):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                swapped = True
        if not swapped:
            return


def bubbleSortRecursive(arr, n=None):
    if n == None:
        n = len(arr)

    if len(arr) == 1:
        return

    swapped = False

    for j in range(n - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapped = True

    if not swapped:
        return

    bubbleSortRecursive(arr, n - 1)


def bubblesort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp


size = int(input("Enter size of the array : "))
arr = list()

for i in range(size):
    c = random.randrange(0, size)
    arr.append(c)

# bubblesort(arr)
bubbleSort(arr)
# bubbleSortRecursive(arr)
print("Sorted array is : ")
print(arr)
