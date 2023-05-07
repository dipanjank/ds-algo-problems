from typing import List


class Trie:

    def __init__(self, char=None) -> None:
        self.children = {}
        self.char = char
        self.is_word = False

    def __str__(self):
        return f"Trie(char={self.char}, is_word={self.is_word})"

    def __repr__(self) -> str:
        return str(self)

    def add(self, word):
        cur = self
        for char in word:
            if char in cur.children:
                cur = cur.children[char]
            else:
                cur.children[char] = Trie(char)
                cur = cur.children[char]

        cur.is_word = True

    def matches(self, prefix) -> List[str]:
        cur = self
        for char in prefix:
            if char in cur.children:
                cur = cur.children[char]
            else:
                return []

        words = []
        cur.get_words(prefix, words)
        return words

    def get_words(self, prefix, words):
        result = []
        if self.is_word:
            words.append(prefix)
        for char, child in self.children.items():
            child.get_words(prefix + char, words)
