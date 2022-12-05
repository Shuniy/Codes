import math

# Time : O(n)
def factorialRecursive(n):
    if n <= 1:
        return 1
    
    return n * factorialRecursive(n - 1)

def factorialIterative(n):
    if n <= 1:
        return 1
    
    result = 1
    while n:
        result *= n
        n -= 1
        
    return result

def factorialOfLargeNumber(n):
    if n <= 1:
        return 1
    
    result = [None] * 500
    result[0] = 1
    resultSize = 1
    currentNum = 2
    while currentNum <= n:
        resultSize = factorialOfLargeNumberHelper(result, currentNum, resultSize)
        currentNum += 1
    
    answer = ""
    for i in range(resultSize - 1, -1, -1):
        answer += str(result[i])
        
    return int(answer)        

def factorialOfLargeNumberHelper(result, currentNum, resultSize):
        
    index = 0
    carry = 0
    while index < resultSize:
        product = result[index] * currentNum + carry
        result[index] = product % 10
        carry = product // 10
        index += 1
        
    while carry:
        result[resultSize] = carry % 10
        carry = carry // 10
        resultSize += 1
    
    return resultSize

n = 10
print(factorialRecursive(n))
print(factorialIterative(n))
print(math.factorial(n))
print(factorialOfLargeNumber(n))