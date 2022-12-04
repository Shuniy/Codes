"""
The lookup operation (i.e., get()) and put() / set() is supposed to be fast for a cache memory.

While doing the get() operation, if the entry is found in the cache, it is known as a cache hit. If, however, the entry is not found, it is known as a cache miss.

When designing a cache, we also place an upper bound on the size of the cache. If the cache is full and we want to add a new entry to the cache, we use some criteria to remove an element. After removing an element, we use the put() operation to insert the new element. The remove operation should also be fast.

For our first problem, the goal will be to design a data structure known as a Least Recently Used (LRU) cache. An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit.

Your job is to use appropriate data structure(s) to implement the cache.

In case of a cache hit, your get() operation should return the appropriate value.
In case of a cache miss, your get() should return -1.
While putting an element in the cache, your put() / set() operation must insert the element. If the cache is full, you must write code that removes the least recently used entry first and then insert the element.
All operations must take O(1) time.

For the current problem, you can consider the size of cache = 5.


For the LRU_Cache problem, after thinking of using different approaches (included previous failures), it has been decided to use the OrderedDict(), specifically the use of the method .popitem(last=False). It allows to remove the first added element, which is basic for the priority construction demanded.

Time and Space complexity
In respects to the limitation of the cache, any hashing approach has been discarded, as the risk of collision, hence the necessity of adding a nested hash (reaching O(n)). Finally deciding for this approach that satisfies the O(1) requirement. As in therms of space complexity, the structure requires the usage of c, being c the desired LRU_Cache capacity; being it in the end assimilable to O(n).
"""

from collections import OrderedDict


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache = OrderedDict
        self.capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self.capacity == 0:
            print("Can't Perform operations on 0 capacity cache")
            return
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
        else:
            if len(self.cache) < self.capacity:
                self.cache[key] = value
            else:
                self.cache.popitem(last=False)
                self.cache[key] = value

# Normal Case:
our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))
# returns 1
print(our_cache.get(2))
# returns 2
print(our_cache.get(9))
# returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))
# returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Edge Case:
our_cache = LRU_Cache(2)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(1, 10)
print(our_cache.get(1))
# should return 10
print(our_cache.get(2))
# should return 2

our_cache = LRU_Cache(0)
our_cache.set(1, 1)
# should print some message like "Can't perform operations on 0 capacity cache"
print(our_cache.get(1))
# should return -1
