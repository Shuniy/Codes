class Stack:
    # LIFO Stack implementation using a Python list as underlying storage.
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def isEmpty(self):
        return len(self.data) == 0

    def push(self, e):
        self.data.append(e)

    def peek(self):
        return self.data[-1]

    def pop(self):
        return self.data.pop()


def operatorpriority(x):
    if x in "+-":
        return 1
    elif x in "*/":
        return 2
    elif x in "^":
        return 3
    return 0


def polishnotation(A):
    # Converts Infix to Prefix Notation
    stack = Stack()
    A = '(' + A + ')'
    output = ""
    for c in A[::-1]:
        print(c)
        if c.isnumeric():
            output += c
        elif c == ")":
            stack.push(c)
        elif c in "+-*/^":
            if c == "^":
                while operatorpriority(c) <= operatorpriority(stack.peek()):
                    output += stack.pop()
            else:
                while operatorpriority(c) < operatorpriority(stack.peek()):
                    output += stack.pop()
            stack.push(c)
        elif c == "(":
            while not stack.isEmpty():
                c1 = stack.pop()
                if c1 == ')':
                    break
                output += c1
    while not stack.isEmpty():
        output += stack.pop()
    return output


print(polishnotation('(3+4)*(5+6)'))
