# sorted arrays : A, B, C
# equation is minimize: absolute of (max(a, b, c) - min(a, b, c))
# a belongs to A
# b belongs to B
# c belongs to C

# Brute Force is to create each possible combination and find the minimum

# Optimized:
# there are two ways to minimize the equations:
# either minimizr the max value or maximize the min value
# Since, it is a sorted array, therefore, 
# only way is to maxmimize the value because next element in sorted array will always be greater than before

def minimizeEquation(arr1, arr2, arr3):
    i = 0
    j = 0
    k = 0
    m = len(arr1)
    n = len(arr2)
    o = len(arr3)
    globalMin = float("inf")
    currentMin = float("inf")
    while i < m and j < n and k < o:
        currentMin = arr1[i] + arr2[j] + arr3[k]
        globalMin = min(globalMin, currentMin)
        currentMinimumValue = min(arr1[i], arr2[j], arr3[k])
        if currentMinimumValue == arr1[i]:
            i += 1
        elif currentMinimumValue == arr2[j]:
            j += 1
        else:
            k += 1      
    return globalMin
