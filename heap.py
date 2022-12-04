# Min Heap, if want to make Max heap then change the signs in heapify methods
from Elmo.HeapSort import heapify
from _typeshed import Self


class Heap:
    def __init__(self, size) -> None:
        self.heap = [None] * size
        # next index represent where to insert next element
        self.nextIndex = 0

    def _parentIndex(self, childIndex):
        return (childIndex - 1) // 2

    def _parentValue(self, childIndex):
        return self.heap[self._parentIndex(childIndex)]

    def _childrenIndices(self, parentIndex):
        childIndex1 = 2 * parentIndex + 1
        childIndex2 = 2 * parentIndex + 2
        return (childIndex1, childIndex1)

    def _childrenValues(self, parentIndex):
        childIndex1, childIndex2 = self._childrenIndices(parentIndex)
        childValue1, childValue2 = self.heap[childIndex1], self.heap[childIndex2]
        return (childValue1, childValue2)

    def size(self):
        return self.nextIndex

    def isEmpty(self):
        return self.size == 0

    def getMinimum(self):
        if self.size() == 0:
            return None
        return self.heap[0]

    def _upHeapify(self, index):
        if index == 0:
            return 

        indexParent = self._parentIndex(index)
        parentValue = self._parentValue(index)
        childValue = self.heap[index]

        if parentValue > childValue:
            # swap values
            self.heap[index] = parentValue
            self.heap[indexParent] = childValue
            self._upHeapify(indexParent)
        else:
            pass

    def insert(self, value):
        if self.nextIndex < len(self.heap) - 1:
            self.heap[self.nextIndex] = value
            self._upHeapify(self.nextIndex)
            self.nextIndex += 1

    def _downHeapify(self):
        parentIndex = 0
        # self.nextIndex is still not reduced and point to swapped removed element
        while parentIndex < self.nextIndex:
            leftChildIndex, rightChildIndex = self._childrenIndices(parentIndex)
            parentValue = self.heap[parentIndex]
            leftChild = None
            rightChild = None
            minElement = None

            if leftChildIndex < self.nextIndex:
                leftChild = self.heap[leftChildIndex]

            if rightChildIndex < self.nextIndex:
                rightChild = self.heap[rightChildIndex]

            if leftChild:
                minElement = min(parentValue, leftChild)
            
            if rightChild:
                minElement = min(parentValue, rightChild)

            if minElement == parentValue:
                return

            if minElement == leftChild:
                self.heap[leftChildIndex] = parentValue
                self.heap[parentIndex] = minElement
                parentIndex = leftChildIndex
            elif minElement == rightChild:
                self.heap[rightChildIndex] = parentValue
                self.heap[parentIndex] = minElement
                parentIndex = rightChildIndex

    def delete(self):
        if self.size() == 0:
            return None

        self.nextIndex -= 1
        toRemove = self.heap[0]
        lastElement = self.heap[self.nextIndex]
        self.heap[0] = lastElement
        self.heap[self.nextIndex] = toRemove
        self._downHeapify()
        return toRemove

    def heapify(self, arr):
        self.heap = self.heapSort(arr)
        return self.heap

    def _heapify(self, arr, index):
        if index == 0:
            return arr

        indexParent = (index - 1) // 2
        parentValue = arr[indexParent]
        childValue = arr[index]

        if childValue > parentValue:
            arr[indexParent] = childValue
            arr[index] = parentValue
            arr = self._heapify(arr, indexParent)
        else:
            pass

        return arr

    def heapSort(self, arr):
        n = len(arr)
        for i in range(n):
            arr = self._heapify(arr, i)

        swapPosition = n - 1
        for i in range(n):
            biggerValue = arr[0]
            arr[0] = arr[swapPosition]
            arr[swapPosition] = biggerValue

            for i in range(swapPosition):
                arr = self._upHeapify(arr, i)
            swapPosition -= 1

        return arr