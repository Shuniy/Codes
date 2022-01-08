"""
Stack  of Plates: Imagine a (literal) stack of plates.  If  the stack gets too high,  it might topple. 
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some 
threshold. Implement a data structure SetOfStacks that mimics this. SetO-fStacks should be 
composed of several stacks and should create a new stack once the previous one exceeds capacity. 
SetOfStacks. push() and SetOfStacks. pop()  should behave identically to a single stack 
(that is, pop () should return the same values as it would if there were just a single stack). 
FOLLOW UP 
Implement a function popAt ( int  index) which performs a pop operation on a specific sub-stack. 
Hints:#64, #87
"""

class SetOfStacks:
    def __init__(self, capacity) -> None:
        self.stacks = []
        self.capacity = capacity

    def getLastStack(self):
        if len(self.stacks) == 0:
            return None

        return self.stacks[-1]

    def isEmpty(self):
        last = self.getLastStack()
        return last == None or len(last) == 0

    def push(self, value):
        last = self.getLastStack()
        if last is not None and len(last) != self.capacity:
            last.append(value)
        else:
            newStack = []
            newStack.append(value)
            self.stacks.append(newStack)

    def pop(self):
        last = self.getLastStack()
        if last == None:
            return

        value = last.pop()
        if len(last) == 0:
            self.stacks.pop()
        return value

