"""
Stack Min: How would you design a stack which, in addition to push and pop, has a function min 
which returns the minimum element? Push, pop and min should all operate in 0(1) time. 
"""
class Node:
    def __init__(self, value, minimum, maximum) -> None:
        self.value = value 
        self.min = minimum
        self.max = maximum

class Stack:
    def __init__(self, values = []) -> None:
        self.stack = values
        self.min = None
        self.length = 0
        self.top = None
        self.max = None

    def push(self, value):
        if self.min and value < self.min:
            self.min = value
        elif self.max and value >= self.max:
            self.max = value
        else:
            self.min = value
            self.max = value

        newNode = Node(value, self.min, self.max)
        self.stack.append(newNode)
        self.top = newNode.value
        self.length += 1

    def pop(self, value):
        if self.isEmpty():
            self.min = None
            self.max = None
            return None

        topNode = self.stack.pop()
        self.length -= 1
        self.min = self.stack[-1].min
        self.max = self.stack[-1].max
        self.top = self.stack[-1].value
        return topNode.value

    def getMin(self):
        return self.min

    def getMax(self):
        return self.max

    def size(self):
        return self.length

    def isEmpty(self):
        return self.length == 0

    def peek(self):
        self.top = self.stack[-1].value
        return self.stack[-1].value


    
