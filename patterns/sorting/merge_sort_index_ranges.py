# Time Complexity = O(nlogn)
# Space : O(n)

def merge(left, right):
    merged = []
    i = 0
    j = 0
    # [1,2,3] and [0,1,4]
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


def mergeSortHelper(arr, start, end):
    if start >= end:
        return arr[start: end + 1]

    mid = start + (end - start) // 2
    left = mergeSortHelper(arr, start, mid)
    right = mergeSortHelper(arr, mid + 1, end)
    sorted = merge(left, right)
    return sorted


def mergeSort(arr):
    return mergeSortHelper(arr, 0, len(arr))


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 3, 13, 21, 34214, 35, 436, 54, 3, 25, 57, 3, 3, 76, 98, 80, 789,
       43, 2, 6453, 0, 7896, 245, 67, 7, 78, 98, 67, 542, 5, 7, 9, 3, 4567, 8896, 7, 54634, 29, 8, 4, 567, 89, 600, 985, 7463, 9328]
# arr = [9,8,7,6,5,4,3,2,1,0]
print(mergeSort(arr[:]))
