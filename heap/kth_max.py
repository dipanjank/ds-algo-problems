"""
Find the k-th maximum in a stream of numbers
"""
import heapq


class KthMax:
    def __init__(self, k):
        self.k = k
        self.heap_data = []

    def find_max(self, item):
        if len(self.heap_data) < self.k:
            # fill up the heap with first k items
            heapq.heappush(self.heap_data, item)
        else:
            # if item < root (min) in the heap, we can ignore it because it's not in top k
            # otherwise we replace the root node with item
            if item > self.heap_data[0]:
                heapq.heapreplace(self.heap_data, item)

        v = self.heap_data[0]
        return v if len(self.heap_data) >= self.k else -1


def test():
    m = KthMax(3)
    assert m.find_max(10) == -1
    assert m.find_max(7) == -1
    assert m.find_max(12) == 7
    assert m.find_max(14) == 10
    assert m.find_max(1) == 10
    assert m.find_max(5) == 10


if __name__ == "__main__":
    test()