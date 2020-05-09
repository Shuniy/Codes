"""
Given a number N, find number of set bits in binary representation of it
N = 13
Binary = 1101
Output = 3

Basic:
Count all set bits 1 by 1.
Last bit = N&1
ans += 1
left shift mask or right shift N
while N > 0 and update answer

2nd one:
Take log base 2 of the number and add 1

while n >0
n = n & n -1
number of times while loop is executing is the answer
"""

def countBits1(n):
    ans = 0
    while(n > 0):
        ans += n&1
        n = n >> 1
    return ans

def countBits2(n):
    ans = 0
    while n > 0:
        n = n & (n -1)
        ans += 1
    return ans

print(countBits1(13))
print(countBits2(13))
