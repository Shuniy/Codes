def power(a, b):
    if b == 0:
        return 1
    if b <= 1:
        return a
    
    return a * power(a, b - 1)

def power(a, b):
    if b == 0:
        return 1
    
    halfPower = power(a, b // 2)
    fullPower = halfPower * halfPower
    if b % 2:
        return a * fullPower
    else:
        return fullPower

print(power(2, 3))