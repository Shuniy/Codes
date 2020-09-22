"""
Euclids Theorem
GCD(a , b) = GCD(b, a % b)

GCD(a, 0) = a
"""
def GCD(a, b):
    return a if b == 0 else GCD(b, a % b)

print('HCF')
print(GCD(3, 12))
print("LCM")
print((3 * 12) / GCD(3, 12))