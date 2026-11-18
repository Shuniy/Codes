def EvaluateExpression(expression: str) -> bool:
    """
    Evaluate a given boolean expression and return the result.

    Args:
        expression (str): The expression to be evaluated.

    Returns:
        bool: The result of the evaluation.
    """
    memo = {}
    return EvaluateExpressionHelper(expression, 0, len(expression) - 1, True, memo)

def evaluate(b1, b2, op):
    if op == '&':
        return b1 & b2
    elif op == '|':
        return b1 | b2
    return b1 ^ b2

def EvaluateExpressionHelper(expression: str, i: int, j: int, requirement: bool, memo: dict) -> bool:
    """
    A helper function to evaluate a boolean expression and return the result.

    Args:
        expression (str): The expression to be evaluated.
        i (int): The starting index of the expression.
        j (int): The ending index of the expression.
        memo (dict): A dictionary to store the memoized results of subproblems.

    Returns:
        bool: The result of the evaluation.
    """
    if (i, j, requirement) in memo:
        return memo[(i, j, requirement)]

    if i > j:
        return False
    
    if i == j:
        if requirement:
            return expression[i] == 'T'
        else:
            return expression[i] == 'F'

    ans = 0
    for k in range(i + 1, j, 2):
        leftT = EvaluateExpressionHelper(expression, i, k - 1, True, memo)
        leftF = EvaluateExpressionHelper(expression, i, k - 1, False, memo)
        rightT = EvaluateExpressionHelper(expression, k + 1, j, True, memo)
        rightF = EvaluateExpressionHelper(expression, k + 1, j, False, memo)

        if expression[k] == '&':
            if requirement:
                ans += leftT * rightT
            else:
                ans += leftF * rightF + leftF * rightT + leftT * rightF
        elif expression[k] == '|':
            if requirement:
                ans += leftT * rightT + leftF * rightT + leftT * rightF
            else:
                ans += leftF * rightF
        elif expression[k] == '^':
            if requirement:
                ans += leftT * rightF + leftF * rightT
            else:
                ans += leftF * rightF + leftT * rightT

    memo[(i, j, requirement)] = ans
    return memo[(i, j, requirement)]
    

# test cases
print(EvaluateExpression("T|F&F|T"))
print(EvaluateExpression("T&T|F|T"))
print(EvaluateExpression("T&T|F|T"))
print(EvaluateExpression("T|T&T|F|F|F"))
print(EvaluateExpression("T|T&T|F|F|F"))
print(EvaluateExpression("T|T&F^T"))
    