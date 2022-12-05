"""
Sieve of Eratosthenes : Generate an array with prime numbers.
Other optimizations:
https://www.youtube.com/watch?time_continue=1187&v=yB57bcffJo4&feature=emb_logo
"""


def sieve_fast(n):
    size = 100000000000
    prime = [1 for i in range(size)]
    for i in range(3, size, 2):
        prime[i] = 1
    for i in range(3, size, 2):
        if prime[i] == 1:
            j = i
            for j in range(size, j + i):
                prime[j] = 0

    prime[2] = 1
    prime[1] = prime[0] = 0
    for p in range(size):
        if prime[p] == 1:
            print(p)

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
sieve(100)
