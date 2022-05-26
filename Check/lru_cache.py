# LRU Cache operations should all be O(1) operation
# Time : O(1)
# Space : O(n) as general for doubly linked list and hash table

# Every operation performed below is Time : O(1)

class LRUCache:
    def __init__(self, max_size) -> None:
        self.max_size = max_size or 1
        self.cache = {}
        self.current_size = 0
        self.list_of_most_recent = DoublyLinkedList()

    def insert_key_value_pair(self, key, value):
        if key not in self.cahe:
            if self.current_size == self.max_size:
                self.evict_least_recent()
            else:
                self.current_size += 1
            
            self.cache[key] = DoublyLinkedListNode(key, value)
        else:
            self.replace_key(key, value)

        self.update_most_recent(self.cache[key])

    def evict_least_recent(self):
        key_to_remove = self.list_of_most_recent.tail.key
        self.list_of_most_recent.removeTail()
        del self.cache[key_to_remove]

    def update_most_recent(self, node):
        self.list_of_most_recent.setToHead(node)

    def replace_key(self, key, value):
        if key not in self.cache:
            raise Exception("The provided key not present in the LRU Cache!")

        self.cache[key].value = value

    def get_value_from_key(self, key):
        if key not in self.cache:
            return  None

        self.update_most_recent(self.cache[key])
        return self.cache[key].value
        
    def get_most_recent_key(self):
        return self.list_of_most_recent.head.key

# Insertion and deletion at head and tail are O(1)
# Accessing and Searching the node is O(n)
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setToHead(self, node):
        if self.head == node:
            return
        elif self.head is None:
            self.head = node
            self.tail = node
        elif self.head == self.tail:
            self.tail.prev = node
            self.head = node
            self.head.next = self.tail
        else:
            if self.tail == node:
                self.removeTail()
            node.removeBindings()
            self.head.prev = node
            node.next = self.head
            self.head = node

    def removeTail(self):
        if self.tail is None:
            return
        if self.tail == self.head:
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None


class DoublyLinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def removeBindings(self):
        if self.prev is not None:
            self.prev.next = self.next
        if self.next is not None:
            self.next.prev = self.prev
        self.prev = None
        self.next = None
