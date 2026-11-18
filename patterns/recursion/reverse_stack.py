def reverseStack(stack):
    n = len(stack)
    return reverseStackHelper(stack, n)

def reverseStackHelper(stack, n):
    if n <= 1:
        return stack
    
    topElement = stack.pop()
    restSortedStack = reverseStackHelper(stack, n - 1)
    return insert(restSortedStack, topElement)

def insert(stack, element):
    if len(stack) <= 0:
        stack.append(element)
        return stack
    
    topElement = stack.pop()
    stack = insert(stack, element)
    stack.append(topElement)
    return stack

arr = [1,2,3,4,5,6,7,8,9,0]
print(reverseStack(arr))