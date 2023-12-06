import dataclasses
import functools
import heapq
from typing import Optional, Union


@functools.total_ordering
@dataclasses.dataclass
class QueueEntry:
    priority: int
    item: Union[int, str]

    def __lt__(self, other):
        return self.priority < other.priority

    def __eq__(self, other):
        return self.priority == other.priority


class PriorityQueue:
    """Allows priority based enqueue and dequeue of items."""
    REMOVED = "<removed-item>"

    def __init__(self):
        self.q = []
        self.items = {}

    def enqueue(self, item: int, priority: int):
        """If item exists, remove it first, then add it into the PriorityQueue."""
        if item in self.items:
            self._remove(item)

        entry = QueueEntry(priority=priority,item=item)
        self.items[item] = entry
        heapq.heappush(self.q, entry)

    def _remove(self, item: int):
        """Mark the entry containing item as removed."""
        entry = self.items.pop(item)
        entry.item = self.REMOVED

    def dequeue(self) -> Optional[int]:
        """Remove the item with the least priority,ignoring the entries marked for deletion."""
        while self.q:
            mp_entry = heapq.heappop(self.q)
            if not mp_entry.item == self.REMOVED:
                return mp_entry.item
        raise KeyError("dequeue from empty PriorityQueue")


if __name__ == '__main__':
    pq = PriorityQueue()
    pq.enqueue(10, 5)
    pq.enqueue(20, 2)
    # expect 20
    print(pq.dequeue())

    pq.enqueue(20, 3)
    pq.enqueue(10, 1)
    # expect 10
    print(pq.dequeue())
