"""
Time Complexity: Time complexity of above implementation of shellsort is O(n2). 
In the above implementation gap is reduce by half in every iteration. There are 
many other ways to reduce gap which lead to better time complexity. See this for 
more details.

ShellSort is mainly a variation of Insertion Sort. In insertion sort, we move 
elements only one position ahead. When an element has to be moved far ahead, many 
movements are involved. The idea of shellSort is to allow exchange of far items. 
In shellSort, we make the array h-sorted for a large value of h. We keep reducing 
the value of h until it becomes 1. An array is said to be h-sorted if all sublists 
of every h’th element is sorted.
"""

import random
import time


def shellSort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            toChange = arr[i]
            j = i
            while j >= gap and toChange < arr[j - gap]:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = toChange
        gap = gap // 2


def shellsort(arr):
    n = len(arr)
    gap = n//2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap //= 2


size = int(input("Enter size of the array : "))
arr = list()

for i in range(size):
    c = random.randrange(0, size)
    arr.append(c)

# print("Entered array is : ")
# print(arr)

# shellsort(arr)
shellSort(arr)

print("Sorted array is : ")
print(arr)
start = time.time()
"the code you want to test stays here"
end = time.time()
print(end - start)
