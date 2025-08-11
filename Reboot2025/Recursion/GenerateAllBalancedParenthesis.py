
def generateAllBalancedParenthesis(n):
    output = []
    generateAllBalancedParenthsisHelper(n, n, "", output, 0)
    return output


def generateAllBalancedParenthsisHelper(openCount, closedCount, result, output, balanced):
    if openCount == 0 and closedCount == 0 and balanced == 0:
        output.append(result)
        return

    if balanced >= 0:
        if openCount > 0:
            generateAllBalancedParenthsisHelper(
                openCount - 1, closedCount, result + "(", output, balanced + 1)
        if closedCount > 0:
            generateAllBalancedParenthsisHelper(
                openCount, closedCount - 1, result + ")", output, balanced - 1)


print(generateAllBalancedParenthesis(3))
