"""
Write an efficient program to find the sum of contiguous subarray
ithin a one-dimensional array of numbers which has the largest sum.
"""
from sys import maxsize

def kadane(arr, n):
    global_max = -maxsize
    max_here = 0
    start = 0
    end = 0
    s = 0

    for i in range(n):
        max_here = max_here + arr[i]

        if max_here > global_max:
            global_max = max_here
            start = s
            end = i

        if max_here < 0:
            max_here = 0
            s = i + 1

    return global_max

if __name__ == "__main__":
    a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
    print("Maximum contiguous sum is", kadane(a, len(a)))
