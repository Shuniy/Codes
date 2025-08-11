import collections


def MaximumAllSubnumsaySizeK(nums: list[int], k: int) -> list[int]:
    """
    Given a list of integers `nums` and an integer `k`, returns a list of the maximum values of all subarrays of size `k`.

    Parameters:
        - nums (list[int]): The input list of integers.
        - k (int): The size of the subarrays.

    Returns:
        - result (list[int]): A list of the maximum values of all subarrays of size `k`.

    Example:
        >>> MaximumAllSubnumsaySizeK([1, 3, 2, 4, 5], 2)
        [3, 4, 5]
    """
    if len(nums) < k:
        return []

    result = []
    i = 0
    max_numbers = collections.deque([])
    for j, item in enumerate(nums):
        while max_numbers and item > max_numbers[-1]:
            max_numbers.popleft()

        if j - i + 1 < k:
            continue
        result.append(max_numbers[0])
        if max_numbers[0] == nums[i]:
            max_numbers.popleft()
        i += 1

    return result


arr = [1, 3, -1, -3, 5, 3, 6, 7]
K = 3
print(MaximumAllSubnumsaySizeK(arr, K))

arr = [12, 1, 78, 90, 57, 89, 56]
K = 3
print(MaximumAllSubnumsaySizeK(arr, K))

arr = [1, 3, 1, 2, 0, 5]
K = 3
print(MaximumAllSubnumsaySizeK(arr, K))
