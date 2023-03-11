"""
Given a set of n number of tasks, implement a task scheduler method, tasks(), to run in  time that finds the minimum
number of machines required to complete these n tasks.
"""
import dataclasses
import heapq
from functools import total_ordering
from operator import attrgetter


@dataclasses.dataclass
class Task:
    start: int
    end: int


@total_ordering
class TaskItem:

    def __init__(self, task, attr_getter):
        self.task = task
        self.attr_getter = attr_getter

    def __eq__(self, other):
        return self.attr_getter(self.task) == self.attr_getter(other.task)

    def __lt__(self, other):
        return self.attr_getter(self.task) < self.attr_getter(other.task)


class TaskHeap:

    def __init__(self, attr_name):
        self.heap_data = []
        self.attr_getter = attrgetter(attr_name)

    def __len__(self):
        return len(self.heap_data)

    def push(self, task):
        heapq.heappush(self.heap_data, TaskItem(task, self.attr_getter))

    def pop(self):
        v = heapq.heappop(self.heap_data)
        return v.task

    def peek(self):
        return self.heap_data[0].task


def min_machines(tasks):
    """This solution uses two min heaps. One for the start time and one for the end time.

    * Initially all the tasks are in the start heap.
    * At each round we pop the root of the start heap, which is the task with the earliest start time (the current task)
    * If the end heap is empty, we push the current task to the end heap increment the machine count by 1
    * otherwise we compare the task to the top of the end heap. This is the currently executing task with the earliest
    end time.
    * If the running task ends before the start of the current task, then we need a new machine, so we increment machine_count
    * Otherwise we pop the task at the root of the end heap and keep the machine count the same.
    """
    start_heap = TaskHeap("start")
    end_heap = TaskHeap("end")

    for start, end in tasks:
        t = Task(start, end)
        start_heap.push(t)

    machine_count = 0
    max_count = 0

    while start_heap:
        earliest_start = start_heap.pop()
        print(f"Before {earliest_start}, machine_count={machine_count}")
        if end_heap:
            while end_heap:
                earliest_end = end_heap.peek()
                if earliest_start.start < earliest_end.end:
                    break
                else:
                    end_heap.pop()
                    machine_count -= 1

        machine_count += 1
        end_heap.push(earliest_start)

        if machine_count > max_count:
            max_count = machine_count

    return max_count


if __name__ == "__main__":
    tasks = [(1, 7), (8, 9), (3, 6), (9, 14), (6, 7)]
    assert min_machines(tasks) == 2

    tasks = [(2, 5), (2, 5), (2, 5), (2, 5)]
    assert min_machines(tasks) == 4

    tasks = [(1, 7), (8, 13), (5, 6), (10, 14), (6, 7)]
    assert min_machines(tasks) == 2

    tasks = [(12, 13), (13, 15), (17, 20), (13, 14), (19, 21), (18, 20)]
    assert min_machines(tasks) == 3
