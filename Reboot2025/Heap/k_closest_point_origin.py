import heapq


def k_closest_point_origin(arr, k):
    """
    Find the k closest points to the origin in the array.

    Args:
        arr (list): The input array.
        k (int): The number of closest points to find.

    Returns:
        list: The k closest points to the origin in the array.
    """
    minHeap = []
    for i in range(len(arr)):
        if len(minHeap) < k:
            heapq.heappush(minHeap, [arr[i][0] ** 2 + arr[i][1] ** 2, arr[i]])
        else:
            if minHeap[0][0] > arr[i][0] ** 2 + arr[i][1] ** 2:
                heapq.heapreplace(
                    minHeap, [arr[i][0] ** 2 + arr[i][1] ** 2, arr[i]])
    result = [item[1] for item in minHeap]
    return result


# test cases for above function
arr = [[3, 3], [5, -1], [-2, 4]]
k = 2
print(k_closest_point_origin(arr, k))

arr = [[3, 3], [5, -1], [-2, 4], [0, 0]]
k = 2
print(k_closest_point_origin(arr, k))

arr = [[3, 3], [1, -1], [-2, 4]]
k = 2
print(k_closest_point_origin(arr, k))
