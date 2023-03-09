"""
Find median of streaming data.
"""
from functools import total_ordering
import heapq


@total_ordering
class HeapItem:

    def __init__(self, val, min_heap):
        self.val = val
        self.min = min_heap

    def __eq__(self, other):
        return self.val == other.val

    def __lt__(self, other):
        if self.min:
            return self.val < other.val
        else:
            return self.val > other.val


class BinaryHeap:

    def __init__(self, min_heap=True):
        self.min_heap = min_heap
        self.data = []

    def __len__(self):
        return len(self.data)

    def push(self, val):
        heapq.heappush(self.data, HeapItem(val, self.min_heap))

    def pop(self):
        v = heapq.heappop(self.data)
        return v.val

    def peek(self):
        return self.data[0].val


class MedianFinder:
    """
    Create two heaps.
        - A max heap to hold the left side of the sorted data so far
        - A min heap to hold the left side of the sorted data so far
        - If a new data point falls to the left of the max (root) element of the max heap, if goes to the max heap.
        - Otherwise it goes into the min heap
        - We always keep the two heaps balanced.
        - if n_items is even, median is the sum of the two roots
        - otherwise it is the root of the bigger heap
    """

    def __init__(self):
        self.min_heap = BinaryHeap(True)
        self.max_heap = BinaryHeap(False)
        self.n_items = 0

    def median(self, val):
        self.n_items += 1

        if not self.max_heap:
            self.max_heap.push(val)
            return val

        root_max = self.max_heap.peek()

        if val < root_max:
            self.max_heap.push(val)
        else:
            self.min_heap.push(val)

        if len(self.max_heap) - len(self.min_heap) > 1:
            v = self.max_heap.pop()
            self.min_heap.push(v)
        elif len(self.min_heap) - len(self.max_heap) > 1:
            v = self.min_heap.pop()
            self.max_heap.push(v)

        if self.n_items % 2 == 0:
            root_max = self.max_heap.peek()
            root_min = self.min_heap.peek()
            return (root_max + root_min) / 2.0
        else:
            if len(self.max_heap) > len(self.min_heap):
                return self.max_heap.peek()
            else:
                return self.min_heap.peek()


def main():
    values = [1, 2, 3, 5, 10, 11, 15, 17]
    medians = [1, 1.5, 2, 2.5, 3, 4, 5, 7.5]
    m = MedianFinder()
    for item, expected_median in zip(values, medians):
        if item == 17:
            pass
        actual_median = m.median(item)
        print(expected_median, actual_median)
        d = expected_median - actual_median

        assert abs(d) < 1E-4


if __name__ == "__main__":
    main()
