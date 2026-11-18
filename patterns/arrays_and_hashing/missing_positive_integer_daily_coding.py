"""
Hard
Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

# This can be done by considering things such as since we need only positive numbers we can seperate the negative and positive numbers
# Then, we can use the length of the array as the factor to finf if the number is missing or not
# Suppose number are continuous in form

def get_positive_subset(array):
    i = 0
    j = len(array) - 1

    while i < j:
        if array[i] > 0 and array[j] <= 0:
            array[i], array[j] = array[j], array[i]
        elif array[i] > 0:
            j -= 1
        else:
            i += 1
    pivot = i if array[i] > 0 else i + 1
    return array[pivot:]

def get_missing_number(array):
    if not array:
        return 1

    array = get_positive_subset(array)
    n = len(array)

    # special case
    if max(array) == n:
        return max(array) + 1

    for num in array:
        current = abs(num)
        if current - 1 < n:
            array[current - 1] *= -1

    for i in range(n):
        if array[i] > 0:
            return i + 1
 
assert get_missing_number([3, 4, -1, 1]) == 2
assert get_missing_number([1, 2, 0]) == 3
assert get_missing_number([1, 2, 5]) == 3
assert get_missing_number([1]) == 2
assert get_missing_number([-1, -2]) == 1
assert get_missing_number([]) == 1
