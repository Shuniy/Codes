"""
Given an unsorted array of size n.
Array elements are in the range from 1 to n.
One number from set {1, 2, …n} is missing and one number occurs
twice in the array. Find these two numbers.
"""

def repeat_and_missing_1(arr):
    Total_sum = sum([i for i in range(1, len(arr) + 1)])
    Total_sum_squares = sum([i**2 for i in range(1, len(arr) + 1)])

    Sum_array = sum(arr)
    sum_squares = sum([item**2 for item in arr])

    x_y = Total_sum - Sum_array
    x2_y2 = Total_sum_squares - sum_squares

    sum_of_repeated_and_missing = x2_y2 / x_y

    first_number = (sum_of_repeated_and_missing + x_y ) / 2
    second_number = sum_of_repeated_and_missing - first_number

    repeated = 0
    missing = 0

    if first_number in arr:
        repeated = first_number
        missing = second_number
    else:
        repeated = second_number
        missing = first_number

    return repeated, missing

def repeat_and_missing_2(arr):
    global x, y
    n = len(arr)
    x = 0
    y = 0

    xor1 = arr[0]
    for i in range(1, n):
        xor1 = xor1 ^ arr[i]

    for i in range(1, n):
        xor1 = xor1 ^ i

    set_bit_no = xor1 & ~(xor1 - 1)

    for i in range(n):
        if (arr[i] & set_bit_no) != 0:
            x = x ^ arr[i]
        else:
            y = y ^ arr[i]
    for i in range(1, n + 1):
        if (i & set_bit_no) != 0:
            x = x ^ i
        else:
            y = y ^ i
    return y, x


if __name__ == "__main__":
    arr = [3, 1, 3]
    arr = [4, 3, 6, 2, 1, 1]
    repeat, missing = repeat_and_missing_1(arr)
    print(repeat, missing)
