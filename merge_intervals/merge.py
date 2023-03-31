"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an
array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

from operator import itemgetter


def merge_intervals(intervals):
    intervals.sort(key=itemgetter(0))
    n = len(intervals)
    if n <= 1:
        return intervals
    current = 0

    while True:
        if current >= n - 1:
            break
        i1 = intervals[current]
        i2 = intervals[current + 1]
        if i1[1] >= i2[0]:
            int_ = [i1[0], max(i1[1], i2[1])]
            intervals.pop(current + 1)
            intervals.pop(current)
            intervals.insert(current, int_)
            n -= 1
        else:
            current += 1

        return intervals


def main():
    intervals = [[1, 4], [0, 2], [3, 5]]
    merge_intervals(intervals)
    assert intervals == [[0, 5]]


if __name__ == '__main__':
    main()



