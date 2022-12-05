def clearlastibits(n, i):
    mask = -1 << i
    return n & mask

n = 5
i = 2
print(clearlastibits(n, i))