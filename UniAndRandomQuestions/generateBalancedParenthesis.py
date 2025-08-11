def generateBalancedParenthesis(n: int) -> list[str]:
    if n <= 0:
        return []
    open = closed = n
    result = []
    helper(open, closed, "", result)
    return result

def helper(open, closed, op, result):
    if open <= 0 and closed <= 0:
        result.append(op)
        return

    if open > 0:
        helper(open - 1, closed, op + "(", result)
    if closed > open and closed > 0:
        helper(open, closed - 1, op + ")", result)
    return


print("Balanced Parenthesis", generateBalancedParenthesis(3))