
import collections

def MaximumAllSubarraySizeK(arr: list[int], k: int) -> list[int]:
    n = len(arr)
    result: list[int] = []
    queue = collections.deque(arr)
    i = 0
    for j in range(n):
        while queue and queue[0] < arr[j]:
            _ = queue.popleft()
        if j - i + 1 < k:
            continue
        else:
            result.append(queue[0])
            if queue[0] == arr[i]:
                _ = queue.popleft()
            i += 1
            
    return result
        

arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(MaximumAllSubarraySizeK(arr, k))

arr = [12, 1, 78, 90, 57, 89, 56]
k = 3
print(MaximumAllSubarraySizeK(arr, k))

arr = [1,3,1,2,0,5]
k = 3
print(MaximumAllSubarraySizeK(arr, k))