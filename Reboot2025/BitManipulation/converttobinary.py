def converttobinary(n):
    ans = 0
    p = 1
    
    while n:
        lastbit = n & 1
        ans += p * lastbit
        p *= 10
        n = n >> 1
        
    return ans

n = 5
print(converttobinary(n))