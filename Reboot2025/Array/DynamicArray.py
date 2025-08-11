class DynamicArray:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.array = [0] * self.capacity

    def get(self, i: int) -> int:
        if i >= self.capacity:
            raise IndexError("Out of Index!")

        return self.array[i]

    def set(self, i: int, n: int) -> None:
        if i >= self.capacity:
            raise IndexError("Out of Index!")

        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.capacity == self.length:
            self.resize()

        self.array[self.length] = n
        self.length += 1

    def popback(self) -> int:
        if self.length > 0:
            self.length -= 1

        element = self.array[self.length]
        return element

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        arr = [0] * self.capacity
        for i in range(self.length):
            arr[i] = self.array[i]

        self.array = arr
        del arr

    def getSize(self) -> int:
        return self.length

    def getCapacity(self) -> int:
        return self.capacity
