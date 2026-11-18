def reverse_string(input):
    if len(input) <= 1:
        return input
    else:
        print(input)
        return reverse_string(input[1:]) + input[0]


print("Pass" if ("" == reverse_string("")) else "Fail")
print("Pass" if ("cba" == reverse_string("abc")) else "Fail")
