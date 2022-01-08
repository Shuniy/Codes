# Time : O(2^n), Space : O(n)
def fibonacci_recursive(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n == 0:
        print("Invalid Input")
        return None
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Time : O(n), Space : O(n)
def fibonacci_array(n):
    fibonacci = []
    fibonacci.append(0)
    fibonacci.append(1)
    for i in range(2, n):
        fibonacci.append(fibonacci[i - 2] + fibonacci[i - 1])

    return fibonacci[n - 1]

# Time : O(n), Space : O(1)
def fibonacci_iterative(n):
    num1 = 0
    num2 = 1
    sum = 0
    for i in range(n - 2):
        sum = num1 + num2
        num1 = num2
        num2 = sum
    return num2

print(fibonacci_recursive(5))
print(fibonacci_array(5))
print(fibonacci_iterative(5))