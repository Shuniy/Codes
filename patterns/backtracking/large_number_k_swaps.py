def large_number_k_swaps(s: str, k: int):
    """
    Find the largest possible number given a list of digits and number of swaps k.
    
    Parameters:
    s (str): The list of digits.
    k (int): The number of swaps allowed.
    
    Returns:
    int: The maximum possible number found.
    """
    return large_number_k_swaps_helper(k, 0, list(s), int(s))

def large_number_k_swaps_helper(k: int, index: int, current: list, result: int):
    """
    Helper function for finding the largest possible number given a list of digits and number of swaps k.
    
    Parameters:
    k (int): The number of swaps left.
    index (int): The index of the current list of digits.
    current (list): The current list of digits.
    result (int): The maximum possible number found so far.
    
    Returns:
    int: The maximum possible number found.
    """
    if k == 0 or index == len(current):
        return result
    mx = max(current[index:])
    for i in range(index, len(current)):
        if current[index] >= current[i] or current[i] != mx:
           continue
        current[index], current[i] = current[i], current[index]
        result = max(result, int("".join(current)))
        result = max(result, large_number_k_swaps_helper(k - 1, index + 1, current, result))
        current[index], current[i] = current[i], current[index]
    return result

# test cases
print(large_number_k_swaps("123", 2))
print(large_number_k_swaps("122345", 2))
print(large_number_k_swaps("4321", 2))
print(large_number_k_swaps("010", 1))
print(large_number_k_swaps("10102", 2))
print(large_number_k_swaps("1234567", 4))
print(large_number_k_swaps("1234567", 2))
