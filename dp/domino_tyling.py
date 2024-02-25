"""
Given a positive integer N, the task is to find the number of ways to fill the board of dimension 2*N with a
tile of dimensions 2 × 1, 1 × 2, (also known as domino) show below that can be rotated by 90 degrees.
"""
from functools import lru_cache


@lru_cache
def num_ways(n: int) -> int:
    if n in (1, 2):
        return n
    else:
        return num_ways(n - 1) + num_ways(n - 2)


if __name__ == '__main__':
    for n in [3, 4, 5]:
        print(n, num_ways(n))
