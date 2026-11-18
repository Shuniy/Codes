def nthBitHavingMore1than0(n):
    if n <= 1:
        return ["1"]
    result = []
    helper(n, 0, 0, "", result)
    return result

def helper(n, n1, n0, op, result):
    if n <= 0:
        result.append(op)
        return
    helper(n - 1, n1 + 1, n0, op + "1", result)
    if n1 > n0:
        helper(n - 1, n1, n0 + 1, op + "0", result)
    return

print("Generate nth Bits having more 1 than 0", nthBitHavingMore1than0(3))