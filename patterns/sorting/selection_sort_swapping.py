# Time : O(n^2)
# Space : O(1)

def selectionSort(arr):
    if len(arr) <= 1:
        return arr

    for i in range(len(arr)):
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[minIndex] > arr[j]:
                minIndex = j

        arr[minIndex], arr[i] = arr[i], arr[minIndex]

    return arr


arr = [3, 2, 1, 9, 87, 7, 6, 5, 4, 2, 1, 3, 4, 542, 4, 32, 1, 34213, 214, 4, 32, 4, 352, 1, 324, 432, 4, 32, 54, 364, 355,
       6, 78, 887, 98, 0, 54, 757, 67, 456, 78, 5, 42, 4646, 110, 7, 89, 98, 77, 3, 422, 14, 67, 89, 878, 3, 345, 57, 869, 43, 4]
print(selectionSort(arr))
