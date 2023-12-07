"""
A Fenwick Tree, or a Binary Indexed Tree, allows us to

* Calculate sum of a range of values in O(log N) time
* Update the value at an index, and then update the pre-computed data structure in O(log N) time

A Fenwick Tree is represented as an array, where each element at index i stores the cumulative sum of a specific range
in the original array. The key idea is to use the binary representation of the index to determine which elements
contribute to the cumulative sum.

It's easier to assume that the array index is 1 based. Then for an array of size n, the Fenwick tree nodes are calculated
by the formula:

F[i] = sum(A[k]) for k = i-LSB(i)+1,...,i where LSB(i) is the least significant bit in the binary representation of i

For example:

F[1] = A[1]
F[2] = A[1] + A[2]
F[3] = A[3]
F[4] = A[1] + A[2] + A[3] + A[4]
F[5] = A[5]
F[6] = A[5] + A[6]
F[7] = A[7]
F[8] = A[1] + A[2] + A[3] + A[4] + A[5] + A[6] + A[7] + A[8]
F[9] = A[9]
F[10] = A[9] + A[10]
F[11] = A[11]
F[12] = A[9] + A[10] + A[11] + A[12]
F[13] = A[13]
F[14] = A[13] + A[14]
F[15] = A[15]
F[16] = A[1] + A[2] + A[3] + A[4] + A[5] + A[6] + A[7] + A[8] + A[9] + A[10] + A[11] + A[2] + A[13] + A[14] + A[15] + A[16]

Range Sum Calculation
---------------------
Let's say we want to calculate sum(A[1,2,...,6]) = A[1] + A[2] + A[3] + A[4] + A[5] + A[6]. This can be written as

A[1] + A[2] + A[3] + A[4] + A[5] + A[6] = (A[1] + A[2] + A[3] + A[4]) + (A[5] + A[6]) = F(4) + F(6)

Note that 6 = 110b and 4 = 100b. So to calculate the range sum, we

* result = 0
* take the binary representation of the end index
* add F(index) to the result
* set index = set LSB of index = 0
* repeat until index = 0

Update value at index
---------------------
Update works similarly, but in the opposite direction. Adding delta to F[index] does not change F[0],.., F[index -1].
It only affects F[k] where index < k < n where k is found by progressively adding 1 the LSB of index.

For example, say we added delta to A[9]. We need to update F[9], F[10], F[12] and F[16]
(01001 -> 01010 -> 01100 -> 10000)
"""

from typing import List


class FenwickTree:

    def __init__(self, items: List[int]):
        self.n = len(items) + 1
        self.fenwick_tree = [0] * self.n
        for i, val in enumerate(items):
            self.update(i, val)

    def update(self, index: int, delta: int):
        """Add delta to the value at index i to val."""
        index += 1
        while index < self.n:
            self.fenwick_tree[index] += delta
            index = self.child_index(index)

    def sum_range(self, index: int) -> int:
        """Return the sum of values at index 0 to index, both inclusive."""
        index += 1
        result = 0
        while index > 0:
            print(index, self.fenwick_tree[index])
            result += self.fenwick_tree[index]
            index = self.parent_index(index)

        return result

    def sum_range_partial(self, left: int, right) -> int:
        """Return the sum of values at index left to index right, both inclusive."""
        left_sum = self.sum_range(left - 1)
        right_sum = self.sum_range(right)
        return right_sum - left_sum

    @staticmethod
    def lsb(index: int) -> int:
        """Return the LSB of index"""
        return index & -index

    def parent_index(self, index: int) -> int:
        """Return the index of the Fenwick parent."""
        return index - self.lsb(index)

    def child_index(self, index: int) -> int:
        return index + self.lsb(index)


if __name__ == '__main__':
    items = [2, 16, 8, 7, 3, 10, 5, 9, 1, 4]

    ft = FenwickTree(items)
    print(ft.sum_range(2), sum(items[:3]))
    print(ft.sum_range(7), sum(items[:8]))
