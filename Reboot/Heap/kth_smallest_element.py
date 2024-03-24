import heapq


def kth_smallest_element(arr, k):
    """
    Find the kth smallest element in the given array using a min heap.

    Args:
        arr (list): The input array.
        k (int): The kth smallest element to find.

    Returns:
        int: The kth smallest element in the array.
    """
    minHeap = []
    for i in range(len(arr)):
        if len(minHeap) < k:
            heapq.heappush(minHeap, arr[i])
        else:
            if minHeap[0] > arr[i]:
                heapq.heapreplace(minHeap, arr[i])
    return minHeap[-1]


# test cases for above functions
arr = [2, 5, 6, 8, 9, 234, 6, 4568, 57, 855, 45, 45, 7, 5646, 4, 7, 4]
k = 4
print(kth_smallest_element(arr, k))
