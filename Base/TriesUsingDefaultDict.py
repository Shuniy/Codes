"""
Trie using default Dict()

A cleaner way to build a trie is with a Python default dictionary. The following TrieNod class is using collections.defaultdict instead of a normal dictionary.
"""
import collections

class TrieNode:
    def __init__(self):
        self.chilren = collections.defaultdict(TrieNode)
        self.is_word = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        """
        Add 'word' to trie
        """
        node = self.root
        for i, char in enumerate(word):
            if i == len(word) - 1:
                node.children[char].is_word = True

            else:
                node.children[char]
                node = node.chilren[char]

    def exists(self, word):
        """
        Check if word exists in trie
        """
        node = self.root
        for i, char in enumerate(word):
            if i == len(word) - 1:
                return node.chilren[char].is_word
            else:
                node = node.chilren[char]


# Add words
valid_words = ['the', 'a', 'there', 'answer', 'any', 'by', 'bye', 'their']
word_trie = Trie()
for valid_word in valid_words:
    word_trie.add(valid_word)

# Tests
assert word_trie.exists('the')
assert word_trie.exists('any')
assert not word_trie.exists('these')
assert not word_trie.exists('zzz')
print('All tests passed!')

"""
The Trie data structure is part of the family of Tree data structures. It shines when dealing with sequence data, whether it's characters, words, or network nodes. When working on a problem with sequence data, ask yourself if a Trie is right for the job.
"""
