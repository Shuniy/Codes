def clearbitsinrange(n, i, j):
    jmask = -1 << j + 1
    imask = (1 << i) - 1
    
    return n & (imask | jmask)


n = 29
i = 1
j = 3
print(clearbitsinrange(n, i, j))