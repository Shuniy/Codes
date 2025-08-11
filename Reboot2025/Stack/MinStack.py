class MinStack:

    def __init__(self):
        self.stack = []
        self.minElement = float("inf")

    def push(self, val: int) -> None:
        if val < self.minElement:
            self.stack.append(2 * val - self.minElement)
            self.minElement = val
        else:
            self.stack.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        if popped < self.minElement:
            self.minElement = 2 * self.minElement - popped

    def top(self) -> int:
        if self.stack[-1] < self.minElement:
            return self.minElement
        else:
            return self.stack[-1]

    def getMin(self) -> int:
        return self.minElement


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()