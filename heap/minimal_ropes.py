"""
Given n ropes of different lengths, connect them into a single rope with minimum cost. Assume that the cost to
connect two ropes is the same as the sum of their lengths.

Input:  [5, 4, 2, 8]

Output: The minimum cost is 36

[5, 4, 2, 8] –> First, connect ropes of lengths 4 and 2 that will cost 6.
[5, 6, 8]    –> Next, connect ropes of lengths 5 and 6 that will cost 11.
[11, 8]      –> Finally, connect the remaining two ropes that will cost 19.

Therefore, the total cost for connecting all ropes is 6 + 11 + 19 = 36.
"""

import heapq


def min_cost(lengths):
    lengths = [l for l in lengths]
    heapq.heapify(lengths)

    total = 0
    while len(lengths) > 1:
        l1 = heapq.heappop(lengths)
        l2 = heapq.heappop(lengths)
        total += l1 + l2
        heapq.heappush(lengths, l1 + l2)

    last = heapq.heappop(lengths)
    return total


if __name__ == "__main__":
    lengths = [5, 4, 2, 8]
    assert min_cost(lengths) == 36
