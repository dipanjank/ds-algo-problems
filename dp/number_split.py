"""Split a positive integer n > 2 into at least 2 positive integers that sum to n and their product is the maximum.
Return the product."""
import functools


@functools.lru_cache
def max_product(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        val = 0
        for i in range(1, n):
            candidate = max(i * max_product(n - i), i * (n - i))
            val = max(val, candidate)
        return val


if __name__ == '__main__':
    ans = max_product(5)
    print(ans)