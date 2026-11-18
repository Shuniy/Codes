class HashTable(object):
    def __init__(self):
        self.table = [None] * 10000

    def store(self, string):
        self.table[self.calculate_hash_value(string)] = [string]

    def lookup(self, string):
        hash_value = self.calculate_hash_value(string)
        if self.table[hash_value] is not None:
            return hash_value
        else:
            return -1

    def calculate_hash_value(self, string):
        return ord(string[0]) * 100 + ord(string[1])


hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print(hash_table.calculate_hash_value('ZippySphinx'))

# Test lookup edge case
# Should be -1
print(hash_table.lookup('ZippySphinx'))

# Test store
hash_table.store('ZippySphinx')
# Should be 8568
print(hash_table.lookup('ZippySphinx'))

# Test store edge case
hash_table.store('DELICIOUS')
# Should be 8568
print(hash_table.lookup('DELICIOUS'))
