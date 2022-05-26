from collections import deque

class Stack:
    def __init__(self) -> None:
        self.queue = deque()

    def push(self, x):
        tempDeque = deque([x])
        tempDeque.extend(self.queue)
        self.queue = tempDeque

    def pop(self):
        return self.queue.popleft()

    def top(self):
        return self.queue[0]

    def isEmpty(self):
        return len(self.queue) == 0
