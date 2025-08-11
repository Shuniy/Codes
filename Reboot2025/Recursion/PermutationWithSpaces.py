def permutationWithSpaces(string):
    output = []
    permutationWithSpacesHelper(string, 1, string[0], output)
    return output

def permutationWithSpacesHelper(string, i, result, output):
    if i >= len(string):
        output.append(result)
        return
    
    permutationWithSpacesHelper(
        string, i + 1, result + "_" + string[i], output)
    permutationWithSpacesHelper(
        string, i + 1, result + string[i], output)


print(permutationWithSpaces("abc"))