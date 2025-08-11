import heapq


def kth_smallest_element(arr, k):
    """
    Find the kth smallest element in the given array using a max heap.

    Args:
        arr (list): The input array.
        k (int): The kth smallest element to find.

    Returns:
        int: The kth smallest element in the array.
    """
    maxHeap = []
    for i in range(len(arr)):
        if len(maxHeap) < k:
            heapq.heappush(maxHeap, -arr[i])
        else:
            if -maxHeap[0] > arr[i]:
                heapq.heapreplace(maxHeap, -arr[i])
    return -maxHeap[0]


# test cases for above functions
arr = [2, 5, 6, 8, 9, 234, 6, 4568, 57, 855, 45, 45, 7, 5646, 4, 7, 4]
k = 4
print(kth_smallest_element(arr, k))
arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
K = 4
print(kth_smallest_element(arr, k))
