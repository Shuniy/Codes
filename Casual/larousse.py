
"""
Larousse Method
"""

def multiply(x, y):
    small = 0
    big = 0
    total = 0
    if x < y:
        small = x
        big = y
    else:
        small = y
        big = x
    while small >= 1:
        small = small // 2;
        big = big * 2;
        if small % 2 != 0:
            total += big
    return total;

print("Enter two positive numbers : ")
a = input()
b = input()

print("Product of two numbers is : ")
print(multiply(int(a), int(b)))
        