
import collections


def MaximumAllSubnumsaySizeK(nums: list[int], k: int) -> list[int]:
    n = len(nums)
    result: list[int] = []
    queue = collections.deque([])
    i = 0
    for j in range(n):
        while queue and queue[-1] < nums[j]:
            _ = queue.pop()
        queue.append(nums[j])
        if j - i + 1 < k:
            continue
        else:
            result.append(queue[0])
            if queue[0] == nums[i]:
                _ = queue.popleft()
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


