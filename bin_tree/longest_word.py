"""
Given an array of strings words representing an English Dictionary, return the longest word in words that can be built one character at a time by other words in words.

If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.

Note that the word should be built from left to right with each additional character being added to the end of a previous word. 

 

Example 1:

Input: words = ["w","wo","wor","worl","world"]
Output: "world"
Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
"""

from collections import deque

class Trie:

    def __init__(self):
        self.is_word = False
        self.children = {}

    def add_word(self, word):
        cur = self
        for w in word:
            if w in cur.children:
                cur = cur.children[w]
            else:
                cur.children[w] = Trie()
                cur = cur.children[w]
        cur.is_word = True

    def word_children(self):
        result = []
        for c, child in self.children.items():
            if child.is_word:
                result.append((c, child))

        return result
    
class Solution:
    def longestWord(self, words: List[str]) -> str:
        words = list(set(words))
        t = Trie()
        for w in words:
            t.add_word(w)
        
        answer = []

        def dfs(node, c, path):
            if not node:
                return
            if node.is_word:
                path = path + c
            wc = node.word_children()
            if wc:
                for char, child in wc:
                    dfs(child, char, path)
            else:
                answer.append(path)

        dfs(t, None, "")
        if answer:
            max_len = 0
            for w in answer:
                max_len = max(max_len, len(w))
            answer = [w for w in answer if len(w) == max_len]
            answer.sort()
            return answer[0]
        else:
            return ""
        
