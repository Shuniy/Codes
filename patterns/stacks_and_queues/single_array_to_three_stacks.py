"""
Three in One: Describe how you could use a single array to implement three stacks. 

Like many problems, this one somewhat depends on how well we'd like to support these stacks. If we're 
okay with simply allocating a fixed amount of space for each stack, we can do that. This may mean though 
that one stack runs out of space, while the others are nearly empty. 
Alternatively, we can be flexible in our space allocation, but this significantly increases the complexity of 
the problem.
"""

# Fixed Division
# For stack 1, we will use [0,  X/3). 
# For stack 2, we will use [ X ,  2X/3 ) 
# For stack 3, we will use [ 2X/3 , n)

# Time : O(1) : Space : O(n)
class FixedMultiStack:
    def __init__(self, stackSize, numOfStack = 3) -> None:
        # stack capacity provided by the user
        # means the size of indivisual stack
        self.stackCapacity = stackSize
        # values of the stack
        self.values = [None] * (stackSize * self.numOfStacks + 1)
        # sizes of each stack
        self.sizes = [] * (self.numOfStacks)
    
    # check if stack is full
    def isFull(self, stackNum):
        return self.sizes[stackNum - 1] == self.stackCapacity

    # returns the index of the top 
    def indexOfTop(self, stackNum):
        offset = self.stackCapacity * (stackNum - 1)
        size = self.sizes[stackNum - 1]
        return offset + size - 1

    # check if stack is empty
    def isEmpty(self, stackNum):
        return self.sizes[stackNum - 1] == 0

    # returns the top of the stack
    def peek(self, stackNum):
        if self.isEmpty(stackNum):
            print('Stack is Empty')
            return None
        return self.values[self.indexOfTop(stackNum)]

    # pushes element to stack
    def push(self, value, stackNum):
        if self.isFull(stackNum):
            print('Cant add to stack, stack is full, OVERFLOW!!!')
            return None

        self.sizes[stackNum] += 1
        self.values[self.indexOfTop(stackNum)] = value 

    # pop element from stack
    def pop(self, stackNum):
        if self.isEmpty(stackNum):
            print('Cant pop element, Nothing present in stack, UNDERFLOW!!!')
            return None

        topIndex = self.indexOfTop(stackNum)
        popedValue = self.values[topIndex]
        self.values[topIndex] = None
        self.sizes[stackNum] -= 1
        return popedValue

    

