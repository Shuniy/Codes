"""
Max and Min in a Unsorted Array
In this problem, we will look for smallest and largest integer from a list of unsorted integers. The code should run in O(n) time.

Sorting usually requires O(n log n) time
Can you come up with a O(n) algorithm (i.e., linear time)?

This problem focuses on finding max and min values from an unsorted array, we are not required to nothing extra and here lies the key, not being required to sort anything, we can solve the problem with a single transversal and two placeholders, as reference for min and max values.

Time and Space complexity
In this case, we perform a single transverse of the whole input, being the time complexity of O(n). In respect to the space complexity, we have just a pair of pointers, hence, it is independent from input size; O(1).
"""
import random

def get_min_max(ints):
    if len(ints) == 0:
        return None

    max_val = - float("inf")
    min_val = float("inf")

    for inti in ints:
        if inti > max_val:
            max_val = inti

        if inti < min_val:
            min_val = inti

    return (min_val, max_val)

# Normal cases
print('Normal Cases:')
# Case 1
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# Case 2
l = [i for i in range(-12, 25)]  # a list containing -12 - 24
random.shuffle(l)
print("Pass" if ((-12, 24) == get_min_max(l)) else "Fail")
print('\n')

# Edge cases
print('Edge Cases:')
# Case 3
l = [i for i in range(300, 301)]  # a list containing 300
random.shuffle(l)
print("Pass" if ((300, 300) == get_min_max(l)) else "Fail")

# Case 4
l = []  # an empty list
print("Pass" if (None == get_min_max(l)) else "Fail")

# Case 5
l = [i for i in range(-24, -1)]  # a list containing -24 - -2
random.shuffle(l)
print("Pass" if ((-24, -2) == get_min_max(l)) else "Fail")
