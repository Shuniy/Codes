def getithbit(n, i):
    if n == 0:
        return 0
    
    mask = 1 << i
    return 1 if n & mask else 0

n = 5
i = 1
print(getithbit(n, i))