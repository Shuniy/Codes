def phone_keypad_problem(digits: str):
    """
    Returns a list of strings, where each string is a possible combination of
    characters that can be typed by pressing the given sequence of digits on
    a phone keypad.  The mapping of digits to characters is given by the chars
    dictionary.

    :param digits: A string of digits
    :return: A list of possible strings
    """
    chars = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"],
    }
    result = []
    phone_keypad_problem_helper(digits, chars, 0, "", result)
    return result

def phone_keypad_problem_helper(digits: str, chars: dict, index: int, current: str, result: list):
    """
    Helper function for phone_keypad_problem.

    Parameters:
        digits (str): The input string of digits.
        chars (dict): A dictionary mapping each digit to its corresponding characters.
        index (int): The index of the current digit in the input string.
        current (str): The current string of characters.
        result (list): The list of possible character strings.

    Returns:
        None
    """
    
    if index == len(digits):
        if current:
            result.append(current)
        return
    
    for char in chars[int(digits[index])]:
        current += char
        phone_keypad_problem_helper(digits, chars, index + 1, current, result)
        current = current[:-1]

# test cases
print(phone_keypad_problem("23"))
print(phone_keypad_problem("234"))
print(phone_keypad_problem("2"))
print(phone_keypad_problem("3"))
print(phone_keypad_problem(""))
