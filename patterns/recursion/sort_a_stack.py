
def sortAStack(stack):
    if len(stack) == 1:
        return stack
    
    topElement = stack.pop()
    restSortedStack = sortAStack(stack)
    
    tempStack = []
    while restSortedStack and restSortedStack[-1] > topElement:
        tempStack.append(restSortedStack.pop())
    
    restSortedStack.append(topElement)
    while tempStack:
        restSortedStack.append(tempStack.pop())
    return restSortedStack

stack = [9,8,4,5,6,1,2,7,0,3]
        # [0,1,2,4,5,6,7,8,9, -> 3]

print(sortAStack(stack[:]))

def sortStack(stack):
    return sortStackHelper(stack)

def sortStackHelper(stack):
    if len(stack) <= 1:
        return stack
    
    topElement = stack.pop()
    restSortedStack = sortStackHelper(stack)
    return insert(restSortedStack, topElement)

def insert(stack, element):
    if len(stack) == 0:
        stack.append(element)
        return stack
    
    if stack[-1] <= element:
        stack.append(element)
        return stack
    
    topElement = stack.pop()
    stack = insert(stack, element)
    stack.append(topElement)
    return stack

print(sortStack(stack))