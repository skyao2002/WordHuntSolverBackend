from django.apps import AppConfig
from .trie import TrieNode, add

class SolverConfig(AppConfig):
    print("loading needed values...")
    dictionaryLoaded = False
    dictionaryTrie = TrieNode()

    print("loading dictionary")
    with open("solver/dictionary.txt", "r") as infile:
        for line in infile:
            word = line.rstrip()
            curr = dictionaryTrie
            for i, char in enumerate(word):
                if not char in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
                if i == len(word) - 1:
                    curr.word_finished = True
    
    dictionaryLoaded = True

class TrieNode(object):
    """
    Our trie node implementation. Very basic. but does the job
    """
    
    def __init__(self):
        self.children = {}
        # Is it the last character of the word.`
        self.word_finished = False


