"""
Queue via Stacks: Implement a MyQueue class which implements a queue using two stacks.
"""

# major operations are going to be done on stack oldest
class Queue:
    def __init__(self) -> None:
        self.stackOldest = []
        self.stackNewest = []

    def size(self):
        return len(self.stackNewest) + len(self.stackOldest)

    def shiftStacks(self):
        if len(self.stackOldest) == 0:
            while len(self.stackNewest):
                self.stackOldest.append(self.stackNewest.pop())

    #  peek in queue returns the oldest element
    def peek(self):
        self.shiftStacks()
        return self.stackOldest[-1]

    def push(self, x):
        self.stackNewest.append(x)

    def pop(self):
        self.shiftStacks()
        return self.stackOldest.pop()
