class Stack(object):

    def __init__(self, initialItems: list[object] = []) -> None:
        self.stack = initialItems

    def __eq__(self, __value: object) -> bool:
        return self.stack == __value

    def push(self, value: object) -> None:
        self.stack.append(value)

    def pop(self) -> object:
        return self.stack.pop()

    def peek(self) -> object:
        return self.stack[-1]

    def size(self) -> int:
        return len(self.stack)


stack: Stack = Stack([1, 2, 3, 4, 56, 7, 8, 9, 6])
print(stack.peek())
print(stack.push(0))
print(stack.push(123))
print(stack.pop())
print(stack.size())
