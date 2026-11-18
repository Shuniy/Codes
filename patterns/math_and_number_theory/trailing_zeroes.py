import math as m

"""
Find trailing zeroes are present in a numbers factorial

so we have to calculate just occurences of 5 and 2 which multiplies to 10.
that is to calculate 2 powers like 2,4,6,8 .... and then if it multiplies by 5.

use floor  and divide with each digit and then add

2 powers will not be calculated as they automatically make tham 10
"""

def trailing_zeroes(n):
    ans = 0
    # Initial power of 5
    p = 5
    while((n/p) > 0):
        ans += (n/p)
        p *= 5
    return m.ceil(ans)

assert trailing_zeroes(100) == 25