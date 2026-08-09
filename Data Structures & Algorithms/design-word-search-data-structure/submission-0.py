class TrieNode:
    def __init__(self):
        self.char = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.char:
                node.char[c] = TrieNode()
            node = node.char[c]
        node.isEnd = True
    def search(self, word: str) -> bool:
        def dfs(i, node):
            if i == len(word):
                return node.isEnd
            c = word[i]
            if c == '.':
                for char in node.char.values():
                    if dfs(i + 1, char):
                        return True
                return False
            if c not in node.char:
                return False
            return dfs(i + 1, node.char[c])
        return dfs(0, self.root)

# searching for a word in a data struct efficiently
# need to store letters in a node that we can trace and check if the word exist
# like a trietree
# tridenode has a dictionary and a isEnd from what i rmb
# all lowercase or . for fillers and at most 2 .