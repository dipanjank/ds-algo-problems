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


class UnionFind2:
    """This version does not use the representative element."""
    def __init__(self, items):
        self.group_items_map = {i: {item} for i, item in enumerate(items)}
        self.item_group_map = {item: i for i, item in enumerate(items)}

    def __len__(self):
        return len(self.group_items_map)

    def find(self, item):
        return self.item_group_map[item]

    def union(self, a, b):
        # Get the groups that each item belongs to.
        group_a, group_b = self.find(a), self.find(b)

        # If the items belong to the same group we shouldn't do anything.
        if group_a == group_b:
            return False

        # Get all items that are in item a's group.
        items_a = set(self.group_items_map[group_a])

        # Join these items with item b's group and remove the old group.
        self.group_items_map[group_b] |= items_a
        del self.group_items_map[group_a]

        # Update all the group number for all the items that were moved.
        for item in items_a:
            self.item_group_map[item] = group_b

        return True
