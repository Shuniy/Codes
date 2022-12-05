def powerof2(n):
    return False if n & n - 1 else True

n = 8
print(powerof2(n))
n = 7
print(powerof2(n))