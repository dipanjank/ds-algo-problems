"""Implement a MaxHeap in python.

The heapq module implements methods for a min heap only. Here we wrap the code in a ``HeapItem`` class which inverts
the meaning of the ``__lt__`` operator, i.e. HeapItem(2) > HeapItem(3). This allows us to reuse the heapq methods to
maintain a min heap of ``HeapItem`` objects. In a min-heap, the smallest object is always at the root level. In this
case, this is the `HeapItem`` with the biggest value.
"""
import heapq
from functools import total_ordering


@total_ordering
class HeapItem:
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        return self.val == other.val

    def __lt__(self, other):
        return self.val > other.val


class MaxHeap:
    def __init__(self, initial_values=None):
        self.items = []
        if initial_values:
            for v in initial_values:
                self.items.append(HeapItem(v))
            heapq.heapify(self.items)

    def __len__(self):
        return len(self.items)

    def heappush(self, val):
        heapq.heappush(self.items, HeapItem(val))

    def heappop(self):
        v = heapq.heappop(self.items)
        return v.val

    def heapreplace(self, val):
        v = heapq.heapreplace(HeapItem(val))
        return v.val

    def heappushpop(self, val):
        v = heapq.heappushpop(HeapItem(val))
        return v.val


def main():
    vals = [1, 10, 7, -3, 2, 11, 9, 6]
    m = MaxHeap(initial_values=vals)
    while m:
        print(m.heappop())


if __name__ == "__main__":
    main()
