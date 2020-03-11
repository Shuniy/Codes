"""
Collision Handling
As discussed earlier, when two different inputs produce the same output, then we have a collision. Our implementation of get_hash_code() function is satisfactory. However, because we are using compression function, we are prone to collisions.

Consider the following scenario.

We have a bucket array of length 10 and we get two different hash codes for two different inputs, say 355, and 1095. Even though the hash codes are different in this case, the bucket index will be same because of the way we have implemented our compression function. Such scenarios where multiple entries want to go to the same bucket are very common. So, we introduce some logic to handle collisions.

There are two popular ways in which we handle collisions.

Closed Addressing or Separate chaining
Open Addressing

Closed addressing is a clever technique where we use the same bucket to store multiple objects. The bucket in this case will store a linked list of key-value pairs. Every bucket has it's own separate chain of linked list nodes.

In open addressing, we do the following:

If, after getting the bucket index, the bucket is empty, we store the object in that particular bucket

If the bucket is not empty, we find an alternate bucket index by using another function which modifies the current hash code to give a new code

Separate chaining is a simple and effective technique to handle collisions and that is what we discuss here.

Implement the put and get function using the idea of separate chaining.
"""

class LinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMap:
    def __init__(self, initial_size = 15):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p = 31
        self.num_entries = 0
        self.load_factor = 0.7

    def put(self, key, value):
        bucket_index = self.get_bucket_index(key)
        new_node = LinkedListNode(key, value)
        head = self.bucket_array[bucket_index]
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next
        head = self.bucket_array[bucket_index]
        new_node.next = head
        self.bucket_array[bucket_index] = new_node
        self.num_entries += 1

    def get(self, key):
        bucket_index = self.get_hash_code(key)
        head = self.bucket_array[bucket_index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return None

    def get_bucket_index(self, key):
        return self.get_hash_code(key)

    def get_hash_code(self, key):
        key = str(key)
        num_buckets = len(self.bucket_array)
        current_coefficient = 1
        hash_code = 0
        for character in key:
            hash_code += ord(character) * current_coefficient
            hash_code = hash_code % num_buckets
            current_coefficient *= self.p
            current_coefficient = current_coefficient % num_buckets

        return hash_code % num_buckets

    def size(self):
        return self.num_entries

    def _rehash(self):
        old_num_buckets = len(self.bucket_array)
        old_bucket_array = self.bucket_array
        num_buckets = 2 * old_num_buckets
        self.bucket_array = [None for _ in range(num_buckets)]
        for head in old_bucket_array:
            while head is not None:
                key = head.key
                value = head.value
                self.put(key, value)
                head = head.next

    def delete(self, key):
        bucket_index = self.get_bucket_index(key)
        head = self.bucket_array[bucket_index]
        previous = None
        while head is not None:
            if head.key == key:
                if previous is None:
                    self.bucket_array[bucket_index] = head.next
                else:
                    previous.next = head.next
                self.num_entries -= 1
                return
            else:
                previous = head
                head = head.next


hash_map = HashMap(7)

hash_map.put("one", 1)
hash_map.put("two", 2)
hash_map.put("three", 3)
hash_map.put("neo", 11)

print("size: {}".format(hash_map.size()))


print("one: {}".format(hash_map.get("one")))
print("neo: {}".format(hash_map.get("neo")))
print("three: {}".format(hash_map.get("three")))
print("size: {}".format(hash_map.size()))

hash_map.delete("one")

print(hash_map.get("one"))
print(hash_map.size())
