import collections
import heapq


def frequency_sort(arr):
    """
    Sorts the input array 'arr' based on the frequency of elements and returns the sorted array.
    """
    maxHeap = []
    counter = collections.Counter(arr)
    items = counter.items()
    for item in items:
        heapq.heappush(maxHeap, (-item[1], item[0]))

    result = []
    for item in maxHeap:
        result.extend([item[1]] * (-1 * item[0]))

    return result


# test cases for above function
arr = [2, 5, 2, 8, 5, 6, 8, 8]
print(frequency_sort(arr))
