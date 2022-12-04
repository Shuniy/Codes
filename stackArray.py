"""
Functionality
Our goal will be to implement a Stack class that has the following behaviors:

push - adds an item to the top of the stack
pop - removes an item from the top of the stack (and returns the value of that item)
size - returns the size of the stack
top - returns the value of the item at the top of stack (without removing that item)
is_empty - returns True if the stack is empty and False otherwise
"""

class Stack(object):
    def __init__(self, initial_size = 10):
        self.arr = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.num_elements = 0

    def push(self, element):
        if self.next_index == len(self.arr):
            self.handle_stack_capacity_full()
        self.arr[self.next_index] = element
        self.next_index += 1
        self.num_elements += 1

    def handle_stack_capacity_full(self):
        old_arr = self.arr
        self.arr = [0 for _ in range(2 * len(old_arr))]
        for index, element in enumerate(old_arr):
            self.arr[index] = element

    def size(self):
        return self.next_index

    def is_empty(self):
        return self.next_index == 0

    def pop(self):
        if self.is_empty():
            self.next_index = 0
            return None
        self.next_index = -1
        self.num_elements -= 1
        return self.arr[self.next_index]

# Checking
foo = Stack()
print(foo.arr)
print("Pass" if foo.arr == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] else "Fail")

foo = Stack()
foo.push(1)
foo.push(2)
foo.push(3)
foo.push(4)
foo.push(5)
foo.push(6)
foo.push(7)
foo.push(8)
foo.push(9)
foo.push(10)  # The array is now at capacity!
foo.push(11)  # This one should cause the array to increase in size
print(foo.arr)  # Let's see what the array looks like now!
print("Pass" if len(foo.arr) == 20 else "Fail")
foo = Stack()
# We first have to push an item so that we'll have something to pop
foo.push("Test")
print(foo.pop())  # Should return the popped item, which is "Test"
print(foo.pop())
