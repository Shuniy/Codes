def printUniqueSubsets(string: str) -> list[str]:
    if len(string) <= 1:
        return [string]

    result = set()
    uniqueSubsetsHelper(0, string, "", result)
    return list(result)


def uniqueSubsetsHelper(currentIndex: int, input: str, output: str, result: set[str]):
    if currentIndex >= len(input):
        result.add(output)
        return
    uniqueSubsetsHelper(currentIndex + 1, input, output + input[currentIndex], result)
    uniqueSubsetsHelper(currentIndex + 1, input, output, result)
    return

print("All Unique Subsets", printUniqueSubsets("abcba"))
