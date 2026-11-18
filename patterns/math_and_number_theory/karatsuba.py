"""
Time Complexity: Time complexity of the above solution is O(nlog23) = O(n1.59).

X =  Xl*2^n/2 + Xr    [Xl and Xr contain leftmost and rightmost n/2 bits of X]
Y =  Yl*2^n/2 + Yr    [Yl and Yr contain leftmost and rightmost n/2 bits of Y]

XY = (Xl*2^n/2 + Xr)(Yl*2^n/2 + Yr)
   = 2^n XlYl + 2^n/2(XlYr + XrYl) + XrYr
   
XlYr + XrYl = (Xl + Xr)(Yl + Yr) - XlYl- XrYr

XY = 2^n XlYl + 2^n/2 * [(Xl + Xr)(Yl + Yr) - XlYl - XrYr] + XrYr

XY = 2^2ceil(n/2) XlYl + 2^ceil(n/2) * [(Xl + Xr)(Yl + Yr) - XlYl - XrYr] + XrYr   
"""

def karatsuba(x,y):
    if len(str(x)) or len(str(y)) == "1":
        return x*y
    else:
        n = max(len(str(x)), len(str(y)))
        nby2 = n/2
        a = x / 10**(nby2)
        b = x % 10**(nby2)
        c = y / 10**(nby2)
        d = y % 10**(nby2)
        
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        ad_plus_bc = karatsuba(a+b, c+d) - ac - bd
        
        prod = ac * 10**(n) + (ad_plus_bc * 10**(nby2)) + bd
        
    return prod    

print("Enter two numbers : ")
a = int(input())
b = int(input())
print("Product of two numbers is : ")
print(karatsuba(a, b))