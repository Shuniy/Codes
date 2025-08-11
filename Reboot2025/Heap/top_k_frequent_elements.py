import collections
import heapq


def top_k_frequent_elements(arr, k):
    counter = collections.Counter(arr)
    items = counter.items()
    minHeap = []
    for item in items:
        if len(minHeap) < k:
            heapq.heappush(minHeap, (item[1], item[0]))
        else:
            if minHeap[0][0] < item[1]:
                heapq.heapreplace(minHeap, (item[1], item[0]))
        print(minHeap)
    return [item[1] for item in minHeap]


# test cases for above function
arr = [5, 2, 1, 1, 1, 3, 3, 3, 3, 5, 2]
k = 2
print(top_k_frequent_elements(arr, k))
