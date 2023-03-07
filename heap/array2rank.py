"""
Given an array of distinct integers, replace each array element by its corresponding rank in the array.

Example
-------

Input:  [10, 8, 15, 12, 6, 20, 1]
Output: [4, 3, 6, 5, 2, 7, 1]
"""

import heapq
from functools import total_ordering


@total_ordering
class Item:

    def __init__(self, index, val):
        self.index = index
        self.val = val

    def __eq__(self, other):
        return self.val == other.val

    def __lt__(self, other):
        return self.val < other.val


def rank(x):
    heap = [Item(i, v) for i, v in enumerate(x)]
    heapq.heapify(heap)
    ranks = [0] * len(heap)

    i = 0
    while heap:
        i += 1
        v = heapq.heappop(heap)
        ranks[v.index] = i

    return ranks


if __name__ == "__main__":
    x = [10, 8, 15, 12, 6, 20, 1]
    ranks = rank(x)
    assert ranks == [4, 3, 6, 5, 2, 7, 1]
