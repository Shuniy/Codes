"""
Method 1 : Generate all subarrays and find sum
Method 2 : Generate Prefix
Method 3 : Kadane's Algorithm
Method 4 : Dynamic Programming
"""
# O(n^3)
def generateSubarrays(arr):
    subarrays = []

    for i in range(len(arr)):
        for j in range(i, len(arr)):
            subarrays.append(arr[i:j + 1])
            
    return subarrays

# Method 1
# O(n^3)
def subarraySum1(arr):
    subarrays = generateSubarrays(arr)
    subarraysSums = []

    for item in subarrays:
        subarraysSums.append(sum(item))

    return max(subarraysSums)

# Method 2
# O(n^2)
def subarraySum2(arr):
    prefix = [0 for _ in range(len(arr) + 1)]
    for i in range(1, len(arr)):
        prefix[i] = prefix[i - 1] + arr[i]

    largestSum = 0

    for i in range(len(arr)):
        for j in range(i, len(arr)):
            subarraySum = prefix[j] - prefix[i - 1] if i > 0 else prefix[j]
            largestSum = max(largestSum, subarraySum)

    return largestSum

# Method 3
#O(n)
def subarraySum3(arr):
    currentSum = 0
    largestSum = 0
    
    for i in range(len(arr)):
        currentSum = currentSum + arr[i]
        if currentSum < 0:
            currentSum = 0
            
        largestSum = max(largestSum, currentSum)
        
    return largestSum

# Method 4
# O(n)
def subarraySum4(arr):
    if len(arr) == 0:
        return 0
    
    if len(arr) == 1:
        return arr[0]
    
    for i in range(1, len(arr)):
        if arr[i - 1] > 0:
            arr[i] += arr[i - 1]
            
    return max(arr)

arr = [1, 2, 3, 4, 5, 6, 7, -1, -12, -3, -4, -6, -8, -9, 34, 12, -
       312, -3241, -565, -63, 123, 523, 654, 13, 145, 1235, 6, 1665, 212]

print(subarraySum1(arr))
print(subarraySum2(arr))
print(subarraySum3(arr))
print(subarraySum4(arr))