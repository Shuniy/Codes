def LargestSubarraySumK(arr: list[int], n: int, k: int) -> int:
    i: int = 0
    maxLen: int = 0
    currentSum: int = 0
    for j in range(len(arr)):
        currentSum += arr[j]
        if currentSum < k:
            continue
        elif currentSum == k:
            maxLen = max(maxLen, j - i + 1)
        else:
            while currentSum > k:
                currentSum -= arr[i]
                i += 1
            if currentSum == k:
                maxLen = max(maxLen, j - i + 1)
            
    return maxLen

def LargestSubarraySumKHashmap(arr: list[int], n: int, k: int) -> int:
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

arr = [ 10, 5, 2, 7, 1, 9 ]
n = len(arr)
k = 15

print("Length = " , LargestSubarraySumK(arr, n, k))
print("Length = " , LargestSubarraySumKHashmap(arr, n, k))