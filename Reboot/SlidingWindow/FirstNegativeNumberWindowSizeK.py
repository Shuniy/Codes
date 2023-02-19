import collections

def FirstNegativeNumberWindowSizeK(arr: list[int], n: int, k: int) -> list[int]:
    i = 0
    result = []
    queue = collections.deque([item for item in arr if item < 0])
    for j in range(len(arr)):
        if j - i + 1 < k:
            continue
        else:
            if len(queue) == 0:
                result.append(0)
            else:
                result.append(queue[0])
                if queue[0] == arr[i]:
                    _ = queue.popleft()
                i += 1
            
    return result

arr: list[int] = [12, -1, -7, 8, -15, 30, 16, 28]
n: int = len(arr)
k: int = 3
print(FirstNegativeNumberWindowSizeK(arr, n, k))