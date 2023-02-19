def maximumSubSubarraySizeK(arr: list, k: int) -> int:
    if len(arr) < k:
        return 0
    
    i: int = 0
    maxSum: int = 0
    currentSum: int = 0
    for j in range(len(arr)):
        currentSum += arr[j]
        if j - i + 1 < k:
            continue
        else:
            maxSum = max(currentSum, maxSum)
            currentSum -= arr[i]
            i += 1
    return maxSum

arr: list[int] = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k: int = 3
print("Maximum Subarrau sum of size k: ", maximumSubSubarraySizeK(arr=arr, k=k))

arr: list[int] = [100, 200, 300, 400]
k: int = 4
print("Maximum Subarrau sum of size k: ", maximumSubSubarraySizeK(arr=arr, k=k))