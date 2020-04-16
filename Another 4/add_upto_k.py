"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""

# Using sorting

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
