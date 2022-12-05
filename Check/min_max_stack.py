# We want all in constant time and space

class MinMaxStack:
    def __init__(self) -> None:
        self.min_max_stack = []
        self.stack = []

    def peek(self):
        return self.stack[len(self.stack) - 1] # self.stack[-1]

    def pop(self):
        self.min_max_stack.pop()
        return self.stack.pop()

    def push(self, number):
        new_min_max = {"min" : number, "max" : number}

        if len(self.min_max_stack):
            last_min_max = self.min_max_stack[len(self.min_max_stack) - 1]

            new_min_max['min'] = min(last_min_max['min'], number)
            new_min_max['max'] = max(last_min_max['max'], number)

        self.min_max_stack.append(new_min_max)
        self.stack.append(number)

    def get_minimum(self):
        return self.min_max_stack[len(self.min_max_stack) - 1]['min']

    def get_maximum(self):
        return self.min_max_stack[len(self.min_max_stack) - 1]['max']