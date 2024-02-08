# Implementation of trie

class TrieNode:
    def __init__(self):
        self.childern = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        '''
        Intalize the data strucutre
        '''
        self.root = TrieNode()

    def insert(self, word):

        cur = self.root

        for c in word:
            if c not in cur.childern:
                cur.childern[c] = TrieNode()
            cur = cur.childern[c]
        cur.endOfWord = True
    
    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.childern:
                return False
            cur = cur.childern[c]
    
        return cur.endOfWord
    
    def startsWith(self, prefix):
        cur = self.root

        for c in prefix:
            if c not in cur.childern:
                return False
            cur = cur.childern[c]
        return True