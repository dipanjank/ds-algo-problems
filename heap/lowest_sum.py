"""
Find k pairs with smallest sums in two arrays.

Examples:

Input :  arr1[] = {1, 7, 11}
         arr2[] = {2, 4, 6}
         k = 3
Output : [1, 2],
         [1, 4],
         [1, 6]
Explanation: The first 3 pairs are returned from the sequence [1, 2], [1, 4], [1, 6],  [7, 2], [7, 4], [11, 2], [7, 6], [11, 4], [11, 6]
"""
from operator import itemgetter


def smallest_k_sum(x1, x2, k):
    x1.sort()
    x2.sort()
    n1, n2 = len(x1), len(x2)

    result = []
    idx1, idx2 = 0, 0
    for _ in range(0, k):
        result.append((x1[idx1], x2[idx2]))

        if idx1 == n1 - 1 and idx2 == n2 - 1:
            break
        if idx1 == n1 - 1:
            idx1, idx2 = 0, idx2 + 1
            continue
        if idx2 == n2 - 1:
            idx1, idx2 = idx1 + 1, 0
            continue

        index_pairs = [(idx1 + 1, idx2), (idx1, idx2 + 1)]
        min_s, f1, f2 = float("inf"), 0, 0
        for j, k in index_pairs:
            s = x1[j] + x2[k]
            if s < min_s:
                min_s = s
                f1, f2 = j, k
        idx1, idx2 = f1, f2

    return result


def smallest_k_sum_bf(x1, x2, k):
    sums = []

    for i in x1:
        for j in x2:
            s = i + j
            sums.append([s, (i, j)])

    sums.sort(key=itemgetter(0))
    result = []
    for _, pair in sums[:k]:
        result.append(pair)

    return result


if __name__ == '__main__':
    arr1 = [1, 7, 11]
    arr2 = [2, 4, 6]

    r = smallest_k_sum(arr1, arr2, 3)
    assert set(r) == {(1, 2), (1, 4), (1, 6)}

    r = smallest_k_sum(arr1, arr2, 5)
    assert set(r) == {(1, 2), (1, 4), (1, 6), (7, 2), (7, 4)}

    r = smallest_k_sum(arr2, arr1, 3)
    assert set(r) == {(2, 1), (4, 1), (6, 1)}
