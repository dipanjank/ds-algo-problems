"""
Problem Statement
Given an array of intervals representing ‘N’ appointments, find out if a person can attend all the appointments.

Example 1:

Appointments: [[1,4], [2,5], [7,9]]
Output: false
Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.

Example 2:

Appointments: [[6,7], [2,4], [8,12]]
Output: true
Explanation: None of the appointments overlap, therefore a person can attend all of them.

Example 3:

Appointments: [[4,5], [2,3], [3,6]]
Output: false
Explanation: Since [4,5] and [3,6] overlap, a person cannot attend both of these appointments.
"""

from operator import itemgetter


def can_attend_all(events):
    # sort the events by the start time
    events.sort(key=itemgetter(0))

    for i, e in enumerate(events):
        if i == 0:
            current_end = e[1]
        else:
            if e[0] < current_end:
                return False
            else:
                current_end = e[1]

    return True


def main():
    assert not can_attend_all([[1, 4], [2, 5], [7, 9]])
    assert can_attend_all([[6, 7], [2, 4], [8, 12]])


if __name__ == '__main__':
    main()
