"""
You are given an integer array gifts denoting the number of gifts in various piles. Every second, you do the following:

Choose the pile with the maximum number of gifts.
If there is more than one pile with the maximum number of gifts, choose any.
Leave behind the floor of the square root of the number of gifts in the pile. Take the rest of the gifts.
Return the number of gifts remaining after k seconds.
"""

import heapq
import math
from functools import total_ordering


@total_ordering
class HeapItem:
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        return self.val == other.val

    def __lt__(self, other):
        return self.val > other.val


def max_gift(gifts, k):
    heap_data = [HeapItem(g) for g in gifts]
    heapq.heapify(heap_data)

    for _ in range(k):
        item = heapq.heappop(heap_data)
        if item.val > 1:
            remaining = int(math.sqrt(item.val))
            item = HeapItem(remaining)

        heapq.heappush(heap_data, item)

    return sum(item.val for item in heap_data)


def main():
    assert max_gift([25, 64, 9, 4, 100], 4) == 29
    assert max_gift([1, 1, 1, 1], 4) == 4


if __name__ == "__main__":
    main()
