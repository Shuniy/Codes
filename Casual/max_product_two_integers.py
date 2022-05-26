"""
Given an array of integers, find maximum product of two integers in an array

arr = [-10,-3,5,6,-2]
"""
def find_maximum_product(arr):
    max1 = arr[0]
    max2 = float('-inf')

    min1 = arr[0]
    min2 = float('inf')

    for i in range(1, len(arr)):
        if arr[i] > max1:
            max2 = max1
            max1 = arr[i]
        elif arr[i] > max2:
            max2 = arr[i]

        if arr[i] < min1:
            min2 = min1
            min1 = arr[i]
        elif arr[i] < min2:
            min2 = arr[i]

    if max1 * max2 > min1 * min2:
        print("Pair is : ", (max1, max2))
    else:
        print("Pair is : ", (min1, min2))

if __name__ == "__main__":
    arr = [-10, -3, 5, 6, -2]
    find_maximum_product(arr)
