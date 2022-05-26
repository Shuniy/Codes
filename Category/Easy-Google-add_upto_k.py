"""
Easy
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""
# Time : O(nlogn) - sorting, Space : O(1)
# 1st method is to use sorting and then use i and j pointers where i = 0 and j = len(array) - 1

# 2nd method is to use hashmap
# Time : O(n), Space : O(n)

def pair_sum(Array, k):
    solutions = set()

    for num in Array:
        if num in solutions:
            return True
        solutions.add(k - num)
    return False

assert not pair_sum([], 17)
assert pair_sum([10, 15, 3, 7], 17)
assert not pair_sum([10, 15, 3, 4], 17)
