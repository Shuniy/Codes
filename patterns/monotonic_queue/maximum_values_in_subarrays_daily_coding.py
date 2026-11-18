"""
Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.

Sliding Window
"""

from collections import deque

def get_sliding_max(a, k):
    window_max_elements = list()
    if not a:
        return None
    if len(a) <= k:
        return max(a)

    dq = deque()
    for i in range(k):
        while dq and a[dq[-1] < a[i]]:
            dq.pop()
        dq.append(i)
    window_max_elements.append(a[dq[0]])

    for i in range(k, len(a)):
        while dq and dq[0] <= i - k:
            dq.popleft()

        while dq and a[dq[-1]] < a[i]:
            dq.pop()
        dq.append(i)

        window_max_elements.append(a[dq[0]])

    return window_max_elements

assert get_sliding_max([10, 5, 2, 7, 8, 7], 3) == [10, 7, 8, 8]
assert get_sliding_max([5, 2, 1], 2) == [5, 2]
