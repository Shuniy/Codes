def n_digit_numbers_increasing(n):
    """
    Generate all n-digit increasing numbers.

    Parameters:
    n (int): The number of digits.

    Returns:
    list: A list of n-digit increasing numbers.
    """
    if n <= 1:
        return [i for i in range(10)]
    result = []
    n_digit_numbers_increasing_helper(n, [], result)
    return result

def n_digit_numbers_increasing_helper(n, current, result):
    """
    Helper function for NDigitNumbersIncreasing.

    Parameters:
    n (int): The number of digits left to append.
    current (list): The current list of digits.
    result (list): The list of results.

    Returns:
    None
    """
    if n == 0:
        result.append(int("".join(current)))
        return
    for i in range(1, 10):
        if current and current[-1] >= str(i):
            continue
        current.append(str(i))
        n_digit_numbers_increasing_helper(n - 1, current, result)
        current.pop()

# test cases
print(n_digit_numbers_increasing(1))
print(n_digit_numbers_increasing(2))
print(n_digit_numbers_increasing(3))
