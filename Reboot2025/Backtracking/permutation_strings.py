def permutation_strings(string):
    """
    Generates all permutations of the input string using backtracking.

    Parameters:
    string (str): The input string for which permutations are to be generated.

    Returns:
    list: A list of all possible permutations of the input string.
    """

    result = []
    permutation_strings_helper(string, 0, list(string), result)
    return result

def permutation_strings_helper(string, index, current, result):
    """
    Helper function for permutation_strings.

    Parameters:
    string (str): The input string for which permutations are to be generated.
    index (int): The current index in the string.
    current (list): The current list of characters.
    result (list): The list of permutation strings.

    Returns:
    None
    """
    if index == len(string):
        result.append("".join(current))
        return
    
    for i in range(index, len(string)):
        current[index], current[i] = current[i], current[index]
        permutation_strings_helper(string, index + 1, current, result)
        current[index], current[i] = current[i], current[index]

def permutation_strings_recursive(string):
    """
    Recursively generates all permutations of the input string.

    Parameters:
    string (str): The input string for which permutations are to be generated.

    Returns:
    list: A list of all possible permutations of the input string.
    """

    result = []
    permutation_strings_helper_recursive(string, "", result)
    return result

def permutation_strings_helper_recursive(ip, op, result):
    """
    Helper function for permutation_strings_recursive.
    It takes three arguments: ip(string input), op(string output), result(list of result strings)
    and returns nothing.
    It will generate all the permutation of the string ip and will append it in the result list.
    """
    if len(ip) == 0:
        result.append(op)
        return
    
    for i in range(len(ip)):
        newIp = ip[:i] + ip[i + 1:]
        newOp = op + ip[i]
        permutation_strings_helper_recursive(newIp, newOp, result)


# test cases
print(permutation_strings("abc"))
print(permutation_strings("xy"))
print(permutation_strings("abcd"))
print(permutation_strings("xyx"))
print(permutation_strings("abcde"))

print(permutation_strings_recursive("abc"))
print(permutation_strings_recursive("xy"))
print(permutation_strings_recursive("abcd"))
print(permutation_strings_recursive("xyx"))
print(permutation_strings_recursive("abcde"))
