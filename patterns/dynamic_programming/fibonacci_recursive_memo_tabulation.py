# 0 1 1 2 3 5 8 13 21 ........
def fibonacciRecursive(n):
    if n <= 1:
        return 0
    
    if n == 2:
        return 1
    
    return fibonacciRecursive(n - 2) + fibonacciRecursive(n - 1)

def fibonacciIterative(n):
    if n <= 1:
        return 0
    
    first = 0
    second = 1
    result = first + second
    for _ in range(2, n - 1):
        first = second
        second = result
        result = first + second
        
    return result

def fibonacciMemoHelper(n, memo):
    if n <= 1:
        return 0
    
    if n == 2:
        return 1
    
    if memo[n] > 0:
        return memo[n]
    
    first = fibonacciMemoHelper(n - 1, memo)
    second = fibonacciMemoHelper(n - 2, memo)
    memo[n] = first + second
    return memo[n]

def fibonacciMemo(n):
    if n <= 1:
        return 0
    
    memo = [0] * (n + 1)
    memo[1] = 1
    return fibonacciMemoHelper(n, memo)
    
def fibonacciDP(n):
    if n <= 1:
        return 1
    
    if n == 2:
        return 1
    
    dp = [0, 1]
    for i in range(2, n):
        dp.append(dp[i - 2] + dp[i - 1])
    return dp[n - 1]

n = 8
print(fibonacciRecursive(n))
print(fibonacciIterative(n))
print(fibonacciMemo(n))
print(fibonacciDP(n))