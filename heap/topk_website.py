"""
You are given a list of (website, user) pairs that represent users visiting websites. Come up with a program that
identifies the top k pairs of websites with the greatest similarity.

For example, suppose k = 1, and the list of tuples is:
[('a', 1), ('a', 3), ('a', 5),
 ('b', 2), ('b', 6),
 ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5),
 ('d', 4), ('d', 5), ('d', 6), ('d', 7),
 ('e', 1), ('e', 3), ('e', 5), ('e', 6)]
Then a reasonable similarity metric would most likely conclude that a and e are the
most similar, so your program should return [('a', 'e')].
"""
import heapq
from collections import defaultdict
from functools import total_ordering


@total_ordering
class HeapItem:

    def __init__(self, w1, w2, score):
        self.w1 = w1
        self.w2 = w2
        self.score = score

    def __eq__(self, other):
        return self.score == other.score

    def __lt__(self, other):
        return self.score > other.score


class MaxHeap:

    def __init__(self):
        self.items = []

    def push(self, item):
        heapq.heappush(self.items, item)

    def pop(self):
        return heapq.heappop(self.items)

    def __len__(self):
        return len(self.items)


def similar_websites(pairs, k):
    users = defaultdict(list)

    for w, u_id in pairs:
        users[w].append(u_id)

    web_list = list(users.keys())
    n_web = len(web_list)

    item_heap = MaxHeap()

    for i in range(n_web - 1):
        for j in range(i + 1, n_web):
            w1, w2 = web_list[i], web_list[j]
            u_w1, u_w2 = users[w1], users[w2]

            common = set(u_w1).intersection(u_w2)
            union = set(u_w1).union(u_w2)
            score = len(common) / len(union)
            item_heap.push(HeapItem(w1, w2, score))

    top_k_pairs = []

    while item_heap and len(top_k_pairs) < k:
        item = item_heap.pop()
        top_k_pairs.append((item.w1, item.w2))

    return top_k_pairs


def main():
    pairs = [('a', 1), ('a', 3), ('a', 5),
        ('b', 2), ('b', 6),
        ('c', 1), ('c', 2), ('c', 3), ('c', 4), ('c', 5),
        ('d', 4), ('d', 5), ('d', 6), ('d', 7),
        ('e', 1), ('e', 3), ('e', 5), ('e', 6)
    ]
    result = similar_websites(pairs, 1)
    assert result == [("a", "e")]


if __name__ == "__main__":
    main()


