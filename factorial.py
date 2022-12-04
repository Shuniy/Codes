import sys

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

def multilpy(x, result, result_size):
    carry = 0
    i = 0
    while i < result_size:
        product = result[i] * x + carry
        result[i] = product % 10
        carry = product / 10
        i = i + 1

    while(carry):
        result[result_size] = carry % 10
        carry = carry / 10
        result_size = result_size + 1
    return result_size

def largeFactorial(n):
    result = [None] * 500
    result[0] = 1
    result_size = 1
    x = 2
    while x <= n:
        result_size = multilpy(x, result, result_size)
        x = x + 1
    print("Factorial of given number is")
    i = result_size-1
    while i >= 0:
        sys.stdout.write(str(result[i]))
        sys.stdout.flush()
        i = i - 1


print("Pass" if (1 == factorial(0)) else "Fail")
print("Pass" if (1 == factorial(1)) else "Fail")
print("Pass" if (120 == factorial(5)) else "Fail")

largeFactorial(120)