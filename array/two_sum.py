"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
"""
from typing import List
from collections import defaultdict


def two_sum_brute_force(x: List[int], target: int) -> List[int]:
    if not x or len(x) < 2:
        return []
    if len(x) == 2:
        return [0, 1] if sum(x) == target else []

    n = len(x)
    for i in range(n):
        for j in range(i+1, n):
            if x[i] + x[j] == target:
                return [i, j]
    return []


def two_sum(x: List[int], target: int) -> List[int]:
    positions = defaultdict(list)

    if not x or len(x) < 2:
        return []
    if len(x) == 2:
        return [0, 1] if sum(x) == target else []

    for i, e in enumerate(x):
        positions[e].append(i)

    for i, e in enumerate(x):
        rem = target - e
        rem_pos = positions[rem]
        if rem != e and rem_pos:
            return [i, rem_pos[0]]
        if rem == e:
            for v in rem_pos:
                if v != i:
                    return [i, v]

    return []


def test():
    assert two_sum([1, 3, 7, 9, 2], 11) == [3, 4]
    assert two_sum([1, 3, 7, 9, 2], 10) == [0, 3]
    assert two_sum([1, 3, 7, 9, 2], 16) == [2, 3]
    assert two_sum([1, 3, 7, 9, 2], 4) == [0, 1]
    assert two_sum([1, 3, 7, 9, 2], 20) == []
    assert two_sum([1, 4, 5, 4, 3], 8) == [1, 3]


if __name__ == "__main__":
    test()


