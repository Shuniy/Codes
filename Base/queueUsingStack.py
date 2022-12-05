class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.items.pop

class Queue:
    def __init__(self):
        self.stack = Stack()

    def size(self):
        return self.stack.size()

    def enqueue(self, value):
        self.stack.push(value)

    def dequeue(self):
        temp_stack = Stack()
        temp_stack_second = Stack()

        for i in range(self.size() - 1):
            temp_stack.push(self.stack.pop())

        for i in range(temp_stack.size()):
            temp_stack_second.push(temp_stack.pop())

        dequeued_value = self.stack.pop()
        self.stack = temp_stack_second
        return dequeued_value

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Test size
print("Pass" if (q.size() == 3) else "Fail")

# Test dequeue
print("Pass" if (q.dequeue() == 1) else "Fail")

# Test enqueue
q.enqueue(4)
print("Pass" if (q.dequeue() == 2) else "Fail")
print("Pass" if (q.dequeue() == 3) else "Fail")
print("Pass" if (q.dequeue() == 4) else "Fail")
q.enqueue(5)
print("Pass" if (q.size() == 1) else "Fail")
