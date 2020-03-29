"""
This problem is focused on the development of the of a trie a data structure derived from a tree, suited for a good ratio between time and space complexity.

Time and Space complexity
For the trie, time complexity of searching and inserting from a trie depends on the length of the word a that’s being searched for, inserted, and the number of total words, n, making the runtime of these operations O(a*n). Looking into the space complexity of a trie, the worst case, would be when we have a word (or words), with no common characters between them, hence having, a node for each letter. Resulting in a space complexity of O(n).

Building a Trie in Python
Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.

Before we move into the autocomplete function we need to create a working trie for storing strings. We will create two classes:

A Trie class that contains the root node (empty string)
A TrieNode class that exposes the general functionality of the Trie, like inserting a word or finding the node which represents a prefix.
"""

from ipywidgets import interact
from IPython.display import display
from ipywidgets import widgets
class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}

    def insert(self, char):
        if char not in self.children:
            self.children[char] = TrieNode()
        else:
            pass

    def suffixes(self, suffix = ''):
        results = []

        if self.is_word and suffix != '':
            results.append(suffix)
        if len(self.children) == 0:
            return results

        results = []

        if self.is_word and suffix != '':
            results.append(suffix)

        for char in self.children:
            results.extend(self.children[char].suffixes(suffix = suffix + char))

        return results

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node.insert(char)
            node = node.children[char]

        node.is_word = True

    def find(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return node


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f, prefix='');
