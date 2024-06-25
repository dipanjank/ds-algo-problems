"""
Given a set of non-negative integers and a value sum, the task is to check if there is a subset of the given set whose
sum is equal to the given sum.
"""


def subset_sum(arr, target):
    arr.sort()
    n = len(arr)
    dp = [[False] * (target + 1) for _ in range(n)]
    if arr[0] <= target:
        dp[0][arr[0]] = True

    for i in range(1, n):
        num = arr[i]
        for j in range(1, target + 1):
            not_take = dp[i - 1][j]
            take = dp[i - 1][j - num] if num <= j else False
            dp[i][j] = take or not_take

    # pprint(dp)
    return dp[-1][-1]


if __name__ == '__main__':
    nums = [3, 14, 4, 12, 5]
    for t in range(1, 30):
        print(t, subset_sum(nums, t))
