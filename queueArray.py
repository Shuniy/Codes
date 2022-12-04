"""
Functionality
Once implemented, our queue will need to have the following functionality:

enqueue - adds data to the back of the queue
dequeue - removes data from the front of the queue
front - returns the element at the front of the queue
size - returns the number of elements present in the queue
is_empty - returns True if there are no elements in the queue, and False otherwise
_handle_full_capacity - increases the capacity of the array, for cases in which the queue would otherwise overflow
Also, if the queue is empty, dequeue and front operations should return None.
"""

class Queue(object):
    def __init__(self, queue_size : int = 10):
        self.arr = [0 for _ in range(queue_size)]
        self.front_index = -1
        self.next_index = 0
        self.queue_size = 0

    def enqueue(self, value):
        self.arr[self.next_index] = value
        self.queue_size += 1
        self.next_index = (self.next_index + 1)
        if self.front_index == -1:
            self.front_index = 0

    def size(self):
        return self.queue_size

    def is_empty(self):
        return self.queue_size == 0

    def front(self):
        if self.front_index == -1:
            return None
        else:
            return self.arr[self.front_index]

    def dequeue(self):
        if self.is_empty():
            self.front_index = -1
            self.next_index = 0
            return None

        value = self.arr[self.front_index]
        self.front_index = (self.front_index + 1)
        self.queue_size -= 1
        return value

    def handle_queue_capacity_full(self):
        old_arr = self.arr
        self.arr = [0 for _ in range(2 * len(old_arr))]
        index = 0
        for i in range(self.front_index, len(old_arr)):
            self.arr[index] = old_arr[i]
            index += 1
        self.front_index = 0
        self.next_index = index


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
