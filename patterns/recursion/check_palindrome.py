def is_palindrome(input):
    if len(input) <= 1:
        return True
    elif len(input) == 2:
        return input[0] == input[1]
    else:
        output = (input[0] == input[len(input) - 1]) & (is_palindrome(input[1:len(input) - 1]))
        return output


print("Pass" if (is_palindrome("")) else "Fail")
print("Pass" if (is_palindrome("a")) else "Fail")
print("Pass" if (is_palindrome("madam")) else "Fail")
print("Pass" if (is_palindrome("abba")) else "Fail")
print("Pass" if not (is_palindrome("ZippySphinx")) else "Fail")
