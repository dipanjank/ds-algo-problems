"""
Find first `k` non-repeating characters in a string in a single traversal.

For example, if the string is ABCDBAGHCHFAC and k = 3, output would be 'D', 'G', 'F'.
"""
from collections import Counter
import heapq
from functools import total_ordering


@total_ordering
class Item:
    def __init__(self, val):
        self.val = val
        self.count = 0

    def __eq__(self, other):
        return self.count == other.count

    def __lt__(self, other):
        return self.count < other.count

    def inc(self):
        self.count += 1

def first_k_uniq_counter(s, k):
    """This requires 2 passes, first to count, then to check."""
    counts = Counter(list(s))
    uniq_chars = []
    for c in s:
        if counts[c] == 1:
            uniq_chars.append(c)
        if len(uniq_chars) == k:
            break

    return uniq_chars


def first_k_uniq_heap(s, k):


def main():
    assert first_k_uniq_counter("aabbcc", 2) == []
    assert first_k_uniq_counter("aabbcddeffg", 2) == ["c", "e"]


if __name__ == "__main__":
    main()
