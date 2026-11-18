def reverseStack(stack: list[int]) -> list[int]:
    if len(stack) <= 1:
        return stack
    topElement = stack.pop()
    reversedStack = reverseStack(stack)
    return [topElement] + reversedStack

stack = [1,2,3,4,5,6,7,8,9]
print("Reversed Stack", reverseStack(stack))