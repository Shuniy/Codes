import heapq


def connect_ropes_to_minimize_cost(arr):
    """
    Connect the ropes to minimize the cost.

    Args:
        arr (list): The input array.

    Returns:
        int: The minimum cost to connect the ropes.
    """
    minHeap = []
    for i in range(len(arr)):
        heapq.heappush(minHeap, arr[i])

    while len(minHeap) > 1:
        first = heapq.heappop(minHeap)
        second = heapq.heappop(minHeap)
        heapq.heappush(minHeap, first + second)
    return minHeap[-1]


# test cases for above function
arr = [1, 2, 3, 4, 5, 6, 7, 8]
print(connect_ropes_to_minimize_cost(arr))
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(connect_ropes_to_minimize_cost(arr))
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(connect_ropes_to_minimize_cost(arr))
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
