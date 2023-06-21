def knapsack1(values: list, weights: list, capacity: int):
    # top-down DP
    items = list(zip(values, weights))
    n = len(items)

    # consider all possibilities for the i-the [value, weight] combination
    # there are two possibilities:
    # 1. take the i-th object if weight_sum + weight <= capacity
    # 2. Don't take the i-th object
    def backtrack(i, weight_sum, value_sum) -> int:
        # base cases
        if i == n:
            return value_sum

        #
        cur_value, cur_weight = items[i]
        if weight_sum + cur_weight <= capacity:
            take_i = backtrack(i + 1, weight_sum + cur_weight, value_sum + cur_value)
        else:
            take_i = 0

        not_take_i = backtrack(i + 1, weight_sum, value_sum)
        return max(take_i, not_take_i)

    ans = backtrack(0, 0, 0)
    return ans


def knapsack2(values: list, weights: list, capacity: int):
    # bottom up DP
    items = list(zip(values, weights))
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i, item in enumerate(items):
        cur_value, cur_weight = item

        for sum_weights in range(1, capacity + 1):
            if cur_weight <= sum_weights:
                dp[i + 1][sum_weights] = max(dp[i][sum_weights], dp[i][sum_weights - cur_weight] + cur_value)
            else:
                dp[i + 1][sum_weights] = dp[i][sum_weights]

    return dp[-1][-1]


if __name__ == '__main__':
    weights = [1, 2, 3]
    values = [6, 10, 12]
    capacity = 5
    ans = knapsack2(values=values, weights=weights, capacity=capacity)
    print(ans)
