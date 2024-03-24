import heapq


def sum_k1_elements_k2_elements(arr, k1, k2):
    """
    Calculate the sum of elements in the input array between the k1-th and k2-th elements.

    :param arr: list of integers
    :param k1: integer, representing the start index for the sum
    :param k2: integer, representing the end index for the sum
    :return: integer, the sum of elements between the k1-th and k2-th elements
    """
    min_heap = []
    for _, item in enumerate(arr):
        if len(min_heap) <= 6:
            heapq.heappush(min_heap, item)
        else:
            if item < min_heap[0]:
                heapq.heapreplace(min_heap, item)
    return sum(arr[k1: k2])


# test cases for above function
nums = [20, 8, 22, 4, 12, 10, 14]
K1 = 3
K2 = 6
print(sum_k1_elements_k2_elements(nums, K1, K2))
