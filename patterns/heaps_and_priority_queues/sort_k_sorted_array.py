import heapq


def sort_k_sorted_array(arr, k):
    minHeap = []
    for i, item in enumerate(arr):
        if len(minHeap) < k:
            heapq.heappush(minHeap, item)
        else:
            arr[i - k] = minHeap[0]
            heapq.heapreplace(minHeap, item)
    i = len(arr) - k
    while minHeap:
        arr[i] = heapq.heappop(minHeap)
        i += 1

    return arr


# test cases for above function
arr = [6, 5, 3, 2, 8, 10, 9]
k = 4
print(sort_k_sorted_array(arr, k))
