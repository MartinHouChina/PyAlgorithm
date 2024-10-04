class TrieNode:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.weight = 0
        self.children = {}


class Trie(object):
    def __init__(self):
        self.root = TrieNode("")
    
    def insert(self, word):
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(char)
            node = node.children[char]
        
        node.is_end = True
        node.weight += 1
    