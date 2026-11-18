def permutationWithCaseChange(string: str):
    output = []
    permutationWithCaseChangeHelper(string, 0, "", output)
    return output

def permutationWithCaseChangeHelper(string, i, result, output):
    if i >= len(string):
        output.append(result)
        return
    
    permutationWithCaseChangeHelper(string, i + 1, result + string[i], output)
    permutationWithCaseChangeHelper(string, i + 1, result + string[i].swapcase(), output)

string = "aB"
print(permutationWithCaseChange(string))
