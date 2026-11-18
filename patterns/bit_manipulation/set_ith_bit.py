def setithbit(n, i):
    
    mask = 1 << i
    return n | mask
 
n = 5
i = 1
print(setithbit(n, i))
