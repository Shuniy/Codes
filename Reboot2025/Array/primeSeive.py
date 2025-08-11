# Sieve of Eratosthenes is used to find all the prime numbers in range

import math

def primeNumbers(n):
    if n <= 1:
        return 0
    
    result = [2]
    
    for i in range(3, n + 1, 2):
        passed = True
        for j in range(2, int(math.sqrt(i) + 1)):
            if i % j == 0:
                passed = False
                break
        if passed:
            result.append(i)
            
    return result

def primeNumbersSeive(n):
    primes = [True] * (n + 1)
    primes[0] = False
    primes[1] = False
    p = 2
    
    while p * p <= n:
        if primes[p] == True:
            for i in range(p * p, n + 1, p):
                primes[i] = False
            p += 1
            
    result = [i for i in range(n + 1) if primes[i]]
    return result 

print(primeNumbers(30))
print(primeNumbersSeive(30))
