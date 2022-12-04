
def letterCasePermutation(string: str):
    output = []
    letterCasePermutationHelper(string, 0, "", output)
    return output

def letterCasePermutationHelper(string: str, i, result, output):
    if i >= len(string):
        output.append(result)
        return
    
    if string[i].isdigit():
        letterCasePermutationHelper(string, i + 1, result + string[i], output)
    else:
        letterCasePermutationHelper(string, i + 1, result + string[i], output)
        letterCasePermutationHelper(
            string, i + 1, result + string[i].swapcase(), output)

string = "a1B2"
print(letterCasePermutation(string))