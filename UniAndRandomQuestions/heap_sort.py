# Time : O(nlogn)
# Space : O(1)
import random


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


def heap_sort(array):
    build_max_heap(array)

    for end_index in reversed(range(1, len(array))):
        swap(0, end_index, array)

        sift_down(0, end_index - 1, array)

    return array


def build_max_heap(array):
    first_parent_index = (len(array) - 1) // 2
    for current_index in reversed(range(first_parent_index + 1)):
        sift_down(current_index, len(array) - 1, array)


def sift_down(current_index, end_index, heap):
    child_one_index = current_index * 2 + 1
    while child_one_index <= end_index:
        child_two_index = current_index * 2 + \
            2 if current_index * 2 + 2 <= end_index else -1

        if child_two_index > -1 and heap[child_two_index] > heap[child_one_index]:
            index_to_swap = child_two_index
        else:
            index_to_swap = child_one_index

        if heap[index_to_swap] > heap[current_index]:
            swap(current_index, index_to_swap, heap)
            current_index = index_to_swap
            child_one_index = current_index * 2 + 1
        else:
            return

# Create min heap


class Heap:
    def __init__(self, initialItems: list = []) -> None:
        self.heap = []
        if len(initialItems) > 0:
            for item in initialItems:
                self.insert(item)

    def getParentIndex(self, childrenIndex) -> int:
        return childrenIndex // 2

    def getParentValue(self, childrenIndex) -> object:
        return self.heap[self.getParentIndex(childrenIndex)]

    def getChildrenIndices(self, parentIndex) -> tuple[int, int]:
        return (2*parentIndex + 1), (2*parentIndex + 2)

    def getChildrenValues(self, parentIndex) -> tuple[object, object]:
        childIndices = self.getChildrenIndices(parentIndex)
        return self.heap[childIndices[0]], self.heap[childIndices[1]]

    def _upHeapify(self, index: int):
        # Heapify doesn't sort the array, remember that
        if index <= 0:
            return
        parentIndex = self.getParentIndex(index)
        parentValue = self.getParentValue(index)
        childValue = self.heap[index]

        if parentValue > childValue:
            self.heap[parentIndex] = childValue
            self.heap[index] = parentValue
            self._upHeapify(parentIndex)
        return

    def insert(self, value):
        if not self.heap:
            self.heap.append(value)
            return

        self.heap.append(value)
        # Now we have to move that element up that heirarchy
        self._upHeapify(len(self.heap) - 1)

    def getPeek(self) -> object:
        if not self.heap:
            return None
        return self.heap[0]

    def _downHeapify(self):
        if not self.heap:
            return
        parentIndex = 0
        while parentIndex < len(self.heap):
            leftChildIndex, rightChildIndex = self.getChildrenIndices(
                parentIndex)
            leftChildValue = None
            rightChildValue = None
            parentValue = self.heap[parentIndex]

            if leftChildIndex < len(self.heap):
                leftChildValue = self.heap[leftChildIndex]
            if rightChildIndex < len(self.heap):
                rightChildValue = self.heap[rightChildIndex]

            minElement = parentValue
            if leftChildValue is not None and rightChildValue is not None:
                minElement = min(leftChildValue, rightChildValue)
            elif leftChildValue is not None:
                minElement = leftChildValue
            elif rightChildValue is not None:
                minElement = rightChildValue
            else:
                minElement = parentValue

            if minElement == leftChildValue:
                self.heap[leftChildIndex] = parentValue
                self.heap[parentIndex] = leftChildValue
                parentIndex = leftChildIndex
            elif minElement == rightChildValue:
                self.heap[rightChildIndex] = parentValue
                self.heap[parentIndex] = rightChildValue
                parentIndex = rightChildIndex
            else:
                return
        return

    def remove(self) -> object:
        if not self.heap:
            return None
        toRemove = self.heap[0]
        lastElement = self.heap[-1]
        self.heap[0] = lastElement
        self.heap[-1] = toRemove
        self.heap.pop()
        self._downHeapify()
        return toRemove


def maxHeapify(arr, n, i):
    # Since we are heapifying, we should start with the rightmost parent value
    # suppose the largest element is present at i
    largest = i
    leftChildIndex = 2 * i + 1
    rightChildIndex = 2 * i + 2

    if leftChildIndex < n and arr[leftChildIndex] > arr[largest]:
        largest = leftChildIndex

    if rightChildIndex < n and arr[rightChildIndex] > arr[largest]:
        largest = rightChildIndex

    if largest != i:
        # that means we need to change
        arr[largest], arr[i] = arr[i], arr[largest]
        maxHeapify(arr, n, largest)


def heapsort(arr):
    # Just create a max heap and start removing the elements from the maxheap
    # heap will automatically gets sorted
    #  Well since we are not inserting anything, so it will be better to start heapify
    # from the rightmost non leaf node
    for i in range(len(arr) // 2, -1, -1):
        maxHeapify(arr, len(arr), i)

    for i in range(len(arr) - 1, 0, -1):
        # swap and reduce the index
        arr[0], arr[i] = arr[i], arr[0]
        maxHeapify(arr, i, 0)


array = list()
size = int(input("Enter size of the array : "))

for i in range(size):
    c = random.randrange(0, size)
    array.append(c)
heap = Heap(array[:])
# entered array
print("Entered array: ", array)

print("Min Heap: ", heap.heap)
# Insert
heap.insert(6)
print("Min Heap: ", heap.heap)
heap.insert(5)
print("Min Heap: ", heap.heap)
heap.insert(-1)
print("Min Heap: ", heap.heap)
heap.insert(99)
print("Min Heap: ", heap.heap)
# Remove
print(heap.remove())
print("Min Heap: ", heap.heap)
print(heap.remove())
print("Min Heap: ", heap.heap)
print(heap.remove())
print("Min Heap: ", heap.heap)
print(heap.remove())
print("Min Heap: ", heap.heap)
print(heap.remove())
print("Min Heap: ", heap.heap)
print(heap.remove())
print("Min Heap: ", heap.heap)
print(heap.remove())
print("Min Heap: ", heap.heap)

# HeapSort
# Entered array
print(array)
heapsort(array)
print("After HeapSort: ", array)
