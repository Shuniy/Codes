def countsetbits(n):
    count = 0
    while n:
        if n & 1:
            count += 1
            
        n = n >> 1
        
    return count

def countsetbitsfaster(n):
    count = 0
    while n:
        n = n & n - 1
        count += 1
        
    return count
    
n = 5
print(countsetbits(n))
print(countsetbitsfaster(n))
