class SuffixTree:
    def __init__(self, string) -> None:
        self.root = {}
        self.end_symbol = "*"
        self.populate_suffix_tree_from(string)

    # Time : O(n^2)
    # Space : O(n^2)
    def populate_suffix_tree_from(self, string):
        for i in range(len(string)):
            self.insert_substring_starting_at(i, string)

    def insert_substring_starting_at(self, i , string):
        node = self.root
        for j in range(i, len(string)):
            letter = string[j]

            if letter not in node:
                node[letter] = {}

            node = node[letter]
        node[self.end_symbol] = True
    
    # Time : O(m) // m is the length of input string
    # Space : O(1)
    def contains(self, string):
        node = self.root

        for letter in string:
            if letter not in node:
                return False

            node = node[letter]
        # Return True if end_symbol present
        return self.end_symbol in node 
