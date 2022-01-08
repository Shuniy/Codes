def replacebits(n, i, j, val):
    # clear bits in range
    jmask = -1 << j + 1
    imask = (1 << i) - 1
    num = n & (jmask | imask)
    
    mask = val << i
    return num | mask

n = 15
i = 1
j = 3
val = 2
print(replacebits(n, i, j, val))