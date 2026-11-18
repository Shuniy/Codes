def deleteMiddleOfStack(stack: list[int]) -> list[int]:
    if len(stack) <= 1:
        return []
    middleElement = stack[len(stack) // 2]
    print("Middle element was", middleElement)
    return deleteMiddleHelper(stack, middleElement)

def deleteMiddleHelper(stack: list[int], middleElement: int) -> list[int]:
    if len(stack) <= 0:
        return stack

    topElement = stack.pop()
    if topElement == middleElement:
        return stack
    else:
        result = deleteMiddleHelper(stack, middleElement)
        result.append(topElement)
        return result


stack = [1,2,3,4,5,6,7,8,9,0]
print("Middle Element Deleted and stack is", deleteMiddleOfStack(stack))

stack = [1,2,3,4,5,6,7,8,9]
print("Middle Element Deleted and stack is", deleteMiddleOfStack(stack))