def letterCasePermutation(string: str) -> list[int]:
    if len(string) <= 0:
        return []

    result = []
    solve(0, string, "", result)
    return result

def solve(currentIndex: int, ip: str, op: str, result: list[int]):
    if currentIndex >= len(ip):
        result.append(op)
        return
    element: str = ip[currentIndex]
    if element.isdigit():
        solve(currentIndex + 1, ip, op + element, result)
    else:
        if element.islower():
            solve(currentIndex + 1, ip, op + element.upper(), result)
        else:
            solve(currentIndex + 1, ip, op + element.lower(), result)
        solve(currentIndex + 1, ip, op + element, result)
    return

print("Letter case permutation", letterCasePermutation("a1b2"))