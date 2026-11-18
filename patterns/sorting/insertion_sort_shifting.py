# Time Complexity = O(n^2)
# Space Complexity = O(1)

def insertionSort(arr):
    if len(arr) <= 1:
        return arr

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 3, 23, 213, 1, 31, 4, 432, 4, 324, 532, 5, 235,
       321, 12, 3, 13, 14, 3, 543, 25, 23, 13, 2, 4, 235, 23341, 342, 354, 234, 1, 3445, 21]
print(insertionSort(arr[:]))
