"""
Compute number of prime numbers between two numbers
https://www.youtube.com/watch?time_continue=435&v=8sniiDbfPK4&feature=emb_logo
"""

def sieve(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    for p in range(n + 1):
        if prime[p]:
            print(p)
    return prime

prime = sieve(100)
for i in range(len(prime)):
    if prime[i]:
        prime[i] = 1
    else:
        prime[i] = 0
size = len(prime)
csum = [0] * size

for i in range(1, size):
    csum[i] = csum[i - 1] + prime[i]

q = int(input())
while q:
    a = b = 0
    a, b = int(input().split())
    print(csum[b] - csum[a - 1])
