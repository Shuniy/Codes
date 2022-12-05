"""
Good sub_arrays = it is a sub array such that sum is divisble by N

Pigeonhole Principle

https://www.youtube.com/watch?time_continue=864&v=p5Cm_r4T1Rw&feature=emb_logo
"""

def subCount(arr, n, k):
    mod = []
    for i in range(k + 1):
        mod.append(0)
    cumSum = 0
    for i in range(n):
        cumSum = cumSum + arr[i]
        mod[((cumSum % k)+k) % k] = mod[((cumSum % k)+k) % k] + 1

    result = 0
    for i in range(k):

        if (mod[i] > 1):
            result = result + (mod[i]*(mod[i]-1))//2
    result = result + mod[0]

    return result

arr = [4, 5, 0, -2, -3, 1]
k = 5
n = len(arr)

print(subCount(arr, n, k))
arr1 = [4, 5, 0, -12, -23, 1]

k1 = 5
n1 = len(arr1)
print(subCount(arr1, n1, k1))
