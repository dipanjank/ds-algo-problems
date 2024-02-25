"""
Given a rod of length n inches and an array of prices that includes prices of all pieces of size smaller than n.
Determine the maximum value obtainable by cutting up the rod and selling the pieces. For example, if the length of the
rod is 8 and the values of different pieces are given as the following, then the maximum obtainable value is 22
(by cutting in two pieces of lengths 2 and 6)

length   | 1   2   3   4   5   6   7   8
--------------------------------------------
price    | 1   5   8   9  10  17  17  20

And if the prices are as follows, then the maximum obtainable value is 24 (by cutting in eight pieces of length 1)

length   | 1   2   3   4   5   6   7   8
--------------------------------------------
price    | 3   5   8   9  10  17  17  20
"""
import functools


def max_value(prices: list) -> int:
    # make the index 1 based
    prices = [0] + prices
    n = len(prices) - 1

    @functools.lru_cache
    def dp(k: int) -> int:
        if k == 1:
            return prices[k]
        result = 0
        for i in range(k - 1, -1, -1):
            result = max(result, dp(i) + prices[k - i])
        return result

    return dp(n)


if __name__ == '__main__':
    for prices in [
        [2, 4, 7, 8],
        [1, 5, 8, 9, 10, 17, 17, 20],
        [3, 5, 8, 9, 10, 17, 17, 20],
    ]:
        ans = max_value(prices)
        print(prices, ans)
