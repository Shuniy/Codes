def maximumSubSubarraySizeK(arr: list, k: int) -> int:
    """
    Find the maximum sum of a subarray of size k within the given list.

    Args:
        arr (list): The input list of integers.
        k (int): The size of the subarray.

    Returns:
        int: The maximum sum of a subarray of size k.
    """
    if len(arr) < k:
        return -1

    i = 0
    max_sum = 0
    current_sum = 0
    for j, item in enumerate(arr):
        current_sum += item
        if j - i + 1 < k:
            continue
        max_sum = max(max_sum, current_sum)
        current_sum -= arr[i]
        i += 1
    return max_sum


nums: list[int] = [1, 4, 2, 10, 2, 3, 1, 0, 20]
K: int = 3
print("Maximum Subarrau sum of size k: ",
      maximumSubSubarraySizeK(arr=nums, k=K))

nums: list[int] = [100, 200, 300, 400]
K: int = 4
print("Maximum Subarrau sum of size k: ",
      maximumSubSubarraySizeK(arr=nums, k=K))
