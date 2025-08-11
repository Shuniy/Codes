def subsets(string: str) -> list[str]:
    if len(string) <= 1:
        return [string]
    
    output = []
    solve(0, string, "", output)
    return output

def solve(currentIndex: int, input: str, output: str, result: list[str]):
    if currentIndex >= len(input):
        result.append(output)
        return
    solve(currentIndex + 1, input, output + input[currentIndex], result)
    solve(currentIndex + 1, input, output, result)
    return

print("All Subsets or subsequences", subsets("abc"))