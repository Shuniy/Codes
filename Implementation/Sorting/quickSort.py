# Time : O(nlogn) average and worst is O(n^2)
# Space : O(1) // if recursion stack is ignored

def sortALittleBit(arr, startIndex, endIndex):
    leftIndex = startIndex
    pivotIndex = endIndex
    pivotValue = arr[pivotIndex]

    while pivotIndex != leftIndex:
        leftIndexValue = arr[leftIndex]
        if leftIndexValue < pivotValue:
            leftIndex += 1
            continue

        arr[leftIndex] = arr[pivotIndex - 1]
        arr[pivotIndex - 1] = pivotValue
        arr[pivotIndex] = leftIndexValue
        pivotIndex -= 1

    return pivotIndex


def quickSortHelper(arr, start, end):
    if start >= end:
        return

    partition = sortALittleBit(arr, start, end)
    quickSortHelper(arr, start, partition - 1)
    quickSortHelper(arr, partition + 1, end)


def quickSort(arr):
    quickSortHelper(arr, 0, len(arr) - 1)


# arr = [9,8,7,6,5,4,3,2,1,0]
arr = [3, 1, 43, 42, 543, 6567, 769, 87, 0, 3421, 75, 432, 354, 678, 90, 7, 3, 4, 3547, 89, 7, 98, 3, 2, 23, 3456, 78, 98, 76, 543,
       2, 5432, 2456, 475, 89, 0, 7, 763, 523, 3, 6876, 99, 6, 543, 2, 9786, 36, 4758, 908, 7, 6543, 2, 54, 6457, 8, 123, 32, 3, 89, 8]
quickSort(arr)
print(arr)
