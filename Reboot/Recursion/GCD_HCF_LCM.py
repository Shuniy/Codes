# Calculate prime factors
import math

def primeFactors(n):
    if n <= 1:
        return n
    
    while n % 2 == 0:
        print(2, end=" ")
        n = n // 2
        
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            print(i, end=" ")
            n = n // i
            
    if n > 2:
        print(n)
    print()

n = 990
primeFactors(n)

# GCD (Greatest Common Divisor) or HCF (Highest Common Factor) of two numbers is the 
# largest number that divides both of them.
# GCD : 36 and 60 -> 12
def GCD(a, b):
    if a <= 0:
        return b
    
    if b <= 0:
        return a
    
    if a == b:
        return a
    
    if a > b:
        return GCD(a-b, b)
    return GCD(a, b - a)

# Euclidean GCD
"""
Basic Euclidean Algorithm for GCD 
The algorithm is based on the below facts. 

    If we subtract a smaller number from a larger (we reduce a larger number), 
    GCD doesn’t change. So if we keep subtracting repeatedly the larger of two, we end up with GCD.
    Now instead of subtraction, if we divide the smaller number, 
    the algorithm stops when we find remainder 0.
"""
def eucliedianGCD(a, b):
    if a == b:
        return a
    
    if a == 0:
        return b
    
    return eucliedianGCD(b % a, a)

# Extended euclidean gcd
"""
Extended Euclidean Algorithm: 
Extended Euclidean algorithm also finds integer coefficients x and y such that: 

  ax + by = gcd(a, b) 
  
The extended Euclidean algorithm updates results of gcd(a, b) using the results calculated by 
recursive call gcd(b%a, a). 
Let values of x and y calculated by the recursive call be x1 and y1. 
x and y are updated using the below expressions. 

x = y1 - ⌊b/a⌋ * x1
y = x1
"""
def extendedEuclideanGCD(a, b):
    if a == 0:
        return b, 0, 1
    
    GCD, x1, y1 = extendedEuclideanGCD(b % a, a)
    x = y1 - (b // a) * x1
    y = x1

    return GCD, x, y


# LCM (Least Common Multiple) of two numbers 
# is the smallest number which can be divided by both numbers.
# Basic formula is [a x b = LCM x HCF(GCD)]
def LCM(a, b):
    gcd = eucliedianGCD(a, b)
    return (a * b) // gcd

a = 36
b = 60
print(f"GCD of {a} and {b} is : ", GCD(a, b))
print(f"GCD of {a} and {b} is : ", eucliedianGCD(a, b))
GCD, x, y = extendedEuclideanGCD(a, b)
print(f"GCD of {a} and {b} is : ", GCD)
print(f"LCM of {a} and {b} is : ", LCM(a, b))
