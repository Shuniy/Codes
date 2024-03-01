import collections

def MaximumAllSubnumsaySizeK(nums: list[int], k: int) -> list[int]:
    n = len(nums)
    result: list[int] = []
    maxNumbers: collections.deque[int] = collections.deque([])
    i: int = 0
    for j in range(len(nums)):
        while maxNumbers and nums[j] > maxNumbers[-1]:
            maxNumbers.pop()
        maxNumbers.append(nums[j])
        if j - i + 1 < k:
            continue
        else:
            result.append(maxNumbers[0])
            if maxNumbers[0] == nums[i]:
                maxNumbers.popleft()
        i += 1
    return result

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(MaximumAllSubnumsaySizeK(nums, k))

nums = [12, 1, 78, 90, 57, 89, 56]
k = 3
print(MaximumAllSubnumsaySizeK(nums, k))

nums = [1, 3, 1, 2, 0, 5]
k = 3
print(MaximumAllSubnumsaySizeK(nums, k))


