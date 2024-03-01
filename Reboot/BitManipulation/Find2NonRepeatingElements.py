def find2NonRepeatingElements(arr: list[int]):
    sums = 0
    # All the repeated elements when xor is done will be resulted to 0
    # So, only 2 elements will remain, and the xor will be the xor of those 2 elements
    for item in arr:
        sums ^= item

    # Now we will select one element, the one whose rightmost bit is set, i,e 0,1
    # Taking two's complement of the sums, and subtracting it with the sum, will give 1 to us
    sums = sums & -sums
    # Now there are two numbers below
    # if the sums, which is 1 of the two element is used and & with the other operators
    # case 1: since sums is one of the number with negation, xor with one of the number will give 1 result number to us
    # case 2: other number we will get if sums & item is greater than 0, so we will xor other number to negate it and get the unique number
    sum1 = 0
    sum2 = 0
    for item in arr:
        if (sums & item) > 0:
            sum1 = sum1 ^ item
        else:
            sum2 = sum2 ^ item
    return (sum1, sum2)


print(find2NonRepeatingElements([2, 3, 7, 9, 11, 2, 3, 11]))
