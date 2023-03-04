def clearithbit(n, i):
    if n == 0:
        return 0
    
    mask = n ^ (1 << i)
    return n & mask

def clearithbit(n, i):
    if n == 0:
        return 0
    
    mask = ~(1 << i)
    return n & mask


n = 5
i = 1
print(clearithbit(n, i))
