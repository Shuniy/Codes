#  also called prefix tree

import collections


class TrieNode:
    def __init__(self) -> None:
        self.isWord = False
        self.children = {}

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def add(self, word):
        node = self.root

        for i, char in enumerate(word):
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isWord = True


    def exists(self, word):
        node = self.root

        for i, char in enumerate(word):
            if len(word) - 1 == i:
                try:
                    node = node.children[char]
                    return node.isWord
                except KeyError:
                    return False
            else:
                try:
                    node = node.children[char]
                except KeyError:
                    return False

class TrieNode:
    def __init__(self) -> None:
        self.isWord = False
        self.children  = collections.defaultdict(TrieNode)

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def add(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        node.isWord = True

    def exists(self, word):
        node = self.root
        for char in word:
            node = node.children.get(char)
            if node is None:
                return False
        return node.isWord



word_list = ['apple', 'bear', 'goo', 'good',
             'goodbye', 'goods', 'goodwill', 'gooses', 'zebra']
word_trie = Trie()

# Add words
for word in word_list:
    word_trie.add(word)

# Test words
test_words = ['bear', 'goo', 'good', 'goos']
for word in test_words:
    if word_trie.exists(word):
        print('"{}" is a word.'.format(word))
    else:
        print('"{}" is not a word.'.format(word))
