
def deleteMiddleElementOfStackHelper(stack, k):    
    if k == 1:
        stack.pop()
        return stack
    
    topElement = stack.pop()
    stack = deleteMiddleElementOfStackHelper(stack, k - 1)
    stack.append(topElement)
    return stack

def deleteMiddleElementOfStack(stack):
    if len(stack) <= 1:
        return []
    k = 0
    if len(stack) % 2 == 0:
        k = len(stack) // 2
    else:
        k = len(stack) // 2 + 1
    
    return deleteMiddleElementOfStackHelper(stack, k)

stack1 = [1, 2, 3, 5, 6, 7]
stack2 = [1, 2, 3, 4, 5, 6, 7, 8]
stack3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(deleteMiddleElementOfStack(stack1))
print(deleteMiddleElementOfStack(stack2))
print(deleteMiddleElementOfStack(stack3))
