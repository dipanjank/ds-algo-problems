from collections import defaultdict


class UnionFind:

    def __init__(self, data):
        self.parent = {item: item for item in data}

    def root(self, item):
        """Return the root element of the set item belongs to."""
        v = item
        while self.parent[v] != v:
            v = self.parent[v]
        return v

    def union(self, x, y):
        """Connect x and y to the same set. The representative element is the smallest element in the set."""
        root_x = self.root(x)
        root_y = self.root(y)
        if root_x == root_y:
            return
        if root_x > root_y:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x

    def connected(self, x, y):
        """Return True if x and y are in the same set."""
        return self.root(x) == self.root(y)

    def partitions(self, data):
        """Return the partitions as separate lists."""
        parts = defaultdict(list)
        for item in data:
            root = self.root(item)
            parts[root].append(item)

        return list(parts.values())
