import heapq


def k_closest_number(arr, k, x):
    """
    Find the k closest numbers in the array to the given number x.

    Args:
        arr (list): The input array.
        k (int): The number of closest numbers to find.
        x (int): The given number.

    Returns:
        list: The k closest numbers in the array to the given number x.
    """
    maxHeap = []
    for i in range(len(arr)):
        if len(maxHeap) < k:
            heapq.heappush(maxHeap, [-abs(arr[i] - x), arr[i]])
        else:
            if -maxHeap[0][0] > abs(arr[i] - x):
                heapq.heapreplace(maxHeap, [-abs(arr[i] - x), arr[i]])
    result = [item[1] for item in maxHeap]
    return result


# test cases for above function
arr = [10, 2, 14, 4, 7, 6]
x = 5
k = 3
print(k_closest_number(arr, k, x))
