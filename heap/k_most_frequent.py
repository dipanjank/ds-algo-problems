"""
Find the k most frequent items.
"""
import heapq
from collections import Counter
from functools import total_ordering


@total_ordering
class Item:
    def __init__(self, val, count):
        self.val = val
        self.count = count

    def __eq__(self, other):
        return self.count == other.count

    def __lt__(self, other):
        return self.count < other.count

    def __str__(self):
        return f"Item(val={self.val}, count-{self.count})"


def most_frequent(items, k):
    counter = Counter(items)
    item_heap = []

    for val, count in counter.items():
        item = Item(val, count)
        heapq.heappush(item_heap, item)

    n_take = len(item_heap) - k + 1
    freq_items = [heapq.heappop(item_heap).val for _ in range(n_take)]
    return freq_items


def main():
    items = [1, 1, 1, 2, 2, 3]
    v = most_frequent(items, 2)
    assert set(v) == {2, 3}


if __name__ == "__main__":
    main()
