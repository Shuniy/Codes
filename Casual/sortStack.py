"""
Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use 
an additional temporary stack, but you may not copy the elements into any other data structure 
(such as an array). The stack supports the following operations: push, pop, peek, and is Empty
"""
# way is to keep inserting the element into the seconday stack
# and the moment we find the element or peek greater than the element
# we are about to insert we push that peek to the stack

# time : O(n**2) : space : O(n)
def sortStack(stack):
    tempStack = []

    while len(stack):
        # insert each element in stack in sorted order to tempStack
        temp = stack.pop()
        while len(tempStack) and stack[-1] > temp:
            stack.append(temp)

        tempStack.append(temp)

    # not to push the rest into stack
    while len(tempStack):
        stack.append(tempStack.pop())

    return stack

