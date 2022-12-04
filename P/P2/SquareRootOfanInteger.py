"""
Finding the Square Root of an Integer
Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

The principle of this algorithm is to implement a variance of the binary search, due to the required time complexity. This time, though, instead of counting with an already sorted array, we use the natural consecution to use as our imaginary array; the implementation relies on dividing the search space in two parts and checking at each time if the mid point power of 2 is bigger or smaller than the given number (as in a dictionary, is the found word, bigger or smaller than our goal). Additionally, there is the inclusion of a little optimization trick, this is the fact that the square root of a natural number (starting from 2) is half or less, thus giving us a _speed boost by starting with end = number // 2.

Time and Space complexity:
In this case time complexity is O(log(n)), as we transverse the hypothetically ordered natural's number list by using a binary search approach. As for the space complexity, it is independent of the input, requiring solely pointers to different array locations; O(1).

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is O(log(n))
"""


def sqrt(number: int) -> int:
    """
    Calculate the floored square root of a number
    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    if number < 0:
        return None

    if (number == 0) or (number == 1):
        return number

    i_start = 0
    i_end = number // 2

    while i_start <= i_end:
        i_middle = (i_end + i_start) // 2
        i_middle_pow = i_middle * i_middle

        if i_middle_pow == number:
            return i_middle
        elif i_middle_pow < number:
            i_start = i_middle + 1
            result = i_middle
        else:
            i_end = i_middle - 1

    return result

# Normal cases
print('Normal Cases:')
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass \n" if (5 == sqrt(27)) else "Fail \n")

# Edge cases
print('Edge Cases:')
print("Pass" if (None == sqrt(-1)) else "Fail")
print("Pass" if (99380 == sqrt(9876543210)) else "Fail")
