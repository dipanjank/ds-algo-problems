"""Given an array cost where each element cost[i] represents the cost of the ‘i-th’ step on a staircase,
we can climb either 1, 2, or 3 steps and we always start from the first stair. Find the minimum cost to climb all the
stairs."""
import math
from functools import lru_cache


def calc_cost(costs):
    n = len(costs)

    @lru_cache
    def dp(i):
        if i == 0:
            return 0

        c1 = dp(i - 1) + costs[i - 1]
        c2 = dp(i - 2) + costs[i - 2] if i > 1 else math.inf
        c3 = dp(i - 3) + costs[i - 3] if i > 2 else math.inf
        return min(c1, c2, c3)

    return dp(n)


if __name__ == '__main__':
    ans = calc_cost([2, 1, 3, 1, 2])
    print(ans)