"""
Given an array of vertical bar lengths, find the maximum possible area created between them.
"""

from typing import List


def max_area_brute_force(x: List[int]) -> int:
    n = len(x)
    max_area_val = 0

    for x1, y1 in enumerate(x):
        for x2 in range(x1 + 1, n):
            y2 = x[x2]
            area_val = (x2 - x1) * min(y1, y2)
            if area_val > max_area_val:
                max_area_val = area_val

    return max_area_val


def max_area(x: List[int]) -> int:
    n = len(x)

    max_area_val = 0
    x1, x2 = 0, n - 1

    while x1 < x2:
        area_val = (x2 - x1) * min(x[x1], x[x2])
        if area_val > max_area_val:
            max_area_val = area_val
        if x[x1] <= x[x2]:
            x1 += 1
        else:
            x2 -= 1

    return max_area_val


def main():
    assert max_area([7, 1, 2, 3, 9]) == 7 * 4
    assert max_area([4, 8, 1, 2, 3, 9]) == 8 * 4


if __name__ == "__main__":
    main()