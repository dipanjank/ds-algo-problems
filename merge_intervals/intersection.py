"""
Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.

Example 1:

Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
Output: [2, 3], [5, 6], [7, 7]
Explanation: The output list contains the common intervals between the two lists.

Example 2:
Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
Output: [5, 7], [9, 10]
Explanation: The output list contains the common intervals between the two lists.
"""
from operator import itemgetter


def intersection(interval1, interval2):
    interval1.sort(key=itemgetter(0))
    interval2.sort(key=itemgetter(0))

    idx1, idx2 = 0, 0
    n1, n2 = len(interval1), len(interval2)
    matches = []

    while idx1 < n1 and idx2 < n2:
        int1, int2 = interval1[idx1], interval2[idx2]
        if int1[1] < int2[0] or int1[0] > int1[1]:
            idx1 += 1
            idx2 += 1
        else:
            new_interval = [
                max(int1[0], int2[0]),
                min(int1[1], int2[1])
            ]
            matches.append(new_interval)
            if int1[1] == int2[1]:
                idx1 += 1
                idx2 += 1
            elif int1[1] > int2[1]:
                idx2 += 1
            else:
                idx1 += 1

    return matches


def main():
    m = intersection([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])
    print(m)
    assert m == [[2, 3], [5, 6], [7, 7]]


if __name__ == '__main__':
    main()