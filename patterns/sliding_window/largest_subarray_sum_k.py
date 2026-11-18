def LargestSubarraySumK(arr: list[int], k: int) -> int:
    """
    Calculate the length of the largest subarray with a sum equal to or less than k.

    Args:
        arr (list[int]): The input list of integers.
        k (int): The target sum.

    Returns:
        int: The length of the largest subarray with a sum equal to or less than k.
    """
    i = 0
    max_len = 0
    current_sum = 0
    for j, item in enumerate(arr):
        current_sum += item
        if current_sum < k:
            continue
        elif current_sum == k:
            max_len = max(max_len, j - i + 1)
        else:   
            while current_sum > k:
                current_sum -= arr[i]
                i += 1
            if current_sum == k:
                max_len = max(j - i + 1, max_len)
    return max_len


def LargestSubarraySumKHashmap(arr: list[int], k: int) -> int:
    """
    Calculate the length of the largest subarray in the given list `arr` that sums up to `k`.

    Parameters:
    - arr (list[int]): The input list of integers.
    - k (int): The target sum.

    Returns:
    - int: The length of the largest subarray that sums up to `k`.
    """
    maxLen: int = 0
    currentSum: int = 0
    hashmap: dict = {}
    for j in range(len(arr)):
        currentSum += arr[j]
        if currentSum == k:
            maxLen = j + 1
        elif currentSum - k in hashmap:
            maxLen = max(maxLen, j - hashmap[currentSum - k])
        if currentSum not in hashmap:
            hashmap[currentSum] = j
    return maxLen


nums = [10, 5, 2, 7, 1, 9]
K = 15

print("Length = ", LargestSubarraySumK(nums, K))
print("Length = ", LargestSubarraySumKHashmap(nums, K))
