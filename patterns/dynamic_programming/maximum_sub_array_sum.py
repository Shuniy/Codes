import sys

"""
Problem Statement
You have been given an array containg numbers. Find and return the largest sum in a contiguous subarray within the input array.

Example 1:

arr= [1, 2, 3, -4, 6]
The largest sum is 8, which is the sum of all elements of the array.
Example 2:

arr = [1, 2, -5, -4, 1, 6]
The largest sum is 7, which is the sum of the last two elements of the array.
"""
def MaxSubArraySum(input_list : list) -> int:
    localSum = 0
    globalSum = -sys.maxsize - 1
    for i in range(len(input_list)):
        localSum = localSum + input_list[i]
        if localSum > globalSum:
            globalSum = localSum
        if localSum < 0:
            localSum = 0
    return globalSum


a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
print("Maximum contiguous sum is", MaxSubArraySum(a))

