# Time : O((ws + nm) * 8^s) // Atmost 8 neighbors
# Space : O(ws + nm) // (Trie) w number of words and size of words, n and m dimensions of matrix
# // no more than s function call stack that is s recursive calls


def boggleBoard(board, words):
    trie = Trie()
    for word in words:
        trie.add(word)
    finalWords = {}
    visited = [[False for letter in row] for row in board]
    for i in range(len(board)):
        for j in range(len(board[i])):
            explore(i, j, board, trie.root, visited, finalWords)
    return list(finalWords.keys())


def explore(i, j, board, trie, visited, finalWords):
    if visited[i][j] == True:
        return

    if board[i][j] not in trie:
        return

    visited[i][j] = True

    directions = getNeighbours(i, j, board)
    trie = trie[board[i][j]]

    if '*' in trie:
        finalWords[trie['*']] = True
    
    for direction in directions:
        explore(direction[0], direction[1], board, trie, visited, finalWords)

    visited[i][j] = False

def getNeighbours(i, j, board):
    neighbours = []
    possibleDirections = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                          (1, 0), (1, -1), (0, -1), (-1, -1)]
    for direction in possibleDirections:
        di, dj = direction
        newI, newJ = i + di, j + dj
        if 0 <= newI < len(board) and 0 <= newJ < len(board[0]):
            neighbours.append([newI, newJ])
    return neighbours


class Trie:
    def __init__(self):
        self.root = {}
        self.endSymbol = "*"

    def add(self, word):
        current = self.root
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.endSymbol] = word
