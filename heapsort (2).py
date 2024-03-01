"""
Heap sort is a comparison based sorting technique based on Binary Heap data structure. 
It is similar to selection sort where we first find the maximum element and place 
the maximum element at the end. We repeat the same process for remaining element.

What is Binary Heap?
Let us first define a Complete Binary Tree. A complete binary tree is a binary tree 
in which every level, except possibly the last, is completely filled, and all nodes 
are as far left as possible (Source Wikipedia)

A Binary Heap is a Complete Binary Tree where items are stored in a special order 
such that value in a parent node is greater(or smaller) than the values in its two 
children nodes. The former is called as max heap and the latter is called min heap. 
The heap can be represented by binary tree or array.

Why array based representation for Binary Heap?
Since a Binary Heap is a Complete Binary Tree, it can be easily represented as array 
and array based representation is space efficient. If the parent node is stored at 
index I, the left child can be calculated by 2 * I + 1 and right child by 
2 * I + 2 (assuming the indexing starts at 0).

Heap Sort Algorithm for sorting in increasing order:
1. Build a max heap from the input data.
2. At this point, the largest item is stored at the root of the heap. Replace it 
with the last item of the heap followed by reducing the size of heap by 1. Finally, 
heapify the root of tree.
3. Repeat above steps while size of heap is greater than 1.

How to build the heap?
Heapify procedure can be applied to a node only if its children nodes are heapified. 
So the heapification must be performed in the bottom up order.

Time Complexity: Time complexity of heapify is O(Logn). Time complexity of 
createAndBuildHeap() is O(n) and overall time complexity of Heap Sort is O(nLogn).

Applications of HeapSort
1. Sort a nearly sorted (or K sorted) array
2. k largest(or smallest) elements in an array

Heap sort algorithm has limited uses because Quicksort and Mergesort are better in 
practice. Nevertheless, the Heap data structure itself is enormously used. See
Applications of Heap Data Structure
"""

import random


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)


def heapsort(arr):
    n = len(arr)

    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


arr = list()
size = int(input("Enter size of the array : "))

print("Enter elements of array : ")
for i in range(size):
    c = random.randrange(0, size)
    arr.append(int(c))

print("Entered array is : ")
print(arr)

heapsort(arr)

print("Sorted array is : ")
print(arr)
