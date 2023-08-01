"""A Segment Tree is a Data Structure that allows us to update an array and find the sum/min/max of a range in the
array in log(n) time.
"""
from typing import List


class SegmentNode:

    def __init__(self, range_start, range_end):
        self.total = 0
        self.left = None
        self.right = None
        self.range_start = range_start
        self.range_end = range_end

    def __str__(self):
        return f"SegmentNode(total={self.total}, range_start={self.range_start}, range_end={self.range_end})"

    def __repr__(self):
        return str(self)


class SegmentTree:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = self.build_tree(nums, 0, len(nums) - 1)

    def build_tree(self, nums, start, end):
        # Building the tree
        # A segment tree is a complete binary tree with n leaves, where each leaf corresponds to an element in nums
        # as such, the entire tree has 2n nodes. We represent this in an array of size 2n where the child of the node
        # at index i is the sum of the nodes at index 2i + 1 and 2i + 2.
        if start > end:
            return None
        node = SegmentNode(start, end)
        if start == end:
            node.total = nums[start]
        else:
            mid = (start + end) // 2
            node.left = self.build_tree(nums, start, mid)
            node.right = self.build_tree(nums, mid + 1, end)
            node.total = node.left.total + node.right.total
        return node

    def update(self, index: int, val: int):
        # recursively go to the node for index and update the value
        # then recalculate the total for all the parent nodes at every level up
        def update_node(node, i, v):
            if node is None:
                return
            if node.range_start == i and node.range_end == i:
                node.total = v
                return
            mid = (node.range_start + node.range_end) // 2
            if i <= mid:
                update_node(node.left, i, v)
            else:
                update_node(node.right, i, v)

            node.total = node.left.total + node.right.total

        update_node(self.tree, index, val)

    def sum_range(self, start: int, end: int) -> int:
        def get_sum(node, left, right):
            if not node or left > right:
                return 0
            if node.range_start == left and node.range_end == right:
                return node.total
            else:
                mid = (node.range_start + node.range_end) // 2
                # If end of the range is less than the mid, the entire interval lies in the left subtree
                if right <= mid:
                    return get_sum(node.left, left, right)
                # If start of the interval is greater than mid, the entire interval lies in the right subtree
                elif left >= mid + 1:
                    return get_sum(node.right, left, right)
                else:
                    s1 = get_sum(node.left, left, mid)
                    s2 = get_sum(node.right, mid + 1, right)
                    return s1 + s2

        return get_sum(self.tree, start, end)


if __name__ == '__main__':
    tree = SegmentTree([1, 2, 4, 7, 7, 2])
    tree.update(4, 5)
    val = tree.sum_range(0, 5)
    print(val)
