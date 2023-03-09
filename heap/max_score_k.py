"""
You are given a 0-indexed integer array nums and an integer k. You have a starting score of 0.

In one operation:

choose an index i such that 0 <= i < nums.length,
increase your score by nums[i], and
replace nums[i] with ceil(nums[i] / 3).
Return the maximum possible score you can attain after applying exactly k operations.

The ceiling function ceil(val) is the least integer greater than or equal to val.

Example 1:

Input: nums = [10,10,10,10,10], k = 5
Output: 50
Explanation: Apply the operation to each array element exactly once. The final score is 10 + 10 + 10 + 10 + 10 = 50.
"""
import heapq
from functools import total_ordering
import math


@total_ordering
class HeapItem:
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        return self.val == other.val

    def __lt__(self, other):
        return self.val > other.val


def max_score(nums, k):
    heap_data = [HeapItem(i) for i in nums]
    heapq.heapify(heap_data)

    total = 0
    for _ in range(k):
        max_item = heapq.heappop(heap_data)
        total += max_item.val
        new_val = math.ceil(max_item.val / 3)
        heapq.heappush(heap_data, HeapItem(new_val))

    return total


def main():
    assert max_score([1, 10, 3, 3, 3], 3) == 17
    assert max_score([10, 10, 10, 10, 10], 5) == 50


if __name__ == "__main__":
    main()
