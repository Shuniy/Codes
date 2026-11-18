"""
Hard
Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of 
all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

"""
# Time : O(n) Space : O(n)
# Question can be done by maintaing two arrays which stores the product of the previous elements and product upto that element
# Suppose array is [1, 2, 3, 4, 5]
# Left array would be arr[i - 1] * left[i - 1]. This will store the prodcut of the array upto that index but not the element at that index
# Right array would be arr[i + 1] * right[i + 1]. This works same as the left array
# Now, all we have to do is multiply the left and right part of the index because that would have stored the product to left of that index and right of that index


def productArray(array):
    left = [0] * len(array)
    right = [0] * len(array)

    left[0] = 1
    right[len(array) - 1] = 1

    for i in range(1, len(array)):
        left[i] = left[i - 1] * array[i - 1]
    for i in range(len(array) - 2, -1, -1):
        right[i] = right[i + 1] * array[i + 1]
    
    product = [0] * len(array)
    for i in range(len(array) - 1):
        product[i] = left[i] * right[i]

    print(product)

array = [1,2,3,4,5]
productArray(array)

"""
def productArray(arr, n):

    if n == 1:
        print(0)
        return

    i, temp = 1, 1

    prod = [1 for i in range(n)]
    for i in range(n):
        prod[i] = temp
        temp *= arr[i]
    temp = 1
    for i in range(n - 1, -1, -1):
        prod[i] *= temp
        temp *= arr[i]

    for i in range(n):
        print(prod[i], end=" ")

    return

arr = [10, 3, 5, 6, 2]
n = len(arr)
print("The product array is: n")
productArray(arr, n)

"""
