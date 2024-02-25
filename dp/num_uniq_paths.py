"""
Consider a maze mapped to a matrix with the upper left corner at coordinates (row, column) = (0, 0).
You can only move towards the right or down from a cell. Determine the number of distinct paths through the maze.
You must always start from the top-left position (0, 0) and end at the bottom-right (n-1, m-1).

Count the number of ways you can complete this journey.
"""
import functools


@functools.lru_cache
def path_count(m: int, n: int) -> int:
    if m == 1 or n == 1:
        return 1
    else:
        return path_count(m - 1, n) + path_count(m, n - 1)


if __name__ == '__main__':
    for m, n in [(2, 2), (3, 3), (3, 4), (50, 20)]:
        ans = path_count(m, n)
        print(m, n, ans)
