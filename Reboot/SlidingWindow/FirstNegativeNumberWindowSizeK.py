import collections


def FirstNegativeNumberWindowSizeK(nums: list[int], k: int) -> list[int]:
    """
    A function that finds the first negative number in a sliding window of size k within a list of numbers.

    Args:
        nums (list[int]): The input list of numbers.
        k (int): The size of the sliding window.

    Returns:
        list[int]: A list of the first negative numbers in each sliding window of size k.
    """

    i = 0
    result = []
    negative_numbers = collections.deque([])

    for j, item in enumerate(nums):
        if item < 0:
            negative_numbers.append(item)
        if j - i + 1 < k:
            continue
        if not negative_numbers:
            result.append(0)
        else:
            result.append(negative_numbers[0])
            while negative_numbers and negative_numbers[0] == nums[i]:
                negative_numbers.popleft()
            i += 1
    return result


arr: list[int] = [12, -1, -7, 8, -15, 30, 16, 28]
K: int = 3
print(FirstNegativeNumberWindowSizeK(arr, K))
