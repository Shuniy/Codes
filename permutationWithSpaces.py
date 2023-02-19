def permutationWithSpaces(string: str) -> list[str]:
    if len(string) <= 1:
        return [string]

    result = []
    output = string[0]
    solve(1, string, output, result)
    return result

def solve(currentIndex: int, input: str, output: str, result: list[str]):
    if currentIndex >= len(input):
        result.append(output)
        return
    solve(currentIndex + 1, input, output + input[currentIndex], result)
    solve(currentIndex + 1, input, output + "_" + input[currentIndex], result)

print("Permutation with Spaces are", permutationWithSpaces("abc"))